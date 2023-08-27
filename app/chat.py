import json
import os
import random
from django.db.models import Q
import time
from unidecode import unidecode
from app.google_place import get_attraction_from_google, get_hotels_from_google, get_restaurants_google
from app.trip_advisor import (
    foursquare_attraction,
    foursquare_hotels,
    foursquare_restaurant,
    trip_advisor_attraction,
    trip_advisor_restaurants,
)
import openai
from dotenv import load_dotenv
from app.models import Attraction, Country, Hotels_foursqaure, QueryChatGPT, City, Restaurant
from geopy.geocoders import Nominatim
from concurrent.futures import ThreadPoolExecutor
from app.utils import generate_schedule, hotel_from_google, process_attraction, process_hotel, process_restaurant, restarunts_from_google, restaurant_GPT, save_to_db, sort_attractions_by_distance
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from threading import RLock

attrac_lock = RLock()
restaur_lock = RLock() 
city_lock=RLock()
hotel_lock=RLock()
executor = ThreadPoolExecutor(max_workers=20)

# Load environment variables from .env file
load_dotenv()
geolocator = Nominatim(user_agent="dream-trip")
api_key = os.environ.get("FOURSQUARE")
import threading

main_restaurants = []
main_attractions = []
main_hotels = []
def process_city(city_data, country, country_id):
    city_name = city_data["city"]
    description = city_data["description"]
    location = geolocator.geocode(f"{city_name},{country}")
    landmarks = [location.latitude, location.longitude]
    existing_city = City.objects.filter(city=city_name).first()

    print("City:", city_name, landmarks)
    if not existing_city:
        city_query = City(
            country_id=country_id,
            city=city_name,
            latitude=landmarks[0],
            longitude=landmarks[1],
            description=description,
        )
        city_query.save()
        print("Save successfully for city")
    city_data["latitude"] = landmarks[0]
    city_data["longitude"] = landmarks[1]
    city_to_save = City.objects.filter(city=city_name)
    city_objs = city_to_save.all()
    if city_objs:
        city_obj = city_objs[0]
    print(city_obj, "city_obj")

    
    attraction_for_data=(process_attractions(landmarks, city_name, country, city_obj, city_data))
    restaurant_for_data=(process_restaurants(landmarks, city_name, country, city_obj, city_data))
    hotels_for_data=(process_hotels(landmarks, city_name, country, city_obj, city_data))

    main_attractions.extend(attraction_for_data)
    main_restaurants.extend(restaurant_for_data)
    main_hotels.extend(hotels_for_data)
    
    try:
        save_to_db(attraction_for_data,restaurant_for_data,hotels_for_data)

    except:
        print ('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    city_data["attractions"] = attraction_for_data
    city_data["restaurants"] = restaurant_for_data
    city_data["hotels"] = hotels_for_data
    return city_data


# restaur_lock=Lock()
def process_restaurants(landmarks, city_name, country, city_obj, city_data):
    restaurants = []

    with restaur_lock:
        reslut = foursquare_restaurant(landmarks)
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

def process_attractions(landmarks, city_name, country, city_obj, city_data):
    attractions = []
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


def process_hotels(landmarks, city_name, country, city_obj, city_data):
    hotels = []
    with hotel_lock:
        result_for_hotel=foursquare_hotels(landmarks)
        

        if len(result_for_hotel) == 0:
            print("Start google hotels")
            hotels_info_trip = get_hotels_from_google(city=city_name,lat=landmarks[0],lon=landmarks[1])
            for hotel in hotels_info_trip['results']:
                thread = Thread(target=hotel_from_google, args=(hotel, city_obj, hotels))
                thread.start()
                threads.append(thread)
        threads = []
        for hotel in result_for_hotel:
            thread = Thread(target=process_hotel, args=(hotel, city_obj, hotels))
            thread.start()
            threads.append(thread)

        for thread in threads:
                thread.join()

        print ('return hotels')
        return hotels




def run_long_poll_async(ourmessage, mainland, retries=3, delay=1):
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
                    data = json.loads(answer1)
                    data1 = json.loads(answer1)
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
                        existing_country = Country.objects.filter(name=country).first()
                        country_id = existing_country.id
                        existing_country.increase_popularity()
                    except:
                        print("Country does not exist")
                    if not existing_country:
                        query_for_country = Country(name=country)
                        query_for_country.save()
                        country_id = query_for_country.id

                    executor = ThreadPoolExecutor()
                    for city_data in data["cities"]:
                        with city_lock:
                            city_name = city_data["city"]
                            normalized_city_name = unidecode(city_name)
                            try:
                                existing_city = City.objects.filter(city=city_name).first()
                            except:
                                print ('no regular')
                                existing_city = City.objects.filter(Q(city__iexact=normalized_city_name) | Q(city__icontains=normalized_city_name)).first()
                            
                            # existing_city = City.objects.filter(Q(city__iexact=city_name) | Q(city__icontains=city_name)).first()
                            if existing_city:
                                attract = Attraction.objects.filter(city_id=existing_city.id).values()
                                attractions_list = list(attract)
                                attractions = sort_attractions_by_distance(attractions=attractions_list, first_attraction=attractions_list[0])
                                first_5_attractions = attractions[:5]
                                remaining_attractions = attractions[5:]
                                # Shuffle the remaining attractions randomly
                                random.shuffle(remaining_attractions)
                                check=True
                                final_attractions = first_5_attractions + remaining_attractions
                                city_data["attractions"] = final_attractions
                                restaura = Restaurant.objects.filter(city_id=existing_city.id).values()
                                restaurants_list = list(restaura)
                                city_data["restaurants"] = restaurants_list
                                hotels=Hotels_foursqaure.objects.filter(city_id=existing_city.id).values()
                                hotels_list=list(hotels)
                                city_data["hotels"] = hotels_list
                                print("Continue")
                                continue
                            executor.submit(process_city, city_data, country, country_id)
                            check=False
                    executor.shutdown()   
                    combined_data=generate_schedule(data,country,check)
                    query = QueryChatGPT(question=ourmessage, answer=data1,itinerary_description=itinerary_description)
                    query.save()
                    total_prices=combined_data['total_prices']
                    total_transport_private_taxi=combined_data["total_transport_private_taxi"]
                    total_food_prices=combined_data['total_food_prices']
                    costs={
                        "total_prices":total_prices,
                        "total_transport_private_taxi":total_transport_private_taxi,
                        "total_food_prices":total_food_prices,
                    }
                    end_result=combined_data["schedule"]
                    return {'answer':end_result,'itinerary_description':itinerary_description,'main_restaurants':main_restaurants,'main_attractions':main_attractions,"costs":costs}
                except Exception as e:
                    print("Error occurred:", e)
                    print(f"Retrying... (attempt {attempt_data + 1})")
                    time.sleep(delay)

        except openai.error.APIError as e:
            try:
                if e.status_code == 429:
                    time.sleep(1)
                else:
                    raise
            except Exception as e:
                print("Error occurred:", e)
        except Exception as e:
            print("Error occurred:", e)
            print(f"Retrying... (attempt {attempt + 1})")
            time.sleep(delay)

    return "I'm sorry, an error occurred while generating the response. Please try again later."




