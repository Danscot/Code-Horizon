from django.urls import path
from . import views

urlpatterns = [

    # Add more URL patterns for other pages

    path('', views.home, name='home'),

    path('like-post', views.like_post, name='like-post'),

    path('profile/<str:pk>', views.profile, name='profile'),

    path('follow', views.follow, name='follow'),

    path('search', views.search, name='search'),


]