from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Class to correct the "categorys"
    spelling in the admin site
    """

    class Meta:
        verbose_name_plural = "Categories"

    movie_category = models.CharField(max_length=254)
    movie_friendly_category = models.CharField(
        max_length=254, null=True, blank=True
        )

    def __str__(self):
        return self.movie_category

    def get_friendly_name(self):
        return self.movie_friendly_category

class Sub_Category(models.Model):
    """
    Class to correct the 'categorys'
    spelling in the admin site
    """

    class Meta:
        verbose_name_plural = "Sub_Categories"

    movie_sub_category = models.CharField(max_length=254)
    movie_friendly_sub_category = models.CharField(
        max_length=254, null=True, blank=True
        )

    def __str__(self):
        return self.movie_sub_category

    def get_friendly_name(self):
        return self.movie_friendly_sub_category

class Edition(models.Model):
    movie_edition = models.CharField(max_length=254)
    movie_friendly_edition = models.CharField(
        max_length=254, null=True, blank=True
        )

    def __str__(self):
        return self.movie_edition

    def get_friendly_name(self):
        return self.movie_friendly_edition        

class Movie(models.Model):
    movie_category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )
    movie_sub_category = models.ForeignKey(
        'Sub_Category', null=True, blank=True, on_delete=models.SET_NULL
        )
    movie_edition1 = models.ForeignKey(
        'Edition',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='edition1'
        )
    movie_edition2 = models.ForeignKey(
        'Edition',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='edition2'
        )
    movie_edition3 = models.ForeignKey(
        'Edition',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='edition3'
        )
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    director = models.CharField(max_length=254)
    synopsis = models.TextField()
    price_dvd = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    price_bluray = models.DecimalField(
        max_digits=6, decimal_places=2
        )
    price_4k = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
        )
    cover_url = models.URLField(max_length=1024, null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)