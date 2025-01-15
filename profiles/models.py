from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Favourite(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='favourite')
    game = models.ForeignKey(
        'Game', on_delete=models.PROTECT, blank=True, null=True)
    platform = models.ForeignKey(
        'Platform', on_delete=models.PROTECT, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.game.game


class Library(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='library')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    game = models.ManyToManyField('Game')
    platform = models.ManyToManyField('Platform')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Privacy(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='privacy')
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Game(models.Model):
    game = models.CharField(max_length=50)

    def __str__(self):
        return self.game


class Platform(models.Model):
    platform = models.CharField(max_length=50)

    def __str__(self):
        return self.platform
