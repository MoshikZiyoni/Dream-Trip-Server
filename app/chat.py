import json
import os
import time
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

def process_restaurant(name, city_name, country, latitude, longitude, city_to_save, restaurants):
    flickr_photos1 = flickr_api(name, latitude, longitude)
    goog_result1 = google_search(f"{name},{city_name},{country}")

    restaurant_info = {
        'name': name,
        'latitude': latitude,
        'longitude': longitude,
        'photos': flickr_photos1,
        'review_score': goog_result1['review_score'],
    }
    restaurants.append(restaurant_info)

    try:
        city_objs = city_to_save.all()
        if city_objs:
            city_obj = city_objs[0]
            
            resta_query = Restaurant(name=name, city=city_obj, details=restaurant_info)
            resta_query.save()
        else:
            print(f"No city found for {city_name}")
    except Exception as e:
        print ('error in 44')
        print(f"Error occurred: {e}")

def process_attraction(name_attrac, city_name, country, latitude, longitude, city_to_save, attractions):
    flickr_photos = flickr_api(name_attrac, latitude, longitude)
    goog_result = None
    wikisearch = None

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(google_search, f"{name_attrac},{city_name},{country}")
        future2 = executor.submit(process_query, name_attrac)
        goog_result = future1.result()
        wikisearch = future2.result()
        

    attraction_info = {
        'name': name_attrac,
        'latitude': latitude,
        'longitude': longitude,
        'photos': flickr_photos,
        'review_score': goog_result['review_score'],
        'description': wikisearch[0],
        'url': wikisearch[1],
    }

    attractions.append(attraction_info)
    if len(goog_result['review_score'])<0:
        goog_result['review_score']='0'
    try:
        city_objs = city_to_save.all()
        if city_objs:
            city_obj = city_objs[0]
            review_score = goog_result.get('review_score', '0')
            if wikisearch:
                description = wikisearch[0]
                url = wikisearch[1] if len(wikisearch) >= 2 else ""
            else:
                description = ""
                url = ""

            atrc_query = Attraction(
                name=name_attrac,
                city=city_obj,
                latitude=latitude,
                longitude=longitude,
                photos=flickr_photos,
                review_score=review_score,
                description=description,
                url=url
            )
            atrc_query.save()
            attractions.append(attraction_info)

        else:
            print(f"No city found for {city_name}")
    except Exception as e:
        print('Error occurred:', e)
        traceback.print_exc()


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
    city_to_save = City.objects.filter(city=city_name)

    reslut = foursquare_restaurant(landmarks)
    restaurants = []
    if len(reslut) == 0:
        restaurant_ = trip_advisor_restaurants(city_name, country, landmarks)
        restaurants.append(restaurant_)
    else:
        threads = []
        for i in reslut:
            name = i['name']
            latitude = i['geocodes']['main']['latitude']
            longitude = i['geocodes']['main']['longitude']

            thread = threading.Thread(target=process_restaurant, args=(name, city_name, country, latitude, longitude, city_to_save, restaurants))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    reslut1 = foursquare_attraction(landmarks,city_name,country)
    attractions = []
    if len(reslut1) == 0:
        attractions_info_trip = trip_advisor_attraction(city_name, country, landmarks)
        attractions.append(attractions_info_trip)
        print ('tripadvisor line 122')
    else:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            threads = []
            for i in reslut1:
                name_attrac = i['name']
                latitude = i['geocodes']['main']['latitude']
                longitude = i['geocodes']['main']['longitude']

                thread = executor.submit(
                    process_attraction,
                    name_attrac,
                    city_name,
                    country,
                    latitude,
                    longitude,
                    city_to_save,
                    attractions
                )
                threads.append(thread)

            # Wait for all threads to complete
            concurrent.futures.wait(threads)

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
                        executor.submit(process_city, city_data, country,country_id)

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