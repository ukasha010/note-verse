from django.urls import path , include
from . import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('' , views.home , name='home'),
    path('features/' , views.features , name='features'),
    path('why-us/' , views.why_us , name='why-us'),
    path('accounts/signup/' , views.signup , name='account_signup'),
    path('accounts/login/' , auth_views.LoginView.as_view(template_name="Notes/login.html") , name='account_login'),
    path('accounts/logout/' , auth_views.LogoutView.as_view() , name="account_logout"),
    path('forgot-password/' , auth_views.PasswordResetView.as_view(template_name="Notes/forgot-password.html") , name="forgot-password"),
    path('password-reset-confirm/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name="Notes/password-reset-confirm.html") , name="password_reset_confirm"),
    path('password-reset-done/' , auth_views.PasswordResetDoneView.as_view(template_name="Notes/password-reset-done.html") , name="password_reset_done"),
    path('password-reset-complete/' , auth_views.PasswordResetCompleteView.as_view(template_name="Notes/password-reset-complete.html") , name="password_reset_complete"),
    path('dashboard/' , views.dashboard , name="dashboard"),
    path('change-password/' , auth_views.PasswordChangeView.as_view() , name="change_password"),
    path('password-change-done/' , auth_views.PasswordChangeDoneView.as_view() , name="password_change_done"),
    path('account-delete-confirmation/' , views.account_delete_confirmation , name="account_delete_confirmation"),
    path('delete-account/' , views.delete_account , name="delete_account"),
    path('dashboard/todo-list/' , views.TodoListView.as_view() , name='todo-list'),
    path('dashboard/notes/' , views.NotesView.as_view() , name="notes"),
    path('dashboard/notes/<int:id>' , views.NoteDetailView.as_view() , name="note-detail"),
    path('dashboard/notes/delete/<int:id>' , views.NoteDeleteView.as_view() , name="note-delete"),
    
]
