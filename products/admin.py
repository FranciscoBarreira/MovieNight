from django.contrib import admin
from .models import Movie, Category, Edition, Sub_Category
# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'director',
        'title',
        'movie_category',
        'movie_sub_category',
        'movie_edition1',
        'movie_edition2',
        'movie_edition3',
        'cover',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'movie_category',
        'movie_friendly_category',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'movie_sub_category',
        'movie_friendly_sub_category',
    )


class EditionAdmin(admin.ModelAdmin):
    list_display = (
        'movie_edition',
        'movie_friendly_edition',
    )


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Sub_Category, SubCategoryAdmin)
admin.site.register(Edition, EditionAdmin)
