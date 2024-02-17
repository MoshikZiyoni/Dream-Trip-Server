import ast
import json
import os
import random
from django.db.models import Q
import time
import traceback
from unidecode import unidecode
from app.google_place import get_attraction_from_google, get_hotels_from_google, get_restaurants_google
from app.trip_advisor import (
    foursquare_attraction,
    foursquare_hotels,
    foursquare_night_life,
    foursquare_restaurant,
    my_night_life,
    sunset_api,
)
import openai
from dotenv import load_dotenv
from app.models import  Country, QueryChatGPT, City
from geopy.geocoders import Nominatim
from concurrent.futures import ThreadPoolExecutor
from app.utils import clean_json_data, fetch_hotels_and_update, fetch_nightlife_and_update, fetch_sunset_and_update, generate_schedule, hotel_from_google, process_attraction, process_hotel, process_night_life_foursquare, process_restaurant, restarunts_from_google, sort_attractions_by_distance
from threading import Thread
from threading import RLock
from django.core.cache import cache
import concurrent.futures

attrac_lock = RLock()
restaur_lock = RLock() 
city_lock=RLock()
hotel_lock=RLock()
night_life_lock=RLock()
lock = RLock()
generate_schedule_lock=RLock()
new_city_lock= RLock()
executor = ThreadPoolExecutor(max_workers=20)

# Load environment variables from .env file
load_dotenv()
geolocator = Nominatim(user_agent="dream-trip")
api_key = os.environ.get("FOURSQUARE")

main_restaurants = []
main_attractions = []
main_hotels = []
main_night_life = []


def process_attractions_thread(landmarks, city_name, country, city_obj):
    # with lock:
    try:
        return process_attractions(landmarks, city_name, country, city_obj)
    except Exception as e:
        print('error in process_attractions_thread:', e)


def process_restaurants_thread(landmarks, city_name, city_obj):
    # with lock:
    try:
        return process_restaurants(landmarks, city_name, city_obj)
    except Exception as e:
        print('error in process_restaurants_thread:', e)


def process_hotels_thread(landmarks, city_name):
    # with lock:
    try:
        return process_hotels(landmarks, city_name)
    except Exception as e:
        print('error in process_hotels_thread:', e)


def process_night_life_thread(landmarks):
    # with lock:
    try:
        return process_night_life(landmarks)
    except Exception as e:
        print('error in process_night_life_thread:', e)


def process_sunset_thread(landmarks):
    # with lock:
    try:
        return process_sunset(landmarks)
    except Exception as e:
        print('error in process_sunset_thread:', e)
            

def process_city(city_data, country, existing_country):
   with new_city_lock:
        print ('start process city,!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        city_name = city_data["city"]
        description = city_data["description"]
        print("City:", city_name)
        check2=''
        try:
            city_obj = City.objects.get(city=city_name)
            if city_obj:
                 check2=True
        except:
             pass
        location = geolocator.geocode(f"{city_name},{country}")
        landmarks = [location.latitude, location.longitude]
        print('landmarks for process_city',city_name,' : ',landmarks)
        try:
            if check2!=True:
                print('start to save city')
                # time.sleep(1)
                city_query = City(
                country=existing_country,
                city=city_name,
                latitude=float(landmarks[0]),
                longitude=float(landmarks[1]),
                description=description,
                )
                city_query.save()
                print("Save successfully for city")
        except Exception as e:
            print('not able to save line 78',e)

        try:
            # time.sleep(0.6)
            city_data['landmarks']=[float(landmarks[0]),float(landmarks[1])]
            # city_data["latitude"] = float(landmarks[0])
            # city_data["longitude"] = float(landmarks[1])
            city_obj = City.objects.get(city=city_name)
            print(city_obj, "city_obj")
        except Exception as e:
            print (e,'@@@@@@@@@@@@@@@@@@@@@@@@@@','line 86 chat.py')


        try:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                # Submit the threads to the executor
                attraction_thread = executor.submit(process_attractions_thread, landmarks, city_name, country, city_obj)
                restaurant_thread = executor.submit(process_restaurants_thread, landmarks, city_name, city_obj)
                hotels_thread = executor.submit(process_hotels_thread, landmarks, city_name)
                night_life_thread = executor.submit(process_night_life_thread, landmarks)
                sunset_thread = executor.submit(process_sunset_thread, landmarks)

                # Get the results from the submitted threads
                attractions_result = attraction_thread.result()
                restaurants_result = restaurant_thread.result()
                hotels_result = hotels_thread.result()
                night_life_result = night_life_thread.result()
                sunset_result = sunset_thread.result()
            
            # print('attractions_result: ',attractions_result,'@@@@@@@')
            # Store the results in the city_data dictionary
            city_data["attractions"] = attractions_result
            city_data["restaurants"] = restaurants_result
            city_data["hotels"] = hotels_result
            city_data["night_life"] = night_life_result
            city_data["sunset"] = sunset_result
        
        except Exception as e:
            print('error in process_city:', e)
        return city_data

def process_restaurants(landmarks, city_name, city_obj):
    restaurants = []
    print ("start restaurants")
    with restaur_lock:
        reslut = foursquare_restaurant(landmarks)
        # print(reslut)
        if len(reslut) == 0:
            print("Start google restaurant")
            my_restaurant=get_restaurants_google(city=city_name,lat=landmarks[0],lon=landmarks[1])
            threads = []
            for restaur in my_restaurant['results']:
                thread = Thread(target=restarunts_from_google, args=(restaur, city_obj, restaurants))
                thread.start()
                threads.append(thread)
        else:
            threads = []
            for restaur in reslut:
                thread = Thread(target=process_restaurant, args=(restaur, city_obj, restaurants))
                thread.start()
                threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()
    print('return restaurants')
    return restaurants

def process_attractions(landmarks, city_name, country, city_obj):
    attractions = []
    print ("start attractions")
    with attrac_lock:
        result1 = foursquare_attraction(landmarks, city_name, country)
        threads = []

        if len(result1) == 0:
            print("Start google attraction")
            attractions_info_trip = get_attraction_from_google(city=city_name,city_obj=city_obj,lat=landmarks[0],lon=landmarks[1],attractions=attractions)
            for attracs in attractions_info_trip['results']:
                thread = Thread(target=restarunts_from_google, args=(attracs, city_obj, attractions))
                thread.start()
                threads.append(thread)
        else:
            print("Start the else line 94")

            for attrac in result1:
                thread = Thread(target=process_attraction, args=(attrac, city_obj, attractions))
                thread.start()
                threads.append(thread)

        # Wait for all threads to complete
        for thread in threads:
            thread.join()

    print ('return attractions')
    return attractions


def process_hotels(landmarks, city_name):
    print ("start hotels")
    cache_key = f"hotels_{city_name.replace(' ', '_').replace('-', '_')}"
    # Attempt to retrieve data from the cache
    hotels1 = cache.get(cache_key)
    if hotels1 is None:
        hotels = []
        # with lock:
        result_for_hotel=foursquare_hotels(landmarks)
        
        if len(result_for_hotel) == 0:
            print("Start google hotels")
            hotels_info_trip = get_hotels_from_google(city=city_name,lat=landmarks[0],lon=landmarks[1])
            for hotel in hotels_info_trip['results']:
                thread = Thread(target=hotel_from_google, args=(hotel, hotels))
                thread.start()
                threads.append(thread)
        threads = []
        for hotel in result_for_hotel:
            thread = Thread(target=process_hotel, args=(hotel, hotels))
            thread.start()
            threads.append(thread)

        for thread in threads:
                thread.join()
        cache.set(cache_key, hotels, timeout=7 * 24 * 60 * 60)
        print ('return hotels')
        return hotels
    else:
        return hotels1
        

def process_night_life(landmarks):
    night_lifes = []
    result_for_night_life=my_night_life(landmarks)
    print (result_for_night_life,'@@@@@@')
    if ( result_for_night_life=={'night_life': ''}):
        result_for_night_life=foursquare_night_life(landmarks)
        threads = []
        for night_life in result_for_night_life:
            thread = Thread(target=process_night_life_foursquare, args=(night_life, night_lifes))
            thread.start()
            threads.append(thread)

        for thread in threads:
                thread.join()
        return night_lifes
    print ('return night-life')

    return result_for_night_life


    
def process_sunset(landmarks):
    # with lock:
    result_for_sunset=sunset_api(landmarks)
    print ('return sunsets')
    return result_for_sunset


def run_long_poll_async(ourmessage, mainland,durring, retries=3, delay=1):
    print("Start GPT")
    try:
        api_key = os.environ.get("OPENAI_API_KEY")
        openai.api_key = api_key
    except:
        print("Key not found or invalid")

    for attempt in range(retries):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": ourmessage}],
            )
            answer1 = completion.choices[0].message.content
            print(answer1)
            for attempt_data in range(retries):
                try:
                    try:
                        answer1=answer1.remove('```')
                    except:
                        pass
                    try:
                        data = json.loads(answer1)
                        data1 = json.loads(answer1)
                    except:
                        print('not valid json')
                        cleaned_data = clean_json_data(cleaned_data)
                        data=ast.literal_eval(cleaned_data)
                        # print(data)
                        data1=ast.literal_eval(answer1)
                    country = data["country"]
                    if country != mainland:
                        print("Country is not mainland. Retrying...")
                        break
                    
                    try:
                        itinerary_description=data['itinerary-description']
                    except:
                        pass
                    try:
                        itinerary_description=data['itinerary_description']
                    except:
                        pass
                    try:
                        existing_country = Country.objects.get(name=country)
                        country_id = existing_country.id
                        existing_country.increase_popularity()
                    except Country.DoesNotExist:
                        print("Country does not exist")
                        existing_country = Country(name=country)
                        existing_country.save()
                        country_id = existing_country.id
                    threads = []
                    
                    # executor = ThreadPoolExecutor()
                    for city_data in data["cities"]:
                        city_name = city_data["city"]
                        normalized_city_name = unidecode(city_name)
                        with city_lock:

                            try:
                                existing_city = City.objects.prefetch_related('attractions', 'restaurants').filter(city__iexact=normalized_city_name).first()
                                print ('This is the City name of the existing city',normalized_city_name)
                            except City.DoesNotExist:
                                print ('no regular')
                                try:
                                    existing_city = City.objects.filter(Q(city__iexact=normalized_city_name) | Q(city__icontains=normalized_city_name)).first()
                                except:
                                    pass
                            try:
                                if existing_city:
                                    print ('start existing_city')
                                    cache_key = f"existing_city_{existing_city.city}"
                                    existing_city_cache = cache.get(cache_key)
                                    if existing_city_cache is None:
                                        # Use prefetch_related to fetch related attractions and restaurants efficiently
                                        try:
                                            attractions_list = existing_city.attractions.all().values()
                                            restaurants_list = existing_city.restaurants.all().values()
                                        except:
                                            print('There isno attracionts yet for this existing city')
                                            check_for_attraction=True

                                        if check_for_attraction==True:
                                            landmarks=[existing_city.latitude,existing_city.longitude]
                                            attractions_list=process_attractions(landmarks, city_name, country,existing_city)
                                            restaurants_list=process_restaurants(landmarks, city_name, existing_city)
                                        # Sort attractions by distance, shuffle remaining attractions, and set them in city_data
                                        try:
                                            attractions = sort_attractions_by_distance(attractions=attractions_list, first_attraction=attractions_list[0])
                                            first_5_attractions = attractions[:5]
                                            remaining_attractions = attractions[5:]
                                            random.shuffle(remaining_attractions)
                                            final_attractions = first_5_attractions + remaining_attractions
                                        except:
                                            final_attractions=attractions_list
                                        city_data["attractions"] = list(final_attractions)
                                        city_data["restaurants"] = list(restaurants_list)
                                        city_data['landmarks']=[existing_city.latitude,existing_city.longitude]

                                    
                                        sunset_thread = Thread(target=fetch_sunset_and_update, args=(city_data, [existing_city.latitude, existing_city.longitude],))
                                        hotels_thread = Thread(target=fetch_hotels_and_update, args=(city_data, [existing_city.latitude, existing_city.longitude], existing_city.city,))
                                        nightlife_thread = Thread(target=fetch_nightlife_and_update, args=(city_data, [existing_city.latitude, existing_city.longitude],))

                                        threads.extend([sunset_thread, hotels_thread, nightlife_thread])
                                        print("Continue")
                                        cache.set(cache_key, existing_city_cache, timeout=7 * 24 * 60 * 60)
                                    else:
                                        return existing_city_cache
                                else:
                                    if existing_city==None:
                                        print('no exsiting city')
                                        # process_city(city_data,country,existing_country)
                                        executor.submit(process_city, city_data, country,existing_country)
                                        print ("start exceutor")
                            except:
                                print ('last expet 309')
                                pass
                        
                            check=False
                                
                    executor.shutdown()
                    # Start the threads
                    for thread in threads:
                        thread.start()

                    # Wait for all threads to finish
                    for thread in threads:
                        thread.join()
                    
                    with generate_schedule_lock:
                        combined_data=generate_schedule(data,country,check)
                    
                    query = QueryChatGPT(question=ourmessage, answer=data1,itinerary_description=itinerary_description)
                    query.save()
                    total_prices=combined_data['total_attraction_prices']
                    
                    total_food_prices=int(existing_country.average_food)*int(durring)
                    total_transportation=int(existing_country.average_transportation)*int(durring)
                    total_hotels=int(existing_country.average_hotels)*int(durring)
                    avrage_daily_spent=existing_country.average_prices
                    if avrage_daily_spent=='':
                        avrage_daily_spent=0
                    costs={
                        "total_attraction_prices":total_prices,
                        "total_transport_private_taxi":total_transportation,
                        "total_food_prices":total_food_prices,
                        "total_hotels":total_hotels,
                        "avrage_daily_spent":avrage_daily_spent,
                    }
                    trip_id=QueryChatGPT.objects.get(question=ourmessage)
                    trip_id=trip_id.id
                    print(trip_id,'@@@@@@@@@@@@@')
                    end_result=combined_data["schedule"]
                    return {'answer':end_result,'itinerary_description':itinerary_description,'main_restaurants':main_restaurants,'main_attractions':main_attractions,"costs":costs,"trip_id":trip_id}
                except Exception as e:
                    print("Error occurred:", e,traceback.print_exc())
                    print(f"Retrying... (attempt {attempt_data + 1})")
                    time.sleep(delay)

        except openai.error.APIError as e:
            try:
                if e.status_code == 429:
                    time.sleep(1)
                else:
                    raise
            except Exception as e:
                print("Error occurred:", e,)
        except Exception as e:
            print("Error occurred:", e)
            print(f"Retrying... (attempt {attempt + 1})")
            time.sleep(delay)

    return "I'm sorry, an error occurred while generating the response. Please try again later."




