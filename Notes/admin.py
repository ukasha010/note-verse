from django.contrib import admin
from .models import TodoList , Note
# Register your models here.
admin.site.register(TodoList)
admin.site.register(Note)
#admin.site.register(profile)