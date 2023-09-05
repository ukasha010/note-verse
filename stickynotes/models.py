from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StickyNote(models.Model):
    SNote = models.TextField()
    Writer = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Writer} StickyNote" 