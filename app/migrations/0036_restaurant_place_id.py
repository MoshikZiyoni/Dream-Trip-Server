# Generated by Django 4.1.8 on 2023-08-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_attraction_place_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='place_id',
            field=models.TextField(max_length=150, null=True),
        ),
    ]
