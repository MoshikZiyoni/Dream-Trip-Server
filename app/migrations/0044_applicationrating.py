# Generated by Django 4.1.8 on 2023-08-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_delete_search_country_average_prices'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('user', models.TextField(max_length=100)),
            ],
        ),
    ]