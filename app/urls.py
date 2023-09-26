from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path("", views.gpt_view, name= "gpt_view"),
    path("popular/",views.popular_country,name='popular_country'),
    path("search/",views.make_short_trip,name="make_short_trip"),
    path("rating/",views.out_applaction_score,name="out_applaction_score"),
    path("checkrate/",views.check_before_rate,name="check_before_rate"),
    path("user_add_trip/",views.user_add_trip,name="user_add_trip"),
    path("user_trip/",views.user_trip,name="user_trip"),
    path("user_delete_trip/",views.user_delete_trip,name="user_delete_trip"),
]