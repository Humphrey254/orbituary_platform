from django import forms
from .models import Obituary

class ObituaryForm(forms.ModelForm):
    class Meta:
        model = Obituary
        fields = ['title', 'content', 'author_name', 'contact_email', 'image']
