from django.contrib import admin

from .models import Post, LikePost, FollowersCount

# Register your models here.

admin.site.register(Post)

admin.site.register(LikePost)

admin.site.register(FollowersCount)
