# Generated by Django 4.1.8 on 2023-10-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0059_alter_country_average_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='average_prices',
            field=models.CharField(default=0, max_length=200, null=True),
        ),
    ]
