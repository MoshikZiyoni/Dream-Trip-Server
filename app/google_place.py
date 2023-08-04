from dotenv import load_dotenv
import requests
import os
# from app.trip_advisor import flickr_api
load_dotenv()

city_list=[{"city": "Cali", "city_obj": 714, "lat": 3.437222, "lon": -76.5225}]

API_KEY=os.environ.get('google_key')
# def get_attraction_by_city(city,city_obj,lat,lon):
#     base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
#     params = {
#         "query": f"best attraction in {city}",
#         'location':f"{lat},{lon}",
#         "key": API_KEY,
#         "types": "tourist_attraction",
#         "sort": "rating", 
#         "min_rating": 4,
#         "radius":10000,
#         "orderby": "rating",
#         "fields": "photos,formatted_address,name,rating,opening_hours", 
#         "language":"en",
#     }
#     response = requests.get(base_url, params=params)
#     data = response.json()
#     places = []
#     for result in data['results']:
#         name = result['name']
#         latt = result['geometry']['location']['lat']
#         lng = result['geometry']['location']['lng']
#         rating = result['rating']
#         if rating==0:
#             continue
#         place_id = result['place_id']
#         photo_reference = result['photos'][0]['photo_reference'] if result.get('photos') else None
#         html_attributions = result['photos'][0]['html_attributions'] if result.get('photos') else None

#         image = flickr_api(name=name,latitude=lat,longitude=lng)
#         city_obj=City.objects.filter(id=city_obj).first()
#         atrc_query = Attraction(
#             name=name,
#             city=city_obj,
#             latitude=latt,
#             longitude=lng,
#             photos=image,
#             review_score=rating,
#             place_id=place_id,
#             # website=website1,
#             # hours_popular=hours_popular1,
#             # distance=distance1
#         )
#         atrc_query.save()
#         print(f"Save attraction successfully{name}")
#     #     place = {
#     #         'name': name,
#     #         'latitude': lat,
#     #         'longitude': lng,
#     #         'review_score': rating,
#     #         'place_id': place_id,
#     #         'photo': image,
#     #         'html_attributions': html_attributions,
#     #     }
#     #     places.append(place)
        
#     # return places

# for city_info in city_list:
#     city = city_info['city'] 
#     city_obj = city_info['city_obj']
#     lat=city_info['lat']
#     lon=city_info['lon']
#     get_places_by_city(city,city_obj,lat,lon)

# for place in places:
#     print(place['name'], place['rating'])
    
# # Get photo URL
# if place.get('photo_reference'):
#     photo_url = f"https://maps.googleapis.com/maps/api/place/photo?photoreference={place['photo_reference']}&key={API_KEY}"






def get_restaurants_google(city,city_obj,lat,lon):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"best attraction in {city}",
        'location':f"{lat},{lon}",
        "key": API_KEY,
        "types": "restaurant",
        "sort": "rating", 
        "min_rating": 4,
        "radius":10000,
        "orderby": "rating",
        "fields": "photos,formatted_address,name,rating,opening_hours", 
        "language":"en",
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    print (data)
    places = []
    for result in data['results']:
        name = result['name']
        latt = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        rating = result['rating']
        if rating==0:
            continue
        place_id = result['place_id']
        photo_reference = result['photos'][0]['photo_reference'] if result.get('photos') else None
        html_attributions = result['photos'][0]['html_attributions'] if result.get('photos') else None

        # image = flickr_api(name=name,latitude=lat,longitude=lng)
        # # city_obj=City.objects.filter(id=city_obj).first()
        # # atrc_query = Attraction(
        # #     name=name,
        # #     city=city_obj,
        # #     latitude=latt,
        # #     longitude=lng,
        # #     photos=image,
        # #     review_score=rating,
        # #     place_id=place_id,
        # #     # website=website1,
        # #     # hours_popular=hours_popular1,
        # #     # distance=distance1
        # # )
        # # atrc_query.save()
        # # print(f"Save restaurant successfully{name}")
    #     place = {
    #         'name': name,
    #         'latitude': lat,
    #         'longitude': lng,
    #         'review_score': rating,
    #         'place_id': place_id,
    #         'photo': image,
    #         'html_attributions': html_attributions,
    #     }
    #     places.append(place)
        
    # return places

for city_info in city_list:
    city = city_info['city'] 
    city_obj = city_info['city_obj']
    lat=city_info['lat']
    lon=city_info['lon']
    get_restaurants_google(city,city_obj,lat,lon)