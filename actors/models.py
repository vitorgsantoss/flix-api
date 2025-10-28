from django.db import models


NATIONALITY = (
    ('USA', 'UNITED STATES'),
    ('BR', 'BRAZIL'),
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=10, choices=NATIONALITY)

    def __str__(self):
        return self.name

