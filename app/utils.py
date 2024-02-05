import os
import random
import re
from django.db.models import Q
import requests
from app.models import  City,Country
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
from django.core.cache import cache


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
    categories= restaur.get("categories", "")
    try:
        categorie_name=(categories[1])
        categorie_name=categorie_name['name']
        # print (categorie_name,'@@@@')
    except:
        categorie_name=[]
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
        'city_obj':city_obj.id,
        'category':categorie_name

    }
    restaurants.append(restaurant_info)
    return restaurant_info
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


def process_night_life_foursquare(night_life, night_lifes):
    name12 = night_life.get("name", "")
    latitude12 = (
        night_life["geocodes"]["main"]["latitude"]
        if "geocodes" in night_life
        and "main" in night_life["geocodes"]
        and "latitude" in night_life["geocodes"]["main"]
        else ""
    )
    longitude12 = (
        night_life["geocodes"]["main"]["longitude"]
        if "geocodes" in night_life
        and "main" in night_life["geocodes"]
        and "longitude" in night_life["geocodes"]["main"]
        else ""
    )
    rating12 = night_life.get("rating", "0")
    website12 = night_life.get("website", "")
    description1 = night_life.get("description", "")
    hours=night_life.get('hours', {}).get('display', "")
    address=night_life.get('location', {}).get('formatted_address', "")
    tel=night_life.get('tel', "")
    tips = []
    result_tips = night_life.get("tips", [])  # Get the list of tips from the current result
    for j, tip in enumerate(result_tips):
        if j >= 3:
            break
        tip_text = tip.get("text", "")  # Get the text from the tip dictionary
        tips.append(tip_text)
    
    photos12 = night_life.get("photos", "")
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

    night_life_info = {
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

    night_lifes.append(night_life_info)
    

generate_schedule_lock=RLock()

def generate_schedule(data,country,check):
    with generate_schedule_lock:

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
                city_name = city['city']
                # print (city)
                # query1=City.objects.get(city=city_name)
                # landmarks=[query1.latitude,query1.longitude]
                try:
                    landmarks=city['landmarks']
                except Exception as e :
                    print (e)
                city_description = city['description']
                try:
                    attractions = city['attractions']
                    count=0

                    for attraction in attractions:
                        
                        count+=1
                        try:
                            prices=calculate_total_price_attractions(attraction)
                            total+=prices
                        except: 
                            pass
                except:
                    pass
                restaurants = city.get('restaurants',"")
                breakfast_list = []
                restaurants=list(restaurants)
                lunch_list = []
                dinner_list = []
                rest_of_restaurants = []

                for restaurant  in restaurants:
                    try:
                        print ('restaurant:','!!!!!!!!!!!!!!!!!!')
                        category=restaurant ['category'].lower().strip()
                        if 'breakfast' in category or 'cafe' in category:
                            breakfast_list.append(restaurant )
                        elif 'lunch' in category:
                            lunch_list.append(restaurant )
                        elif 'dinner' in category or re.search(r'\bdinner\b', category):
                            print ('@@@@@@')
                            # dinner_list.append(restaurant )
                        else:
                            rest_of_restaurants.append(restaurant )
                    except:
                        pass

                    
                
                        
                hotels=city.get('hotels',"")
                night_life=city.get("night_life","")
                sunset=city.get('sunset',"")
                days_spent = city['days_spent']
                print (days_spent,'@@@@@@@@@@@@@@@@@')
                
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
                
                city_schedule = {'city': city_name, 'description': city_description,'landmarks':landmarks,'days_spent':days_spent,'restaurants':restaurants,'hotels':hotels,'night_life':night_life,'sunset':sunset,'schedules': []}
                # try:
                #     restaurants.remove(restaurant)
                # except:
                for day in range(days_spent):
                    day_schedule = {'day': day + 1, 'attractions': []}
                    

                    for i in range(attractions_per_day):
                        attraction_index = day * attractions_per_day + i
                        attraction = attractions[attraction_index]
                        attraction_start = start_time + (attraction_duration * i)

                    
                        try:
                            lunch_break_start = datetime.strptime('14:00', '%H:%M').time() 
                            lunch_break_end = datetime.strptime('16:00', '%H:%M').time()

                            if lunch_break_start <= attraction_start.time() < lunch_break_end:
                                attraction_start += timedelta(hours=2)
                        except Exception as e:
                            print('filaed in 212',e)
                        attraction_end = attraction_start + attraction_duration

                        daily_schedule = {
                                
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
                        if len(breakfast_list) == 0:
                            breakfast = random.choice(restaurants)
                        else:
                            breakfast = random.choice(breakfast_list)

                        # Choose lunch
                        if len(lunch_list) == 0:
                            lunch = random.choice(restaurants)
                        else:
                            lunch = random.choice(lunch_list)
                            # Remove the selected restaurant from all three lists
                            if lunch in breakfast_list:
                                breakfast_list.remove(lunch)
                            if lunch in dinner_list:
                                dinner_list.remove(lunch)
                            lunch_list.remove(lunch)

                        # Choose dinner
                        if len(dinner_list) == 0:
                            dinner = random.choice(restaurants)
                        else:
                            dinner = random.choice(dinner_list)
                            # Remove the selected restaurant from all three lists
                            if dinner in breakfast_list:
                                breakfast_list.remove(dinner)
                            if dinner in lunch_list:
                                lunch_list.remove(dinner)
                            dinner_list.remove(dinner)
                            

                        day_schedule['attractions'].append(daily_schedule)
                        day_schedule['breakfast_restaurant'] = breakfast
                        day_schedule['lunch_restaurant'] = lunch
                        day_schedule['dinner_restaurant'] = dinner
                    
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
        if prices_for_country is not None:
            taxi_cost = prices_for_country.get('5km taxi ride', 0)
            Lunch = prices_for_country.get('Lunch', 0)
            price_for_dinner=prices_for_country.get('Price of a meal at a restaurant',0)
        else:
            print('No cities found.')

        try:
            
            total_transport_private_taxi = count * int(taxi_cost)
        except:
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
    distance_km = radius * c
    distance_meters = distance_km * 1000


    return distance_km

def sort_attractions_by_distance(attractions, first_attraction):
    print ('start sort')
    try:
        # Sort attractions based on distance from the first attraction
        first_attraction=attractions[0]
        sorted_attractions = sorted(attractions, key=lambda x: calculate_distance(
            first_attraction['latitude'],
            first_attraction['longitude'],
            x['latitude'],
            x['longitude']
        ))
        
        return sorted_attractions
    except:
        print(f'first attraction{first_attraction}')





def quick_from_data_base(country,answer_dict,request_left,trip_id,durring):

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
            
            
            lat = existing_city.latitude
            lon = existing_city.longitude
            landmarks = [lat, lon]
            attractions_cache_key = f"attractions_{landmarks[0]}"
            # Attempt to retrieve data from the cache
            attractions_cache = cache.get(attractions_cache_key)

            if attractions_cache is None:
                print ('attraction is none')
                attractions_list = existing_city.attractions.all().values()
                if len(attractions_list)==0:
                    from app.chat import process_attractions
                    attractions_list=process_attractions(landmarks=landmarks,city_name=existing_city.city,city_obj=existing_city,country=existing_city.country)  
                cache.set(attractions_cache_key, attractions_list, timeout=7 * 24 * 60 * 60)
            else:
                print ('attractions_cache')
                attractions_list=attractions_cache

            restaurants_cache_key = f"restaurants_{landmarks[0]}"
            restaurants_cache = cache.get(restaurants_cache_key)
            if restaurants_cache is None:
                restaurants_list = existing_city.restaurants.all().values()
                if len(restaurants_list)==0:
                    from app.chat import process_restaurants
                    restaurants_list=process_restaurants(landmarks=landmarks, city_name=existing_city.city, city_obj=existing_city)
                cache.set(restaurants_cache_key, restaurants_list, timeout=7 * 24 * 60 * 60)
            else:
                print('restaurants_cache')
                restaurants_list=restaurants_cache
                 
            sunset_thread = Thread(target=fetch_sunset_and_update, args=(city_data, landmarks))
            hotels_thread = Thread(target=fetch_hotels_and_update, args=(city_data, landmarks, city_name))
            nightlife_thread = Thread(target=fetch_nightlife_and_update, args=(city_data, landmarks))

            threads.extend([sunset_thread, hotels_thread, nightlife_thread])

            

           
            try:
                attractions = sort_attractions_by_distance(attractions=attractions_list, first_attraction=attractions_list[0])
                first_5_attractions = attractions[:5]
                remaining_attractions = attractions[5:]
                random.shuffle(remaining_attractions)
                final_attractions = first_5_attractions + remaining_attractions
            except:
                final_attractions=attractions_list
            city_data['landmarks']=landmarks
            city_data["attractions"] = final_attractions
            city_data["restaurants"] = list(restaurants_list)
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
    avrage_daily_spent=(existing_country.average_prices)
    if avrage_daily_spent=='':
        avrage_daily_spent=0
    else:
        avrage_daily_spent=int(avrage_daily_spent)

    costs={
        "total_prices":total_prices,
        "total_transport_private_taxi":total_transport_private_taxi,
        "total_food_prices":total_food_prices,
        "avrage_daily_spent":avrage_daily_spent,
    }
    end_result=answer_from_data1["schedule"]
    end_result.update(costs)
    answer=({'answer' :end_result,"itinerary_description":itinerary_description,"request_left":request_left,"trip_id":trip_id,"durring":durring})
    return answer




API_KEY=os.environ.get('google_key')
def restarunts_from_google(restaur, city_obj, restaurants):
    name_resta = restaur['name']
    latt = restaur['geometry']['location']['lat']
    lng1 = restaur['geometry']['location']['lng']
    price_level=restaur['price_level'] if restaur.get('price_level') else ""
    website_resta=restaur['website'] if restaur.get('website') else ""
    rating = restaur['rating']
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




hotel_lock=RLock()
night_life_lock=RLock()
sun_set_lock=RLock()

def fetch_sunset_and_update(city_data,landmarks):
    with sun_set_lock:
        cache_key = f"sunset_{landmarks[1]}"
        # Attempt to retrieve data from the cache
        sunset1 = cache.get(cache_key)
        if sunset1 is None or sunset1=={'sunset': ''}:
            sunset = sunset_api(landmarks)
            if sunset:
                city_data["sunset"] = sunset
                cache.set(cache_key, sunset, timeout=7 * 24 * 60 * 60)

        else:
            if len(sunset1)<1:
                sunset = sunset_api(landmarks)
                if sunset:
                    city_data["sunset"] = sunset
                    cache.set(cache_key, sunset, timeout=7 * 24 * 60 * 60)
            else:
                print ('sunset cache')
                city_data["sunset"] = sunset1



def fetch_hotels_and_update(city_data, landmarks, city_name):
    from app.chat import process_hotels
    with hotel_lock:
        hotels = process_hotels(landmarks, city_name)
        city_data["hotels"] = hotels



def fetch_nightlife_and_update(city_data, landmarks):
    with night_life_lock:
        cache_key = f"nightlife_{landmarks[0]}"
        # Attempt to retrieve data from the cache
        nightlife1 = cache.get(cache_key)

        if nightlife1 is None or nightlife1=={'night_life': ''}:
            print ('start nightlife')
            nightlife = my_night_life(landmarks)
            
            try:
                if nightlife=={'night_life': ''}:
                    from app.chat import process_night_life
                    nightlife=process_night_life(landmarks)
                    # print(jsonto,'!!!!!!!!!!!!!!!')
            except Exception as e:
                print('line 166' ,e)

            city_data["night_life"] = nightlife
            cache.set(cache_key, nightlife, timeout=7 * 24 * 60 * 60)

        else:
            print ('night_life cache')
            city_data["night_life"] = nightlife1



def clean_json_data(data_str):
    # Attempt to clean and fix string literals by adding double quotes
    data_str = data_str.replace('"itinerary-description":', '"itinerary-description":"')
    data_str = data_str.replace('Experience the best of', 'Experience the best of"')
    # Add more similar replacements as needed for your specific data
    
    # Wrap the entire data in a JSON object
    cleaned_data = f'{{{data_str}}}'
    
    return cleaned_data



