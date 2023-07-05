# Generated by Django 4.1.8 on 2023-06-14 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_city_restaurants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='attractions',
        ),
        migrations.RemoveField(
            model_name='city',
            name='restaurants',
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.JSONField()),
                ('details', models.JSONField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurants', to='app.city')),
            ],
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.JSONField()),
                ('details', models.JSONField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attractions', to='app.city')),
            ],
        ),
    ]