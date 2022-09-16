from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages

from .models import MakeSuggestion
from .forms import SuggestionForm

# Create your views here.


def view_suggestion_page(request):
    """ A view to return the make a suggestion page """

    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent Successfully!')
            return redirect(reverse('suggestion', ))
    else:
        form = SuggestionForm()

    context = {
        'form': form,
    }

    return render(request, 'suggestion/suggestion.html', context)
