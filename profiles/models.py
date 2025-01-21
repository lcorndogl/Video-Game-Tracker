from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Privacy(models.Model):
    privacy = models.CharField(max_length=50)

    def __str__(self):
        return self.privacy


class Game(models.Model):
    game = models.CharField(max_length=50)

    def __str__(self):
        return self.game


class Platform(models.Model):
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.platform


class User_Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='User_Profile')
    game = models.ForeignKey(
        'Game', on_delete=models.PROTECT, blank=True, null=True)
    platform = models.ForeignKey(
        'Platform', on_delete=models.PROTECT, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    privacy = models.ForeignKey('Privacy', on_delete=models.PROTECT,
                                related_name='User_Privacy')

    def __str__(self):
        return self.user.username


class User_Library(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='library')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    game = models.ForeignKey(Game, on_delete=models.PROTECT)
    platform = models.ManyToManyField('Platform')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
