from django import forms

from . import models

class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogPost
        fields = [
            'title',
            'description'
        ]
