from django.db import models

# Create your models here.

class Search(models.Model):
    input=models.TextField(max_length=200)

class Trip(models.Model):
    country_name=models.CharField(max_length=50)
    budget=models.CharField(max_length=50)
    travelers=models.CharField(max_length=50)
    durring=models.SmallIntegerField(null=True)
    response=models.CharField(default='',blank=False)
    
class QueryChatGPT(models.Model):
    question=models.CharField(max_length=500,default='')
    answer=models.TextField(null=False,default='')