# Generated by Django 4.1.8 on 2023-07-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_attraction_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='distance',
            field=models.TextField(max_length=200),
        ),
    ]