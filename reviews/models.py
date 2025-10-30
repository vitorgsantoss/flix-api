from django.db import models
from actors.models import Actor
from django.core.validators import MaxValueValidator, MinValueValidator



MESSAGE = 'Informe um valor entre 0 e 5!'

class Review(models.Model):
    actor = models.ForeignKey(Actor, related_name='reviews', on_delete=models.CASCADE)
    stars = models.IntegerField(
        validators= [
            MinValueValidator(limit_value=0, message=MESSAGE),
            MaxValueValidator(limit_value=5, message=MESSAGE)
        ]
    )
