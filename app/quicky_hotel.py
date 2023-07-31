#  cities=City.objects.all()
#     for city in cities:
#       landmarks=[city.latitude,city.longitude]
#       result=foursquare_hotels(landmarks)
#       hotels= []
#       for hotel in result:
#         process_hotel(hotel=hotel, city_obj=city, hotels=hotels)    
#     return 'ok'