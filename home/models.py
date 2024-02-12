from django.db import models

import uuid

from datetime import datetime

# Create your models here.


class Post(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    user = models.CharField(max_length=100)

    image = models.ImageField(upload_to='post_images', default=None)

    caption = models.TextField()

    created_at = models.DateTimeField(default=datetime.now)

    no_of_likes = models.IntegerField(default=0)

    def __str__(self):

        return self.user


class LikePost(models.Model):

    post_id = models.CharField(max_length=100)

    username = models.CharField(max_length=100)

    def __str__(self):

        return self.username


class FollowersCount(models.Model):

    follower = models.CharField(max_length=100)

    user = models.CharField(max_length=100)

    def __str__(self):

        return self.user

