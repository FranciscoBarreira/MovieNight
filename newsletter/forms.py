from django import forms
from .models import NewsletterSub


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSub
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')

            return email