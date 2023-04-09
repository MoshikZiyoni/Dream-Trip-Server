from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'app'

urlpatterns = [
    path("", views.gpt_func, name= "gpt_func"),
]