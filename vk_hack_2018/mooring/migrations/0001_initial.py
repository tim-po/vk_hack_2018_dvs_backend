# Generated by Django 2.1.1 on 2018-11-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MooringPlace',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='mooring place id')),
            ],
        ),
        migrations.CreateModel(
            name='TimePeriod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='time period id')),
                ('time_from', models.DateTimeField(verbose_name='time from the place is busy')),
                ('time_to', models.DateTimeField(verbose_name='time when the place will be released')),
            ],
        ),
        migrations.AddField(
            model_name='mooringplace',
            name='time_table',
            field=models.ManyToManyField(to='mooring.TimePeriod', verbose_name='time table for a mooring place'),
        ),
    ]
