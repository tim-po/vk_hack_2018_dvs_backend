from django.db import models
import django.utils.timezone


class Photo:
    # class used in many-to-many relations
    id = models.AutoField(
        primary_key=True,
        verbose_name='photo id'
    )

    image = models.ImageField(
        verbose_name='image',
        on_delete=models.CASCADE,
    )


class TimePeriod:
    # class used in many-to-many relations of a mooring place
    id = models.AutoField(
        primary_key=True,
        verbose_name='time period id'
    )

    time_from = models.DateTimeField(
        verbose_name='time from the place is busy'
    )

    time_to = models.DateTimeField(
        verbose_name='time when the place will be released'
    )

    def __str__(self):
        return '{}  -  {}'.format(self.time_from, self.time_to)


class Place(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='place id',
    )

    name = models.CharField(
        verbose_name='place name',
        max_length=250,
    )

    description = models.CharField(
        verbose_name='description of a place',
        max_length=1000,
    )

    category = models.CharField(
        verbose_name='category of a place',
        max_length=20,
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='event id',
    )

    name = models.CharField(
        verbose_name='place name',
        max_length=250,
    )

    description = models.CharField(
        verbose_name='description of an event',
        max_length=2000,
    )

    date = models.DateTimeField(
        verbose_name='time of an event',
    )

    photo = models.ImageField(
        verbose_name='image of an event',
        on_delete=models.CASCADE,
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

    content = models.CharField(
        verbose_name='content of news',
        max_length=1000,
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


class MooringPlace(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='mooring place id',
    )

    time_table = models.ManyToManyField(
        TimePeriod,
        verbose_name='time table for a mooring place'
    )

    def __str__(self):
        return 'mooring place (id: {})'.format(self.id)
