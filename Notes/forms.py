from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from .models import TodoList , Note
class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']   


class TodoListForm(forms.ModelForm):
    
    class Meta:
        model = TodoList
        fields = ['title' , 'description']
        
class NotesForm(forms.ModelForm):
    
    class Meta:
        model = Note
        fields = ['title' , 'description']