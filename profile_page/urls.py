from django.urls import path
from . import views

urlpatterns = [

    # Add more URL patterns for other pages

    path('user_page', views.user_page, name='user_page'),


]