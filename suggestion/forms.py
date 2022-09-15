from django import forms
from .models import MakeSuggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = MakeSuggestion
        fields = ['email', 'subject', 'message']
