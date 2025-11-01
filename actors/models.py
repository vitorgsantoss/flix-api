from django.db import models


NATIONALITY = (
    ('USA', 'UNITED STATES'),
    ('BR', 'BRAZIL'),
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=10, choices=NATIONALITY)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
