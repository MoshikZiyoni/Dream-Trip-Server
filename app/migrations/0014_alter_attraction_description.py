# Generated by Django 4.1.8 on 2023-07-03 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_attraction_details_attraction_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
