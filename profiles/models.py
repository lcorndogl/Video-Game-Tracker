from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Favourites(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='favourites')
    platform = models.CharField(max_length=50)
    game = models.CharField(max_length=50)
    
    def __str__(self):
        return self.game

class Library(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='library')