from django.contrib import admin
from django.urls import path
from . import views,show_all,add_new_attractions

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
    path("user_single_trip/",views.user_single_trip,name="user_single_trip"),
    path("show-all-attractions/",show_all.show_all_attractions,name="show_all_attractions"),
    path("show-all-restaurants/",show_all.show_all_restaurants,name="show_all_restaurants"),
    path("add-new-attraction/",add_new_attractions.add_new_attraction,name="add_new_attraction"),
    path("approve_new_attraction/",add_new_attractions.approve_new_attraction,name="approve_new_attraction"),
    path("country_list/",views.country_list,name="country_list")

    
    
]