from django.db import models


class TimePeriod(models.Model):
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
        return '{}  -  {}'.format(str(self.time_from)[:-9], str(self.time_to)[:-9])


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
        return 'mooring place id: {}'.format(self.id)
