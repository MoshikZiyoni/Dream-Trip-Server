# Generated by Django 4.1.8 on 2023-10-10 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0058_alter_applicationrating_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='average_prices',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
