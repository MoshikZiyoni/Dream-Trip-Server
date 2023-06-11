# url = f"https://api.content.tripadvisor.com/api/v1/location/nearby_search?"
#                         headers = {"accept": "application/json"}
#                         params = {
#                             'latLong': quote(f"{landmarks[0]}, {landmarks[1]}"),  # URL-encode the latLong values
#                             'key' : {key},
#                             # 'searchQuery': city_name+country,
#                             'category': 'attractions',
#                             'radius': '10',
#                             'radiusUnit':'km',
#                             'language' : 'en'
#                         }
#                         response = requests.get(url, headers=headers, params=params)
#                         print(response)
#                         result = response.json()
#                         attractions = []
#                         for attraction in result['data']:
#                             address_string = attraction['address_obj']['address_string']
#                             address_obj = attraction['address_obj']
#                             if 'street1' in address_obj and 'city' in address_obj and 'country' in address_obj:
#                                 street = address_obj['street1']
#                                 city_for_attraction = address_obj['city']
#                                 country = address_obj['country']
#                                 address_string1 = f"{street}, {city_for_attraction}, {country}"
#                                 location = geolocator.geocode(address_string1)
#                                 time.sleep(0.5)
#                                 latitude = None
#                                 longitude = None
#                                 if location is not None:
#                                     latitude = location.latitude
#                                     longitude = location.longitude
#                                     print('Found landmarks for', latitude, longitude)

#                                 attraction_info = {
#                                     'location_ID' : attraction['location_id'],
#                                     'name': attraction['name'],
#                                     'latitude': latitude,
#                                     'longitude': longitude,
#                                     'address_string':address_string,
#                                 }
#                                 attractions.append(attraction_info) 
#                         url = "https://api.content.tripadvisor.com/api/v1/location/nearby_search?"
#                         headers = {"accept": "application/json"}
#                         params = {
#                             'latLong': quote(f"{landmarks[0]}, {landmarks[1]}"),  # URL-encode the latLong values
#                             'key': key,
#                             'category': 'restaurants',
#                             'radius': '10',
#                             'radiusUnit': 'km',
#                             'language': 'en'
#                         }
#                         response_for_restaurants = requests.get(url, headers=headers, params=params)
#                         print(response_for_restaurants)
#                         result_for_restaurants = response_for_restaurants.json()
#                         restaurants = []
#                         for restaurant in result_for_restaurants['data']:
#                             address_string = restaurant['address_obj']['address_string']
#                             address_obj = restaurant['address_obj']
#                             if 'street1' in address_obj and 'city' in address_obj and 'country' in address_obj:
#                                 street = address_obj['street1']
#                                 city_for_restaurant = address_obj['city']
#                                 country = address_obj['country']
#                                 address_string1 = f"{street}, {city_for_restaurant}, {country}"
#                                 location = geolocator.geocode(address_string1)
#                                 time.sleep(0.5)
#                                 latitude = None
#                                 longitude = None
#                                 if location is not None:
#                                     latitude = location.latitude
#                                     longitude = location.longitude
#                                     print('Found landmarks for', latitude, longitude)

#                                 restaurant_info = {
#                                     'location_ID' : restaurant['location_id'],
#                                     'name': restaurant['name'],
#                                     'latitude': latitude,
#                                     'longitude': longitude,
#                                     'address_string':address_string,
#                                 }
#                                 restaurants.append(restaurant_info)