from django.shortcuts import render
from django.contrib import messages

from .models import NewsletterSub
from .forms import NewsletterForm


def view_newsletter_page(request):
    """ A view to return the newsletter page """
    form = NewsletterForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterSub.objects.filter(email=instance.email).exists():
            messages.info(
                request,
                'Sorry, this email is already subscribed to our newsletter!'
                )
        else:
            messages.success(
                request,
                'You are now subscribed to our Newsletter!'
                )
            instance.save()

    context = {
        'form': form,
    }

    template = 'newsletter/newsletter.html'

    return render(request, template, context)