from django.db import models
import django


class TimePeriod(models.Model):
    # class used in many-to-many relations of events
    id = models.AutoField(
        primary_key=True,
        verbose_name='time period id'
    )

    time_from = models.DateTimeField(
        verbose_name='time the event takes place from'
    )

    time_to = models.DateTimeField(
        verbose_name='time the event finishes'
    )

    def __str__(self):
        return '{}  -  {}'.format(str(self.time_from)[:-15], str(self.time_to)[:-15])


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

    dates = models.ForeignKey(
        TimePeriod,
        verbose_name='dates the event takes place on',
        on_delete=models.CASCADE,
        null=True,
    )
    photo = models.ImageField(
        verbose_name='image of an event',
    )

    link = models.CharField(
        verbose_name='link to an event or tickets',
        max_length=100,
        blank=True,
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
