from django.db import models

# Create your models here.
class ApplicationRating(models.Model):
    rating = models.PositiveSmallIntegerField(default=0)
    user_email = models.TextField(max_length=100)
    user_name=models.TextField(max_length=100)
    user_picture=models.TextField(max_length=100,null=True)
    review=models.TextField(max_length=100,null=True)
    
class QueryChatGPT(models.Model):
    question = models.CharField(max_length=500, default="")
    answer = models.TextField(null=False, default="")
    itinerary_description=models.TextField(null=False,default="")

class Country(models.Model):
    name=models.CharField(max_length=100)
    average_prices=models.TextField(max_length=200)
    popularity_score = models.IntegerField(default=0)

    def increase_popularity(self):
        self.popularity_score += 1
        self.save()



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
    distance=models.TextField(max_length=200)
    real_price=models.TextField(max_length=200)
    hours=models.TextField(max_length=150,null=True)
    tel=models.TextField(max_length=100,null=True)
    address=models.TextField(max_length=100,null=True)
    place_id=models.TextField(max_length=150,null=True)
    tips=models.TextField(max_length=3000,null=True)
    
class Restaurant(models.Model):
    city = models.ForeignKey(City, related_name='restaurants', on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    latitude=models.FloatField(null=False)
    longitude=models.FloatField(null=False)
    photos=models.TextField(max_length=100)
    review_score=models.TextField(max_length=20)
    website=models.TextField(max_length=100)
    category=models.TextField(max_length=100)
    price=models.TextField(max_length=20)
    tips=models.TextField(max_length=3000)
    hours=models.TextField(max_length=150,null=True)
    tel=models.TextField(max_length=100,null=True)
    address=models.TextField(max_length=100,null=True)
    place_id=models.TextField(max_length=150,null=True)

class Hotels_foursqaure(models.Model):
    city = models.ForeignKey(City, related_name='hotels', on_delete=models.CASCADE)
    name = models.TextField(max_length=500)
    latitude=models.FloatField(null=False)
    longitude=models.FloatField(null=False)
    photos=models.TextField(max_length=100)
    review_score=models.TextField(max_length=20)
    description=models.TextField(max_length=1000)
    website=models.TextField(max_length=100)
    place_id=models.TextField(max_length=200,null=True)

class Popular(models.Model):
    country=models.TextField(max_length=100)
    image=models.TextField(max_length=255)
    