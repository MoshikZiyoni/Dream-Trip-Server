import json
import os
import time
from app.bs4attraction import google_search_attraction
from app.trip_advisor import foursquare_attraction, foursquare_restaurant, trip_advisor_attraction,trip_advisor_restaurants,flickr_api
from app.bs4 import google_search
import openai
from dotenv import load_dotenv
import requests
from app.models import Attraction, Country, QueryChatGPT,City, Restaurant
from urllib.parse import quote
from geopy.geocoders import Nominatim
import threading
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from app.wikipediaapi import process_query
import traceback

# Load environment variables from .env file
load_dotenv()
geolocator = Nominatim(user_agent="dream-trip")
api_key=os.environ.get('FOURSQUARE')
import threading


def process_city(city_data, country,country_id):
    city_name = city_data['city']
    description = city_data['description']
    location = geolocator.geocode(f"{city_name},{country}")
    landmarks = [location.latitude, location.longitude]
    existing_city = City.objects.filter(city=city_name).first()

    print("City:", city_name, landmarks)
    if not existing_city:
        
        city_query = City(country_id=country_id, city=city_name, latitude=landmarks[0], longitude=landmarks[1], description=description)
        city_query.save()
        print('save successfully for city')
    city_data['latitude'] = landmarks[0]
    city_data['longitude'] = landmarks[1]
    city_to_save = City.objects.filter(city=city_name)
    city_objs = city_to_save.all()
    if city_objs:
        city_obj = city_objs[0]
    print(city_obj,'city_obj')
    reslut = foursquare_restaurant(landmarks)
    restaurants = []
    if len(reslut) == 0:
        print('start trip advisor resturant')
        restaurant_ = trip_advisor_restaurants(city_name, country, landmarks)
        restaurants.append(restaurant_)
    else:
        print('start the else line 49')

        for restaur in reslut:
            name = restaur['name'] if 'name' in restaur else ""
            distance = restaur['distance'] if 'distance' in restaur else ""
            latitude = restaur['geocodes']['main']['latitude'] if 'geocodes' in restaur and 'main' in restaur['geocodes'] and 'latitude' in restaur['geocodes']['main'] else ""
            longitude = restaur['geocodes']['main']['longitude'] if 'geocodes' in restaur and 'main' in restaur['geocodes'] and 'longitude' in restaur['geocodes']['main'] else ""
            rating = restaur['rating'] if 'rating' in restaur else "0"
            price = restaur['price'] if 'price' in restaur else ""
            website = restaur['website'] if 'website' in restaur else ""
            social_media = restaur['social_media'] if 'social_media' in restaur else ""
            menu = restaur['menu'] if 'menu' in restaur else ""
            hours_popular = restaur['hours_popular'] if 'hours_popular' in restaur else ""
            flickr_photos1 = flickr_api(name, latitude, longitude)
            restaurant_info = {
                'name': name,
                'latitude': latitude,
                'longitude': longitude,
                'photos': flickr_photos1,
                'review_score': rating,
                'price':price,
                'website':website,
                'social_media':social_media,
                'menu':menu,
                'hours_popular':hours_popular
            }
            restaurants.append(restaurant_info)
            resta_query = Restaurant(
            name=name,
            city=city_obj,
            latitude=latitude,
            longitude=longitude,
            photos=flickr_photos1,
            review_score=rating)
            resta_query.save()
            print ('save resturants successfuly')

    
    print ('start attracion') 
    reslut1 = foursquare_attraction(landmarks,city_name,country)
    attractions = []
    if len(reslut1) == 0:
        print('start trip advisor atta')
        attractions_info_trip = trip_advisor_attraction(city_name, country, landmarks)
        attractions.append(attractions_info_trip)
        print ('tripadvisor line 93')
    else:
        print('start the else line 94')
        for attrac in reslut1:
            name1 = attrac['name'] if 'name' in attrac else ""
            distance1 = attrac['distance'] if 'distance' in attrac else ""
            latitude1 = attrac['geocodes']['main']['latitude'] if 'geocodes' in attrac and 'main' in attrac['geocodes'] and 'latitude' in attrac['geocodes']['main'] else ""
            longitude1 = attrac['geocodes']['main']['longitude'] if 'geocodes' in attrac and 'main' in attrac['geocodes'] and 'longitude' in attrac['geocodes']['main'] else ""
            rating1 = attrac['rating'] if 'rating' in attrac else "0"
            price1 = attrac['price'] if 'price' in attrac else ""
            website1 = attrac['website'] if 'website' in attrac else ""
            social_media1 = attrac['social_media'] if 'social_media' in attrac else ""
            menu1 = attrac['menu'] if 'menu' in attrac else ""
            hours_popular1 = attrac['hours_popular'] if 'hours_popular' in attrac else ""
            description = attrac['description'] if 'description' in attrac else ""

            flickr_photos = flickr_api(name1, latitude1, longitude1)

            attraction_info = {
            'name': name,
                'latitude': latitude1,
                'longitude': longitude1,
                'photos': flickr_photos,
                'review_score': rating1,
                'price':price1,
                'website':website1,
                'social_media':social_media1,
                'menu':menu1,
                'hours_popular':hours_popular1,
                'description':description
            }

            attractions.append(attraction_info)
            atrc_query = Attraction(
            name=name1,
            city=city_obj,
            latitude=latitude1,
            longitude=longitude1,
            photos=flickr_photos,
            review_score=rating1,
            description=description,
            url=website1
            )
            atrc_query.save()
            print ('save attraction successfuly')

    print(attractions)  

    attractions = city_data['attractions'] = attractions
    restaurants = city_data['restaurants'] = restaurants
    return attractions, restaurants


def run_long_poll_async(ourmessage, retries=3, delay=1):
    
    print('Start GPT')
    try:
        api_key = os.environ.get('OPENAI_API_KEY')
        openai.api_key = api_key
    except:
        print('Key not found or invalid')

    for attempt in range(retries):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": ourmessage}
                ]
            )
            answer1 = completion.choices[0].message.content
            print (answer1)
            for attempt_data in range(retries):
                try:
                    data = json.loads(answer1)
                    # # Extract all city names
                    country = data['country']
                    try:
                        existing_country = Country.objects.filter(name=country).first()
                        country_id=existing_country.id
                    except:
                        print ('not existing_country')
                    if not existing_country:
                        query_for_country=Country(name=country)
                        query_for_country.save()
                        country_id = query_for_country.id
                    # print (country_id)
                    executor = ThreadPoolExecutor()
                    for city_data  in data['cities']:
                        city_name = city_data ['city']
                        existing_city = City.objects.filter(city=city_name).first()
                        if existing_city:
                            # Add attractions and restaurants to city_data dictionary
                            attract=Attraction.objects.filter(city_id=existing_city.id).values()
                            attractions_list = list(attract)
                            city_data['attractions'] = attractions_list
                            restaura=Restaurant.objects.filter(city_id=existing_city.id).values()
                            restaurants_list = list(restaura)
                            city_data['restaurants']=restaurants_list
                            print ('continue')
                            continue
                        executor.submit(process_city, city_data, country, country_id).result()

                    # Shutdown the executor and wait for all threads to complete
                    executor.shutdown()
                    combined_data =json.dumps(data, indent=2)
                    query = QueryChatGPT(question=ourmessage, answer=combined_data)
                    query.save()
                    return combined_data
                except Exception as e:
                    print ('failed in the end line 205')
                    traceback.print_exc()

                    print(f'Error occurred: {e}')
                    print(f'Retrying... (attempt {attempt_data + 1})')
                    time.sleep(delay)

        except openai.error.APIError as e:
            if e.status_code == 429:
                # If we hit the API rate limit, wait for a bit before trying again
                time.sleep(1)
            else:
                # If there's another API error, raise an exception
                raise
        except Exception as e:
            print ('fialed in the end line 218')
            print(f'Error occurred: {e}')
            print(f'Retrying... (attempt {attempt + 1})')
            time.sleep(delay)

    # If all retries fail, return a default error message
    return "I'm sorry, an error occurred while generating the response. Please try again later."