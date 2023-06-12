
import requests
from urllib.parse import quote
from geopy.geocoders import Nominatim
from dotenv import load_dotenv
import os
import time
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
        'radius': '10',
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
  import flickrapi
  api_key =os.environ.get('flickr_key')
  api_secret =os.environ.get('flickr_secret')
  image_list = []
  flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
  # Search for photos by tags (landmark name)
  photos = flickr.photos.search(text=name, per_page=1, extras='url_o',sort='relevance')
  if len(photos['photos']['photo']) == 0:
    print (0)
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
              print('No image URL available for the photo')
#   return(image_list)