# Generated by Django 4.1.8 on 2023-10-02 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0050_alter_usertrip_liked_trips'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrip',
            name='end_trip',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertrip',
            name='start_trip',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usertrip',
            name='liked_trips',
            field=models.TextField(max_length=100),
        ),
    ]