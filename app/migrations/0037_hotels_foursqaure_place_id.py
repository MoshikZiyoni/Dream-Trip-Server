# Generated by Django 4.1.8 on 2023-08-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_restaurant_place_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels_foursqaure',
            name='place_id',
            field=models.TextField(max_length=200, null=True),
        ),
    ]