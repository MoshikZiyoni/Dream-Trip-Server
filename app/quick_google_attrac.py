# def get_places_by_city(city,city_obj,lat,lon):
#         base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
#         params = {
#             "query": f"best attraction in {city}",
#             'location':f"{lat},{lon}",
#             "key": API_KEY,
#             "types": "tourist_attraction",
#             "sort": "rating", 
#             "min_rating": 4,
#             "radius":10000,
#             "orderby": "rating",
#             "fields": "photos,formatted_address,name,rating,opening_hours", 
#             "language":"en",
#         }
#         response = requests.get(base_url, params=params)
#         data = response.json()
#         places = []
#         for result in data['results']:
#             name = result['name']
#             latt = result['geometry']['location']['lat']
#             lng = result['geometry']['location']['lng']
#             rating = result['rating']
#             if rating==0:
#                 continue
#             place_id = result['place_id']
#             photo_reference = result['photos'][0]['photo_reference'] if result.get('photos') else None
#             html_attributions = result['photos'][0]['html_attributions'] if result.get('photos') else None

#             image = flickr_api(name=name,latitude=lat,longitude=lng)
#             city_obj1=City.objects.filter(id=city_obj).first()
#             atrc_query = Attraction(
#                 name=name,
#                 city=city_obj1,
#                 latitude=latt,
#                 longitude=lng,
#                 photos=image,
#                 review_score=rating,
#                 place_id=place_id,
#                 # website=website1,
#                 # hours_popular=hours_popular1,
#                 # distance=distance1
#             )
#             atrc_query.save()
#             print(f"Save attraction successfully{name}")
#         #     place = {
#         #         'name': name,
#         #         'latitude': lat,
#         #         'longitude': lng,
#         #         'review_score': rating,
#         #         'place_id': place_id,
#         #         'photo': image,
#         #         'html_attributions': html_attributions,
#         #     }
#         #     places.append(place)
            
#         # return places

#     for city_info in city_list:
#         city = city_info['city'] 
#         city_obj = city_info['city_obj']
#         lat=city_info['lat']
#         lon=city_info['lon']
#         get_places_by_city(city,city_obj,lat,lon)
#     return 'kkkkkk'