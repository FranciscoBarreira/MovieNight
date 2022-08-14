from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Movie, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Movie.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        

        if 'movie_category' in request.GET:
            categories = request.GET['movie_category'].split(',')
            products = products.filter(movie_category__movie_category__in=categories)
            categories = Category.objects.filter(movie_category__in=categories)

    
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search term")
                return redirect(reverse('products'))
            
            queries = Q(title__icontains=query) | Q(synopsis__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Movie, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)    