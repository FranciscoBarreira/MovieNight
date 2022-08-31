from django.contrib import admin
from .models import NewsletterSub


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')


admin.site.register(NewsletterSub, NewsletterAdmin)