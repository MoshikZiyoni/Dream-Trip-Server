# Generated by Django 4.1.8 on 2023-10-02 17:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0051_usertrip_end_trip_usertrip_start_trip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrip',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
