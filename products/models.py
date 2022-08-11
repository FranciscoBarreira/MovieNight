from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Class to correct the "categorys"
    spelling in the admin site
    """

    class Meta:
        verbose_name_plural = "Categories"

    movie_category = models.CharField(max_length=150)
    movie_friendly_category = models.CharField(
        max_length=150, null=True, blank=True
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

    movie_sub_category = models.CharField(max_length=150)
    movie_friendly_sub_category = models.CharField(
        max_length=150, null=True, blank=True
        )

    def __str__(self):
        return self.movie_sub_category

    def get_friendly_name(self):
        return self.movie_friendly_sub_category