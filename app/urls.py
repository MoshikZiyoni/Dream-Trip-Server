from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path("", views.gpt_view, name= "gpt_view"),
    path("popular/",views.popular_country,name='popular_country'),
    path("  ",views.make_short_trip,name="make_short_trip"),
]