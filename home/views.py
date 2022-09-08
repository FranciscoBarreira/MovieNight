from django.shortcuts import render
from products.models import Movie

# Create your views here.


def index(request):
    """ Returns the index page """

    top_products = Movie.objects.all().order_by(
        '-rating',)

    latest_products = Movie.objects.all().order_by(
        '-created_on',)

    context = {
        'top_products': top_products,
        'latest_products': latest_products,
    }

    return render(request, 'home/index.html', context)
