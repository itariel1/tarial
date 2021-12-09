from django import forms

from . import models

class BookForms(forms.ModelForm):
    class Meta:
        model = models.Books
        fields = [
            'title',
            'description'
        ]
