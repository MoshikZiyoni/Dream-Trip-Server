# Generated by Django 4.1.8 on 2023-05-09 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_querychatgpt_rename_seach_search'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('request_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EmailRequestCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField(auto_now_add=True)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
    ]
