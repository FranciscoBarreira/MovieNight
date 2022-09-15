from django import forms
from .models import MakeSuggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = MakeSuggestion
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        return email