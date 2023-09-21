from dotenv import load_dotenv
import requests
import os
# from app.trip_advisor import flickr_api

load_dotenv()

API_KEY=os.environ.get('google_key')
def get_attraction_from_google(city,lat,lon):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        "query": f"best attraction in {city}",
        'location':f"{lat},{lon}",
        "key": API_KEY,
        "types": "tourist_attraction",
        "sort": "rating", 
        "min_rating": 4,
        "radius":10000,
        "orderby": "rating",
        "fields": "photos,formatted_address,name,rating,opening_hours", 
        "language":"en",
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data
    
    


def get_restaurants_google(city,lat,lon):
    print ('GOOGLEEEEE')
    try:
        base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
        params = {
            "query": f"best restaurant in {city}",
            'location':f"{lat},{lon}",
            "key": API_KEY,
            "types": "restaurant",
            "sort": "rating", 
            "min_rating": 4,
            "radius":10000,
            "orderby": "rating",
            "fields": "photos,formatted_address,name,rating,price_level", 
            "language":"en",
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        return data
    except Exception as e:
        print ('not goodddddddddddddddddddddd',e)



def get_hotels_from_google(city,lat,lon):
    base_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    city='Tel aviv'
    lat=32.0853
    lon=34.7818
    params = {
        "query": f"best hotels in {city}",
        'location':f"{lat},{lon}",
        "key": API_KEY,
        "types": "lodging",
        "sort": "rating", 
        "min_rating": 4,
        "radius":10000,
        "orderby": "rating",
        "fields": "photos,formatted_address,name,rating,opening_hours", 
        "language":"en",
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data