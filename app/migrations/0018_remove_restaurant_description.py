# Generated by Django 4.1.8 on 2023-07-07 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_attraction_distance_restaurant_distance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='description',
        ),
    ]