from django.core import validators
from django import forms
from .models import Task

class Taskrecord(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
                    }