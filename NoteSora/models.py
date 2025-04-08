from django.db import models
from UserSora.models import User

class Note(models.Model):
    titleNote = models.CharField(max_length=100, verbose_name='Title Note')
    contentNote = models.TextField(max_length=500, verbose_name='Content Note')
    createdNote = models.DateTimeField(auto_now_add=True, verbose_name='Date Note')
    isFavorite = models.BooleanField(default=False, verbose_name='Favorite Note')
    author = models.ForeignKey(User, on_delete = models.CASCADE)    