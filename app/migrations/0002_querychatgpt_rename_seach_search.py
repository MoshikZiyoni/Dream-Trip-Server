# Generated by Django 4.1.8 on 2023-04-20 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryChatGPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=500)),
                ('answer', models.TextField(default='')),
            ],
        ),
        migrations.RenameModel(
            old_name='Seach',
            new_name='Search',
        ),
    ]