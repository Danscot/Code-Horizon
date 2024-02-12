from django.urls import path
from . import views

urlpatterns = [

    # Add more URL patterns for other pages

    path('signin', views.signin, name='sign'),

    path('login', views.log_in, name='login'),


]