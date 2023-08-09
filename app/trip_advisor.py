
import json
import requests
from urllib.parse import quote
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os
import time
import flickrapi
load_dotenv()

def trip_advisor_attraction(city_name,country,landmarks):
    geolocator = Nominatim(user_agent="dream-trip")
    key=os.environ.get('TRIP_ADVISOR_KEY')
    print ('start trip adviosr attractions')
    url = f"https://api.content.tripadvisor.com/api/v1/location/nearby_search?"
    headers = {"accept": "application/json"}
    params = {
        'searchQuery': f"{city_name},{country}",
        'latLong': quote(f"{landmarks[0]}, {landmarks[1]}"),  # URL-encode the latLong values
        'key' : {key},
        'category': 'attractions',
        'radius': '10',
        'radiusUnit':'km',
        'language' : 'en'
    }
    response = requests.get(url, headers=headers, params=params)
    print(response)
    result = response.json()
    attractions = []
    for attraction in result['data']:
        address_string = attraction['address_obj']['address_string']
        address_obj = attraction['address_obj']
        if 'street1' in address_obj and 'city' in address_obj and 'country' in address_obj:
            street = address_obj['street1']
            city_for_attraction = address_obj['city']
            country = address_obj['country']
            address_string1 = f"{street}, {city_for_attraction}, {country}"
            location = geolocator.geocode(address_string1)
            time.sleep(0.5)
            latitude = None
            longitude = None
            if location is not None:
                latitude = location.latitude
                longitude = location.longitude
                print('Found landmarks for', latitude, longitude)

            attraction_info = {
                'location_ID' : attraction['location_id'],
                'name': attraction['name'],
                'latitude': latitude,
                'longitude': longitude,
                'address_string':address_string,
            }
            print ('attraction_info save successfuly')
            attractions.append(attraction_info) 
    return (attractions)

def trip_advisor_restaurants(city_name,country,landmarks): 
    geolocator = Nominatim(user_agent="dream-trip")
    key=os.environ.get('TRIP_ADVISOR_KEY')
    print ('start trip adviosr restaurants')

    url = "https://api.content.tripadvisor.com/api/v1/location/search?"
    headers = {"accept": "application/json"}
    params = {
        'searchQuery':f"{city_name},{country}",
        'latLong': quote(f"{landmarks[0]}, {landmarks[1]}"),  # URL-encode the latLong values
        'key': key,
        'category': 'restaurants',
        'radius': '6',
        'radiusUnit': 'km',
        'language': 'en'
    }
    response_for_restaurants = requests.get(url, headers=headers, params=params)
    print(response_for_restaurants)
    result_for_restaurants = response_for_restaurants.json()
    restaurants = []
    for restaurant in result_for_restaurants['data']:
        address_string = restaurant['address_obj']['address_string']
        address_obj = restaurant['address_obj']
        if 'street1' in address_obj and 'city' in address_obj and 'country' in address_obj:
            street = address_obj['street1']
            city_for_restaurant = address_obj['city']
            country = address_obj['country']
            address_string1 = f"{street}, {city_for_restaurant}, {country}"
            location = geolocator.geocode(address_string1)
            time.sleep(0.5)
            latitude = None
            longitude = None
            if location is not None:
                latitude = location.latitude
                longitude = location.longitude
                print('Found landmarks for', latitude, longitude)

            restaurant_info = {
                'location_ID' : restaurant['location_id'],
                'name': restaurant['name'],
                'latitude': latitude,
                'longitude': longitude,
                'address_string':address_string,
            }
            restaurants.append(restaurant_info)
    return (restaurants)
            
def flickr_api(name,latitude,longitude):
  api_key =os.environ.get('flickr_key')
  api_secret =os.environ.get('flickr_secret')
  image_list = []
  flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
  # Search for photos by tags (landmark name)
  photos = flickr.photos.search(text=name, per_page=1, extras='url_o',sort='relevance')
  if len(photos['photos']['photo']) == 0:
    # No photos found for the attraction name, search by latitude and longitude
    photos = flickr.photos.search(lat=latitude, lon=longitude, per_page=1, extras='url_o', sort='relevance')

    if len(photos['photos']['photo']) == 0:
        print('No photos found for the attraction')
  # Extract the photo URLs
  if 'photos' in photos and 'photo' in photos['photos']:
      for photo in photos['photos']['photo']:
          photo_id = photo['id']  # URL of the original-sized photo
          flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
          # Get the sizes of the photo
          sizes = flickr.photos.getSizes(photo_id=photo_id)
          # Extract the URL of the image
          if 'sizes' in sizes and 'size' in sizes['sizes']:
              # Assuming you want the URL of the largest available size
              largest_size = sizes['sizes']['size'][-1]
              image_url = largest_size['source']
              return image_url
            #   image_list.append(image_url)
          else:
              return (image_url=="")


api_key=os.environ.get('FOURSQUARE')

def foursquare_restaurant(landmarks):

    url = "https://api.foursquare.com/v3/places/search?"

    headers = {
        "accept": "application/json",
        "Authorization": api_key
    }
    query= {
        'categories':'13000',
        "ll" :  f"{landmarks[0]},{landmarks[1]}",
        'radius':5000,
        'limit' : 20,
        'fields':'distance,geocodes,name,rating,price,distance,website,photos,social_media,menu'
    }
    response = requests.get(url, params=query,headers=headers)

    response_text=(response.text)
    jsonto=json.loads(response_text)
    reslut=jsonto['results']
    return (reslut)


def foursquare_attraction(landmarks,city_name,country):
    url1 = "https://api.foursquare.com/v3/places/search?"

    headers = {
        "accept": "application/json",
        "Authorization": api_key
    }

    query1= {
        'query': f"attractions in {city_name},{country}",
        'categories':'10027,10025,10055,10068,16000',
        "ll" :  f"{landmarks[0]},{landmarks[1]}",
        'radius':8000,
        'limit' : 20,
        'fields':'distance,geocodes,name,rating,distance,website,photos,menu,hours_popular'

    }
    response1 = requests.get(url1, params=query1,headers=headers)

    response_text1=(response1.text)
    jsonto1=json.loads(response_text1)
    reslut=jsonto1['results']
    return reslut


def foursquare_hotels(landmarks):

    url = "https://api.foursquare.com/v3/places/search?"

    headers = {
        "accept": "application/json",
        "Authorization": api_key
    }
    query= {
        'categories':'19014',
        "ll" :  f"{landmarks[0]},{landmarks[1]}",
        'radius':5000,
        'limit' : 20,
        'fields':'geocodes,name,rating,website,photos,description'
    }
    response = requests.get(url, params=query,headers=headers)

    response_text=(response.text)
    jsonto=json.loads(response_text)
    reslut=jsonto['results']
    return (reslut)