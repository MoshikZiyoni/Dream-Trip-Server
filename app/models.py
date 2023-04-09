from django.db import models

# Create your models here.

class Search(models.Model):
    input=models.TextField(max_length=200)

# class Country(models.Model):

# class City(models.Model):

# class Attractions(models.Model):
