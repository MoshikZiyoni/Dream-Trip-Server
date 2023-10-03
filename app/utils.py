from concurrent.futures import ThreadPoolExecutor
import os
import random
import re
from django.db.models import Q
import openai
import requests
from app.models import Attraction, City, Restaurant,Country
from app.teleport_api import get_cities_by_country
from app.trip_advisor import flickr_api,my_night_life, sunset_api
from app.wikipediaapi import process_query
import json
from datetime import datetime, timedelta
import math
import traceback
from dotenv import load_dotenv
from app.currency_data import calculate_total_price_attractions
import ast
from unidecode import unidecode
from threading import Thread,RLock

shared_resource_lock = RLock()

load_dotenv()

def process_attraction(attrac, city_obj, attractions):
    name1 = attrac.get("name", "")
    distance1 = attrac.get("distance", "")
    latitude1 = (
        attrac["geocodes"]["main"]["latitude"]
        if "geocodes" in attrac
        and "main" in attrac["geocodes"]
        and "latitude" in attrac["geocodes"]["main"]
        else ""
    )
    longitude1 = (
        attrac["geocodes"]["main"]["longitude"]
        if "geocodes" in attrac
        and "main" in attrac["geocodes"]
        and "longitude" in attrac["geocodes"]["main"]
        else ""
    )
    rating1 = attrac.get("rating", "0")
    website1 = attrac.get("website", "")
    hours_popular1 = attrac.get("hours_popular", "")
    hours=attrac.get('hours', {}).get('display', "")
    address=attrac.get('location', {}).get('formatted_address', "")
    tel=attrac.get('tel', "")
    description = attrac.get("description", "")
    distance1=attrac.get("distance","")
    tips = []
    result_tips = attrac.get("tips", [])  # Get the list of tips from the current result
    for j, tip in enumerate(result_tips):
        if j >= 3:
            break
        tip_text = tip.get("text", "")  # Get the text from the tip dictionary
        tips.append(tip_text)
    if len(description)==0:
            try:
                wiki=process_query(name1)
                description=wiki[0]
                print ('descrption from wiki')
            except:
                 print ('descrption from wiki not gooodddddddddddddddd')
    photos1 = attrac.get("photos", "")
    if photos1:
        first_photo = photos1[0]
        prefix = first_photo.get("prefix", "")
        suffix = first_photo.get("suffix", "")
        url1 = f"{prefix}original{suffix}"
        photos1=url1
        
    else:
        try:
            photos1 = flickr_api(name=name1, latitude=latitude1, longitude=longitude1)
        except:
            print ("flickr api can't bring an image")

    attraction_info = {
        "name": name1,
        "latitude": latitude1,
        "longitude": longitude1,
        "photos": photos1,
        "review_score": rating1,
        "website": website1,
        "hours_popular": hours_popular1,
        "hours":hours,
        "address":address,
        "tel":tel,
        'tips':tips,
        "description": description,
        "distance":distance1,
        'city_obj':city_obj.id
    }

    attractions.append(attraction_info)
    # atrc_query = Attraction(
    #     name=name1,
    #     city=city_obj,
    #     latitude=latitude1,
    #     longitude=longitude1,
    #     photos=photos1,
    #     review_score=rating1,
    #     description=description,
    #     website=website1,
    #     hours_popular=hours_popular1,
    #     distance=distance1
    # )
    # atrc_query.save()
    # print("Save attraction successfully")


def process_restaurant(restaur, city_obj, restaurants):
    name = restaur.get("name", "")
    distance = restaur.get("distance", "")
    try:
        latitude = (
            restaur["geocodes"]["main"]["latitude"]
            if "geocodes" in restaur
            and "main" in restaur["geocodes"]
            and "latitude" in restaur["geocodes"]["main"]
            else ""
        )
        longitude = (
            restaur["geocodes"]["main"]["longitude"]
            if "geocodes" in restaur
            and "main" in restaur["geocodes"]
            and "longitude" in restaur["geocodes"]["main"]
            else ""
        )
    except:
        print ('no geocodes')
    try:
        latitude = restaur["latitude"]
        longitude = restaur["longitude"]  
    except:
        pass  
    rating = restaur.get("rating", "0")
    price = restaur.get("price", "")
    website = restaur.get("website", "")
    social_media = restaur.get("social_media", "")
    try:
        instagram_handle = social_media.get("instagram", "")
        social_media = instagram_handle
    except:
        social_media = ""
        print ('no insta')
    menu = restaur.get("menu", "")
    distance=restaur.get("distance","")
    hours_for_resta = restaur.get('hours', {}).get('display', "")
    address_resta = restaur.get('location', {}).get('formatted_address', "")
    tel_for_resta = restaur.get('tel', "")
    photos = restaur.get("photos", "")
    if photos:
        first_photo = photos[0]
        prefix = first_photo.get("prefix", "")
        suffix = first_photo.get("suffix", "")
        url = f"{prefix}original{suffix}"
        photos=url
    else:
        try:
            photos = flickr_api(name, latitude, longitude)
        except:
            print ("flickr api can't bring an image")
    restaurant_info = {
        "name": name,
        "latitude": latitude,
        "longitude": longitude,
        "photos": photos,
        "review_score": rating,
        "price": price,
        "website": website,
        "hours":hours_for_resta,
        "tel":tel_for_resta,
        "address":address_resta,
        "social_media": social_media,
        "menu": menu,
        "distance":distance,
        'city_obj':city_obj.id

    }
    restaurants.append(restaurant_info)
    # resta_query = Restaurant(
    #     name=name,
    #     city=city_obj,
    #     latitude=latitude,
    #     longitude=longitude,
    #     photos=photos,
    #     review_score=rating,
    #     menu=menu,
    #     social_media=social_media,
    #     website=website,
    #     price=price,
    #     distance=distance
    # )
    # resta_query.save()
    # print("Save restaurants successfully")




def process_hotel(hotel, hotels):
    name12 = hotel.get("name", "")
    latitude12 = (
        hotel["geocodes"]["main"]["latitude"]
        if "geocodes" in hotel
        and "main" in hotel["geocodes"]
        and "latitude" in hotel["geocodes"]["main"]
        else ""
    )
    longitude12 = (
        hotel["geocodes"]["main"]["longitude"]
        if "geocodes" in hotel
        and "main" in hotel["geocodes"]
        and "longitude" in hotel["geocodes"]["main"]
        else ""
    )
    rating12 = hotel.get("rating", "0")
    website12 = hotel.get("website", "")
    description1 = hotel.get("description", "")
    hours=hotel.get('hours', {}).get('display', "")
    address=hotel.get('location', {}).get('formatted_address', "")
    tel=hotel.get('tel', "")
    tips = []
    result_tips = hotel.get("tips", [])  # Get the list of tips from the current result
    for j, tip in enumerate(result_tips):
        if j >= 3:
            break
        tip_text = tip.get("text", "")  # Get the text from the tip dictionary
        tips.append(tip_text)
    # if len(description1)==0:
    #         try:
    #             wiki=process_query(name12)
    #             description1=wiki[0]
    #             print ('descrption from wiki')
    #         except:
    #              print ('descrption from wiki not gooodddddddddddddddd')
    photos12 = hotel.get("photos", "")
    if photos12:
        first_photo = photos12[0]
        prefix = first_photo.get("prefix", "")
        suffix = first_photo.get("suffix", "")
        url1 = f"{prefix}original{suffix}"
        photos12=url1
        
    else:
        try:
            photos12 = flickr_api(name=name12, latitude=latitude12, longitude=longitude12)
        except:
            print ("flickr api can't bring an image")

    hotels_info = {
        "name": name12,
        "latitude": latitude12,
        "longitude": longitude12,
        "photos": photos12,
        "review_score": rating12,
        "website": website12,
        "description": description1,
        "hours":hours,
        "address":address,
        "tel":tel,
        'tips':tips,
        # 'city_obj':city_obj.id
    }

    hotels.append(hotels_info)
    


def generate_schedule(data,country,check,):
    print ('@@@@@@@@@@@@@@@@@@@',check)
    total = 0    
    try:
        cities = data['cities']
        num_attractions_per_day = 3
        attraction_duration = timedelta(hours=3)
        lunch_break_start = datetime.strptime('14:00', '%H:%M').time()
        lunch_break_end = datetime.strptime('16:00', '%H:%M').time()
        daily_schedule_end = datetime.strptime('19:00', '%H:%M').time()

        schedule = {'schedules': [] }  # Initialize the schedule dictionary
        for city in cities:
            # print(city)
            city_name = city['city']
            query1=City.objects.get(city=city_name)
            landmarks=[query1.latitude,query1.longitude]
            city_description = city['description']
            attractions = city['attractions']
            count=0

            for attraction in attractions:
                count+=1
                try:
                    prices=calculate_total_price_attractions(attraction)
                    total+=prices
                except: 
                    pass
           
            restaurants = city['restaurants']
            hotels=city['hotels']
            night_life=city.get("night-life","")
            sunset=city.get('sunset',"")
            days_spent = city['days_spent']

            try:
                if check==False:
                    attractions = sort_attractions_by_distance(attractions=attractions, first_attraction=attractions[0])
            except Exception as e:
                print('already sorted')

            days_spent=int(days_spent)
            num_attractions = min(len(attractions), int(num_attractions_per_day) * int(days_spent))
            num_attractions_per_day = int(num_attractions_per_day) 

            # num_attractions = min(len(attractions), num_attractions_per_day * days_spent)
            attractions_per_day = num_attractions // days_spent
            extra_attractions = num_attractions % days_spent

            start_time = datetime(year=1, month=1, day=1, hour=8, minute=0)

            city_schedule = {'city': city_name, 'description': city_description,'landmarks':landmarks,'restaurants':restaurants,'hotels':hotels,'night-life':night_life,'sunset':sunset,'schedules': []}

            for day in range(days_spent):
                day_schedule = {'day': day + 1, 'attractions': []}

                for i in range(attractions_per_day):
                    attraction_index = day * attractions_per_day + i
                    attraction = attractions[attraction_index]
                    attraction_start = start_time + (attraction_duration * i)

                    # Add lunch break if within attraction hours
                    try:
                        lunch_break_start = datetime.strptime('14:00', '%H:%M').time() 
                        lunch_break_end = datetime.strptime('16:00', '%H:%M').time()

                        if lunch_break_start <= attraction_start.time() < lunch_break_end:
                            attraction_start += timedelta(hours=2)
                    except Exception as e:
                        print('filaed in 212',e)
                    attraction_end = attraction_start + attraction_duration

                    attraction_data = {
                        # 'attraction': {
                              'id': attraction.get('id', ''),
                                'city_id': attraction.get('city_id', ''),
                                'name': attraction.get('name', ''),
                                'latitude': attraction.get('latitude', ''),
                                'longitude': attraction.get('longitude', ''),
                                'photos': attraction.get('photos', ''),
                                'review_score': attraction.get('review_score', ''),
                                'description': attraction.get('description', ''),
                                'website': attraction.get('website', ''),
                                'hours_popular': attraction.get('hours_popular', ''),
                                'hours': attraction.get('hours', ''),
                                'address': attraction.get('address', ''),
                                'tips': attraction.get('tips', ''),
                                'tel': attraction.get('tel', ''),
                                'distance': attraction.get('distance', ''),
                                'real_price': attraction.get('real_price', ''),
                                'start_time': attraction_start.strftime('%H:%M'),
                                'end_time': attraction_end.strftime('%H:%M')
                        
                    }

                    day_schedule['attractions'].append(attraction_data)
                try:
                # Add extra attraction if available and within the schedule
                    if extra_attractions > 0 and day_schedule['attractions'][-1]['attraction']['end_time'] < daily_schedule_end.strftime('%H:%M'):
                        extra_attraction = attractions[num_attractions - extra_attractions]
                        extra_attraction_start = start_time + (attraction_duration * (attractions_per_day + extra_attractions - 1))
                        extra_attraction_end = extra_attraction_start + attraction_duration

                        try:
                            if extra_attraction_end.time() <= daily_schedule_end:
                                extra_attraction_data = {
                                    'attraction': {
                                        'id': extra_attraction.get('id', ''),
                                        'city_id': extra_attraction.get('city_id', ''),
                                        'name': extra_attraction.get('name', ''),
                                        'latitude': extra_attraction.get('latitude', ''),
                                        'longitude': extra_attraction.get('longitude', ''),
                                        'photos': extra_attraction.get('photos', ''),
                                        'review_score': extra_attraction.get('review_score', ''),
                                        'description': extra_attraction.get('description', ''),
                                        'website': extra_attraction.get('website', ''),
                                        'hours_popular': extra_attraction.get('hours_popular', ''),
                                        'hours': extra_attraction.get('hours', ''),
                                        'address': extra_attraction.get('address', ''),
                                        'tips': extra_attraction.get('tips', ''),
                                        'tel': extra_attraction.get('tel', ''),
                                        'distance': extra_attraction.get('distance', ''),
                                        'real_price': extra_attraction.get('real_price', ''),
                                        'start_time': extra_attraction_start.strftime('%H:%M'),
                                        'end_time': extra_attraction_end.strftime('%H:%M')
                                    }
                                }
                                day_schedule['attractions'].append(extra_attraction_data)
                                extra_attractions -= 1
                        except Exception as e:
                            print ('Error in 265',e)
                            
                except Exception as e:
                    print('not extra attraction',e)


                start_time += timedelta(days=1)
                city_schedule['schedules'].append(day_schedule)

            schedule['schedules'].append(city_schedule)
    except Exception as e:
        
        print('failed in 261')
        traceback.print_exc() 
    taxi_cost = 0
    Lunch = 0
    price_for_dinner = 0
    prices_for_country=get_cities_by_country(country, limit=2)
    if prices_for_country:
        taxi_cost = prices_for_country.get('5km taxi ride', 0)
        Lunch = prices_for_country.get('Lunch', 0)
        price_for_dinner=prices_for_country.get('Price of a meal at a restaurant',0)
    else:
        print('No cities found.')

    if taxi_cost:
            total_transport_private_taxi = count * int(taxi_cost)
    else:
        total_transport_private_taxi = 0

    price_for_dinner=price_for_dinner*days_spent
    total_food_prices=((Lunch*days_spent*2)+price_for_dinner)
    
    return {"schedule":schedule,"total_prices":int(total),"total_transport_private_taxi":(total_transport_private_taxi),"total_food_prices":int(total_food_prices)}
    # return schedule



def calculate_distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Earth's radius in kilometers
    radius = 6371

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = radius * c

    return distance

def sort_attractions_by_distance(attractions, first_attraction):
    print ('start sort')
    # Sort attractions based on distance from the first attraction
    first_attraction=attractions[0]
    sorted_attractions = sorted(attractions, key=lambda x: calculate_distance(
        first_attraction['latitude'],
        first_attraction['longitude'],
        x['latitude'],
        x['longitude']
    ))
    
    return sorted_attractions






# def extract_attraction_data(my_attractions):
    
#         for attraction_data in my_attractions:
#             city = attraction_data["city"]

#             name = attraction_data["name"]
#             latitude = attraction_data["latitude"]
#             longitude = attraction_data["longitude"]
#             photos = flickr_api(name, latitude, longitude)
#             review_score = attraction_data["review_score"]
#             description = attraction_data["description"]
#             website = attraction_data["website"]
#             hours_popular = attraction_data["hours_popular"]
#             distance = attraction_data["distance"]
#             real_price = attraction_data["real_price"]
#             website = website or ""
#             hours_popular = hours_popular or ""
#             print (name,latitude,longitude,review_score,description,website,hours_popular,distance,real_price)
#             city_objs = City.objects.filter(city=city).first()
#             if city_objs:
#                 print (city_objs.id,'AAAAAAA')
#                 # city_obj = city_objs[0]
#                 print (city_objs.id,'AAAAAAA')
#                 atrc_query = Attraction(
#                 name=name,
#                 city=city_objs,
#                 latitude=latitude,
#                 longitude=longitude,
#                 photos=photos,
#                 review_score=review_score,
#                 description=description,
#                 website=website,
#                 hours_popular=hours_popular,
#                 distance=distance,
#                 real_price=real_price
#             )
#                 atrc_query.save()
#                 print("Save attraction successfully")
               

#             else:
#                 print ("can't save")


# def extract_restaraunt_data(my_resturants):

#         for restaraunt_data in my_resturants:
#             city = restaraunt_data["city"]

#             name = restaraunt_data["name"]
#             latitude = restaraunt_data["latitude"]
#             longitude = restaraunt_data["longitude"]
#             photos = flickr_api(name, latitude, longitude)
#             review_score = restaraunt_data["review_score"]
#             website = restaraunt_data["website"]
#             distance = restaraunt_data["distance"]
#             # social_media=restaraunt_data['social_media']
#             price=restaraunt_data['price']
#             menu=restaraunt_data['menu']
#             website = website or ""
#             menu=menu or ""
#             distance= ""
#             city_objs = City.objects.filter(city=city).first()
#             if city_objs:
#                 resta_query = Restaurant(
#                 name=name,
#                 city=city_objs,
#                 latitude=latitude,
#                 longitude=longitude,
#                 photos=photos,
#                 review_score=review_score,
#                 website=website,
#                 # social_media=social_media,
#                 distance=distance,
#                 price=price,
#                 menu=menu
#                     )
#                 resta_query.save()
#                 print("Save attraction successfully")
               

#             else:
#                 print ("can't save")



# def restaurant_GPT(city):
#         api_key = os.environ.get("OPENAI_API_KEY")
#         openai.api_key = api_key
#         more_data='restaurants:[{name:"",latitude:Float,longitude:Float,review_score:"",website:"",distance:"",price:" 1=cheap5=most expnesive",menu:""}]'
#         message_for_restaurant=f'provide me 10 restarunts in {city} return me as json like that{more_data}'
#         retries = 3  # Maximum number of retries
            
#         for _ in range(retries):
#             try:
#                 completion = openai.ChatCompletion.create(
#                     model="gpt-3.5-turbo",
#                     messages=[{"role": "user", "content": message_for_restaurant}],
#                 )
#                 answer1 = completion.choices[0].message.content
#                 data = json.loads(answer1)
#                 restaurants = data["restaurants"]
#                 return restaurants
#             except Exception as e:
#                 print('Error:', str(e))
#                 print('Retrying...')
#                 continue  # Retry the API call
            
#         else:
#             print('Failed after retries. Not good with ChatGPT')


def quick_from_data_base(country,answer_dict,request_left,trip_id):

    answer_string_modified = re.sub(r"(?<!\w)'(?!:)|(?<!:)'(?!\w)", '"', answer_dict)
    try:
        answer_dict = json.loads(answer_string_modified)
    except:
        print ('EEXPETTTTTTTTTTTTTTT')
        answer_dict = ast.literal_eval(answer_dict)

    try:
        itinerary_description=answer_dict['itinerary-description']
    except:
        print ('failed in 432')
        pass
    try:
        itinerary_description=answer_dict['itinerary_description']
    except:
        pass
    # trip_id=answer_dict['id']

    threads = []
    for city_data in answer_dict["cities"]:
        city_name = city_data["city"]
        normalized_city_name = unidecode(city_name)
        
        try:
            existing_city = City.objects.prefetch_related('attractions', 'restaurants').filter(city__iexact=normalized_city_name).first()
        except:
            print('no regular')
            existing_city = City.objects.filter(Q(city__iexact=normalized_city_name) | Q(city__icontains=normalized_city_name)).first()
        
        if existing_city:
            attractions_list = existing_city.attractions.all().values()
            restaurants_list = existing_city.restaurants.all().values()
            
            attractions = sort_attractions_by_distance(attractions=attractions_list, first_attraction=attractions_list[0])
            first_5_attractions = attractions[:5]
            remaining_attractions = attractions[5:]
            random.shuffle(remaining_attractions)
            final_attractions = first_5_attractions + remaining_attractions

            city_data["attractions"] = final_attractions
            
            city_data["restaurants"] = list(restaurants_list)
            
            lat = existing_city.latitude
            lon = existing_city.longitude
            landmarks = [lat, lon]

            # hotels = process_hotels(landmarks, city_name)
            # city_data["hotels"] = hotels
            # night_life = my_night_life(landmarks)
            # city_data["night-life"] = night_life
            # sunset=sunset_api(landmarks)
            # if sunset:
            #     city_data['sunset']=sunset
            sunset_thread = Thread(target=fetch_sunset_and_update, args=(city_data, landmarks,))
            hotels_thread = Thread(target=fetch_hotels_and_update, args=(city_data, landmarks, city_name,))
            nightlife_thread = Thread(target=fetch_nightlife_and_update, args=(city_data, landmarks))

            threads.extend([sunset_thread, hotels_thread, nightlife_thread])

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    
    
    check=True
    
    answer_from_data1=generate_schedule(answer_dict,country,check)
   
    total_prices=answer_from_data1['total_prices']
    total_transport_private_taxi=answer_from_data1["total_transport_private_taxi"]
    total_food_prices=answer_from_data1['total_food_prices']
    existing_country = Country.objects.get(name=country)

    avrage_daily_spent=int(existing_country.average_prices)
    costs={
        "total_prices":total_prices,
        "total_transport_private_taxi":total_transport_private_taxi,
        "total_food_prices":total_food_prices,
        "avrage_daily_spent":avrage_daily_spent,
    }
    end_result=answer_from_data1["schedule"]
    end_result.update(costs)
    answer=({'answer' :end_result,"itinerary_description":itinerary_description,"request_left":request_left,"trip_id":trip_id})
    return answer




API_KEY=os.environ.get('google_key')
def restarunts_from_google(restaur, city_obj, restaurants):
    name_resta = restaur['name']
    latt = restaur['geometry']['location']['lat']
    lng1 = restaur['geometry']['location']['lng']
    price_level=restaur['price_level'] if restaur.get('price_level') else ""
    website_resta=restaur['website'] if restaur.get('website') else ""
    rating = restaur['rating']
    place_id = restaur['place_id'] if restaur.get('place_id') else None
    photo_reference = restaur['photos'][0]['photo_reference'] if restaur.get('photos') else None

    initial_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={API_KEY}"
    response = requests.get(initial_url)
    final_url = response.url
    # city_obj1=City.objects.filter(id=city_obj).first()
    place = {
    "name": name_resta,
    "latitude": latt,
    "longitude": lng1,
    "review_score": rating,
    "photos":final_url,
    "price": price_level,
    "website":website_resta,
    "city_obj":city_obj.id
}
    restaurants.append(place)


def attraction_from_google(attracs, city_obj, attractions):
    name_attrac = attracs['name']
    lat = attracs['geometry']['location']['lat']
    lng = attracs['geometry']['location']['lng']
    rating1 = attracs['rating']
    if rating1==0:
        return ""
    image = flickr_api(name=name_attrac,latitude=lat,longitude=lng)
    place = {
        "name": name_attrac,
        "latitude": lat,
        "longitude": lng,
        "review_score": rating1,
        
        "photos":image,
        "city_obj":city_obj.id
    }
    attractions.append(place)
    

def hotel_from_google(hotel, hotels):
    name_hotel = hotel['name']
    lattt = hotel['geometry']['location']['lat']
    lngg1 = hotel['geometry']['location']['lng']
    rating = hotel['rating']
    place_id = hotel['place_id'] if hotel.get('place_id') else None
    photo_reference = hotel['photos'][0]['photo_reference'] if hotel.get('photos') else None

    initial_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={API_KEY}"
    response = requests.get(initial_url)
    final_url = response.url
    place = {
    "name": name_hotel,
    "latitude": lattt,
    "longitude": lngg1,
    "review_score": rating,
    "photos":final_url,
    # "city_obj":city_obj.id
}
    hotels.append(place)




from django.core.cache import cache

def fetch_sunset_and_update(city_data,landmarks):
    cache_key = f"sunset_{landmarks[1]}"
    # Attempt to retrieve data from the cache
    sunset1 = cache.get(cache_key)
    if sunset1 is None:
        sunset = sunset_api(landmarks)
        if sunset:
            city_data["sunset"] = sunset
            cache.set(cache_key, sunset, timeout=7 * 24 * 60 * 60)

    else:
        city_data["sunset"] = sunset1

def fetch_hotels_and_update(city_data, landmarks, city_name):
    from app.chat import process_hotels
    
    hotels = process_hotels(landmarks, city_name)
    city_data["hotels"] = hotels

def fetch_nightlife_and_update(city_data, landmarks):
    cache_key = f"nightlife_{landmarks[0]}"
    # Attempt to retrieve data from the cache
    nightlife1 = cache.get(cache_key)

    if nightlife1 is None:
        nightlife = my_night_life(landmarks)
        city_data["night-life"] = nightlife
        cache.set(cache_key, nightlife, timeout=7 * 24 * 60 * 60)

    else:
        print (nightlife1)
        city_data["night-life"] = nightlife1
