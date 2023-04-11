from django.db import models

# Create your models here.

class Search(models.Model):
    input=models.TextField(max_length=200)

class Country(models.Model):
    country_name=models.CharField(max_length=50)

class City(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    city_name=models.CharField(max_length=50)

class Attractions(models.Model):
    city=models.ForeignKey(City,on_delete=models.CASCADE)
    attraction_name=models.CharField(max_length=50)
    price=models.SmallIntegerField(null=True)

class QueryChatGPT(models.Model):
    country_name=models.CharField(max_length=50)
    during_trip=models.SmallIntegerField()
    max_stop=models.SmallIntegerField()
    traveler=models.SmallIntegerField()
    budget=models.SmallIntegerField()