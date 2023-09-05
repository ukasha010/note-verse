from django.db import models
from django.contrib.auth.models import User
#from django.core.validators import MinLengthValidator
#from .validator import validate_first_name_starts_with_letter , validate_last_name_starts_with_letter
# Create your models here.

"""class Profile(models.Model):


    def __str__(self):
        return None"""
        
class TodoList(models.Model):
    Writer = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=10 , default="Incomplete")
    
    def __str__(self):
        return self.title
    
class Note(models.Model):
    writer = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    
"""class profile(models.Model):
    first_name = models.CharField(validators=[MinLengthValidator(limit_value=2) , validate_first_name_starts_with_letter] , max_length=25)
    last_name = models.CharField(validators=[MinLengthValidator(limit_value=1) , validate_last_name_starts_with_letter] , max_length=35)
    email = models.EmailField(max_length=40)
    password = models.CharField(validators=[MinLengthValidator(limit_value=8),] , max_length=20)
    image_url = models.URLField(null=True , blank=True)
    age = models.IntegerField(default=18)"""
    
    
    
    