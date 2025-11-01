from django.db import models
from actors.models import Actor
from genres.models import Genre


class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name='movies')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies')
