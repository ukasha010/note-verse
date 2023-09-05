from django.shortcuts import render , redirect , HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from verify_email.email_handler import send_verification_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from stickynotes.forms import StickyNotesForm
from stickynotes.models import StickyNote
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NotesForm , TodoListForm
from .models import TodoList , Note
# Create your views here.
def home(request):
    return render(request , 'Notes/index.html')

def features(request):
    return render(request , 'Notes/features.html')

def why_us(request):
    return render(request , 'Notes/why-us.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            inactive_user = send_verification_email(request , form)
            return render(request , 'Notes/confirm-email.html')
        else:
            for field , errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}" , extra_tags=f"{field}")
            return redirect('account_signup') 
    else:
        form = UserRegistrationForm()
        return render(request , 'Notes/signup.html' , {'form' : form})

@login_required
def dashboard(request):
    if request.method == 'POST':
        form = StickyNotesForm(request.POST)
        if form.is_valid():
            SNote = form.cleaned_data.get('SNote')
            Writer = request.user
            stickynote = StickyNote(SNote = SNote , Writer = Writer)
            stickynote.save()
            messages.success(request , "Sticky Note Successfully Added!")
            return redirect('dashboard')
    form = StickyNotesForm()
    return render(request , "Notes/dashboard.html" , {'form' : form})

def account_delete_confirmation(request):
    return render(request , "Notes/account_delete_confirmation.html")
def delete_account(request):
    user = User.objects.get(username=request.user.username)
    user.delete()
    return redirect("home")

class TodoListView(LoginRequiredMixin , View):
    
    def post(self , request , *args , **kwargs):
        form = TodoListForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            TodoList.objects.create(Writer = request.user , title = title , description = description)
            return redirect('todo-list')
        return HttpResponse("Error")
    
    def get(self , request , *args , **kwargs):
        
        form = TodoListForm()
        Todos = TodoList.objects.filter(Writer = request.user)
        
        context = {
            'form' : form,
            'Todos' : Todos
        }
        return render(request , 'Notes/todo-list.html' , context)
    
class NotesView(LoginRequiredMixin , View):
    
    def get(self , request , *args , **kwargs):
        
        notes = Note.objects.filter(writer = request.user)
        form = NotesForm()
        context = {
            'form' : form,
            'notes' : notes,
            'buttons' : ['Save']
        }
        return render(request , 'Notes/notes.html' , context)
    
    def post(self , request , *args , **kwargs):
        form = NotesForm(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            Note.objects.create(writer = request.user , title = title , description = description)
            return redirect('notes')
        else:
            return redirect('notes')

#"This Will Also Update The Note."        
class NoteDetailView(View):
    
    def post(self , request , id , *args , **kwargs):
        note = Note.objects.get(id = id)
        
        form = NotesForm(request.POST , instance = note)
        
        if form.is_valid():
            form.save()
            return redirect('note-detail' , id = id)
        else:
            return redirect('note-detail' , id = id)
    
    def get(self , request , id , *args , **kwargs):
        note = Note.objects.get(id = id)
        form = NotesForm(instance = note)
        notes = Note.objects.filter(writer = request.user)
        context = {
            'form' : form,
            'buttons' : ['Update', 'Delete'],
            'notes' : notes,
            'note' : note,
        }
        return render(request , 'Notes/notes.html' , context)
        
class NoteDeleteView(View):
    
    def get(self , request , id , *args  ,**kwargs):
        note = Note.objects.get(id = id)
        note.delete()
        return redirect('notes')
    def post(self , request , *args , **kwargs):
        pass