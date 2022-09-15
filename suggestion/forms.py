from django import forms
from .models import MakeSuggestion


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = MakeSuggestion
        fields = ['email']

    def clean(self):
        # email = self.cleaned_data.get('email')
        email = super().clean()

        return email