# Generated by Django 2.1 on 2018-11-09 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20181110_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dates',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='content.TimePeriod', verbose_name='dates the event takes place on'),
        ),
    ]