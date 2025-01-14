from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Favourites(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='favourites')
    platform = models.CharField(max_length=50)
    game = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.game

class Library(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='library')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    game = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
class Privacy(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='privacy')
    private = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username