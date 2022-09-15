from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages

from .models import MakeSuggestion
from .forms import SuggestionForm

# Create your views here.


def view_suggestion_page(request):
    """ A view to return the make a suggestion page """

    form = SuggestionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        cleaned_form = form.cleaned_data['email']

        cleaned_form.save()

    context = {
        'form': form,
    }

    return render(request, 'suggestion/suggestion.html', context)
