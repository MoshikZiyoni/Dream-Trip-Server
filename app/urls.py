from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path("", views.gpt_view, name= "gpt_view"),
    path('long_poll/', views.long_poll, name='long_poll'),

]