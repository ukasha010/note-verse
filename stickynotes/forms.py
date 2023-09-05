from .models import StickyNote
from django import forms

class StickyNotesForm(forms.ModelForm):

    class Meta:
        model = StickyNote
        fields = ['SNote']