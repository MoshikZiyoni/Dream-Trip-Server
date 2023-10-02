# Generated by Django 4.1.8 on 2023-10-01 14:47

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_remove_users_trip_from_query_chat_gpt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='liked_trips',
        ),
        migrations.CreateModel(
            name='UserTrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_trips', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.users')),
            ],
        ),
    ]
