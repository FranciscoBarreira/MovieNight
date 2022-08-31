from django.shortcuts import render

# Create your views here.


def view_suggestion_page(request):
    """ A view to return the about us page """

    return render(request, 'suggestion/suggestion.html')