# Generated by Django 4.1.8 on 2023-07-07 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_rename_url_attraction_social_media_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='distance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='distance',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
