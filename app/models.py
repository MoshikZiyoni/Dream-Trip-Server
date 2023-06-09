from django.db import models

# Create your models here.

class Search(models.Model):
    input=models.TextField(max_length=200)

    
class QueryChatGPT(models.Model):
    question = models.CharField(max_length=500, default="")
    answer = models.TextField(null=False, default="")
    itinerary_description=models.TextField(null=False,default="")

class Country(models.Model):
    name=models.CharField(max_length=100)

class City(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    city=models.CharField(max_length=100)
    latitude=models.FloatField(null=False)
    longitude=models.FloatField(null=False)
    description = models.CharField(max_length=1000)
    

class Attraction(models.Model):
    city = models.ForeignKey(City, related_name='attractions', on_delete=models.CASCADE)
    name = models.TextField(max_length=500)
    latitude=models.FloatField(null=False)
    longitude=models.FloatField(null=False)
    photos=models.TextField(max_length=100)
    review_score=models.TextField(max_length=20)
    description=models.TextField(max_length=1000)
    website=models.TextField(max_length=100)
    hours_popular=models.TextField()
    distance=models.IntegerField(null=False)
    real_price=models.CharField(max_length=200)
    
class Restaurant(models.Model):
    city = models.ForeignKey(City, related_name='restaurants', on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    latitude=models.FloatField(null=False)
    longitude=models.FloatField(null=False)
    photos=models.TextField(max_length=100)
    review_score=models.TextField(max_length=20)
    website=models.TextField(max_length=100)
    social_media=models.TextField(max_length=100)
    price=models.TextField(max_length=20)
    menu=models.TextField(max_length=100)
    distance=models.IntegerField(null=False)
