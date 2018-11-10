from django.db import models


class Place(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='place id',
    )

    name = models.CharField(
        verbose_name='place name',
        max_length=50,
    )

    description = models.TextField(
        verbose_name='description of a place',
    )

    category = models.CharField(
        verbose_name='category of a place',
        max_length=20,
    )

    def __str__(self):
        return self.name
