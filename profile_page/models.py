from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    id_user = models.IntegerField()

    profileimg = models.ImageField(upload_to='profile_img', default='bg.png')

    bio = models.TextField(blank=True, max_length=200)

    profession = models.CharField(blank=True, max_length=20)

    def __str__(self):

        return self.user.username


