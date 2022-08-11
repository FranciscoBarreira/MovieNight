from django.contrib import admin
from .models import Movie, Category, Edition, Sub_Category
# Register your models here.

admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Edition)
