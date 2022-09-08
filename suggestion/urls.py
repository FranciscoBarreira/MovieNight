from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_suggestion_page, name='suggestion'),
]
