from django.db import models
import django


class Photo(models.Model):
    # class used in many-to-many relations
    id = models.AutoField(
        primary_key=True,
        verbose_name='photo id'
    )

    image = models.ImageField(
        verbose_name='image',
    )


class Event(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='event id',
    )

    name = models.CharField(
        verbose_name='place name',
        max_length=250,
    )

    description = models.TextField(
        verbose_name='description of an event',
    )

    date = models.DateTimeField(
        verbose_name='time of an event',
    )

    photo = models.ImageField(
        verbose_name='image of an event',
    )

    link = models.CharField(
        verbose_name='link to an event or tickets',
        max_length=100,
    )

    def __str__(self):
        return self.name


class News(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='news id',
    )

    content = models.TextField(
        verbose_name='content of news',
    )

    date = models.DateTimeField(
        verbose_name='date published',
        default=django.utils.timezone.now
    )

    photos = models.ManyToManyField(
        Photo,
        verbose_name='photos to news',
        blank=True,
    )

    def __str__(self):
        return 'news from {}'.format(self.date)
