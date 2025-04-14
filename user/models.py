from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True, default='default_profile.pic.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('user:profile', kwargs={'username': self.username})

    def get_update_url(self):
        return reverse('user:update', kwargs={'username': self.username})

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        ordering = ['username']

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
