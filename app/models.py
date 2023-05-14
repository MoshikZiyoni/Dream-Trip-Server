from django.db import models

# Create your models here.

class Search(models.Model):
    input=models.TextField(max_length=200)

    
class QueryChatGPT(models.Model):
    question = models.CharField(max_length=500, default="")
    answer = models.TextField(null=False, default="")


