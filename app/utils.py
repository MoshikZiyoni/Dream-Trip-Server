from concurrent.futures import ThreadPoolExecutor
import os
import random
import re
import time
import openai
import requests
from app.models import Attraction, City, Hotels_foursqaure, Restaurant,Country
from app.teleport_api import get_cities_by_country
from app.trip_advisor import flickr_api
from app.wikipediaapi import process_query
import json
from datetime import datetime, timedelta
import math
import traceback
from dotenv import load_dotenv
from app.currency_data import calculate_total_price_attractions
import ast

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




def process_hotel(hotel, city_obj, hotels):
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
    if len(description1)==0:
            try:
                wiki=process_query(name12)
                description1=wiki[0]
                print ('descrption from wiki')
            except:
                 print ('descrption from wiki not gooodddddddddddddddd')
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
        'city_obj':city_obj.id
    }

    hotels.append(hotels_info)
    # hotels_query = Hotels_foursqaure(
    #     name=name12,
    #     city=city_obj,
    #     latitude=latitude12,
    #     longitude=longitude12,
    #     photos=photos12,
    #     review_score=rating12,
    #     website=website12,
    #     description=description1
    # )
    # hotels_query.save()
    # print("Save hotels successfully")


def generate_schedule(data,country,check):
    print ('@@@@@@@@@@@@@@@@@@@',check)
    total = 0    
    try:
        cities = data['cities']
        num_attractions_per_day = 3
        attraction_duration = timedelta(hours=3)
        lunch_break_start = datetime.strptime('14:00', '%H:%M').time()
        lunch_break_end = datetime.strptime('16:00', '%H:%M').time()
        daily_schedule_end = datetime.strptime('19:00', '%H:%M').time()

        schedule = {'city': '', 'description': '','schedules': [] }  # Initialize the schedule dictionary
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

            city_schedule = {'city': city_name, 'description': city_description,'landmarks':landmarks,'restaurants':restaurants,'hotels':hotels, 'schedules': []}

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
                            'id': attraction['id'] if 'id' in attraction else '',
                            'city_id': attraction['city_id'] if 'city_id' in attraction else '',
                            'name': attraction['name'] if 'name' in attraction else '',
                            'latitude': attraction['latitude'] if 'latitude' in attraction else '',
                            'longitude': attraction['longitude'] if 'longitude' in attraction else '',
                            'photos': attraction['photos'] if 'photos' in attraction else '',
                            'review_score': attraction['review_score'] if 'review_score' in attraction else '',
                            'description': attraction['description'] if 'description' in attraction else '',
                            'website': attraction['website'] if 'website' in attraction else '',
                            'hours_popular': attraction['hours_popular'] if 'hours_popular' in attraction else '',
                            'hours': attraction['hours'] if 'hours' in attraction else '',
                            'address': attraction['address'] if 'address' in attraction else '',
                            'tips': attraction['tips'] if 'tips' in attraction else '',
                            "tel" : attraction['tel']if 'tel' in attraction else '',
                            'distance': attraction['distance'] if 'distance' in attraction else '',
                            'real_price': attraction['real_price'] if 'real_price' in attraction else '',
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
                                        'id': extra_attraction['id']if 'id' in attraction else '',
                                        'city_id': extra_attraction['city_id']if 'city_id' in attraction else '',
                                        'name': extra_attraction['name']if 'name' in attraction else '',
                                        'latitude': extra_attraction['latitude']if 'latitude' in attraction else '',
                                        'longitude': extra_attraction['longitude']if 'longitude' in attraction else '',
                                        'photos': extra_attraction['photos']if 'photos' in attraction else '',
                                        'review_score': extra_attraction['review_score']if 'review_score' in attraction else '',
                                        'description': extra_attraction['description']if 'description' in attraction else '',
                                        'website': extra_attraction['website']if 'website' in attraction else '',
                                        'hours_popular': extra_attraction['hours_popular']if 'hours_popular' in attraction else '',
                                        'hours': attraction['hours'] if 'hours' in attraction else '',
                                        'address': attraction['address'] if 'address' in attraction else '',
                                        'tips': attraction['tips'] if 'tips' in attraction else '',
                                        "tel" : attraction['tel']if 'tel' in attraction else '',
                                        'distance': extra_attraction['distance']if 'distance' in attraction else '',
                                        'real_price': attraction['real_price'] if 'real_price' in attraction else '',
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
        price_for_dinner=prices_for_country['Price of a meal at a restaurant']
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






def extract_attraction_data(my_attractions):
    
        for attraction_data in my_attractions:
            city = attraction_data["city"]

            name = attraction_data["name"]
            latitude = attraction_data["latitude"]
            longitude = attraction_data["longitude"]
            photos = flickr_api(name, latitude, longitude)
            review_score = attraction_data["review_score"]
            description = attraction_data["description"]
            website = attraction_data["website"]
            hours_popular = attraction_data["hours_popular"]
            distance = attraction_data["distance"]
            real_price = attraction_data["real_price"]
            website = website or ""
            hours_popular = hours_popular or ""
            print (name,latitude,longitude,review_score,description,website,hours_popular,distance,real_price)
            city_objs = City.objects.filter(city=city).first()
            if city_objs:
                print (city_objs.id,'AAAAAAA')
                # city_obj = city_objs[0]
                print (city_objs.id,'AAAAAAA')
                atrc_query = Attraction(
                name=name,
                city=city_objs,
                latitude=latitude,
                longitude=longitude,
                photos=photos,
                review_score=review_score,
                description=description,
                website=website,
                hours_popular=hours_popular,
                distance=distance,
                real_price=real_price
            )
                atrc_query.save()
                print("Save attraction successfully")
               

            else:
                print ("can't save")


def extract_restaraunt_data(my_resturants):

        for restaraunt_data in my_resturants:
            city = restaraunt_data["city"]

            name = restaraunt_data["name"]
            latitude = restaraunt_data["latitude"]
            longitude = restaraunt_data["longitude"]
            photos = flickr_api(name, latitude, longitude)
            review_score = restaraunt_data["review_score"]
            website = restaraunt_data["website"]
            distance = restaraunt_data["distance"]
            # social_media=restaraunt_data['social_media']
            price=restaraunt_data['price']
            menu=restaraunt_data['menu']
            website = website or ""
            menu=menu or ""
            distance= ""
            city_objs = City.objects.filter(city=city).first()
            if city_objs:
                resta_query = Restaurant(
                name=name,
                city=city_objs,
                latitude=latitude,
                longitude=longitude,
                photos=photos,
                review_score=review_score,
                website=website,
                # social_media=social_media,
                distance=distance,
                price=price,
                menu=menu
                    )
                resta_query.save()
                print("Save attraction successfully")
               

            else:
                print ("can't save")



def restaurant_GPT(city):
        api_key = os.environ.get("OPENAI_API_KEY")
        openai.api_key = api_key
        more_data='restaurants:[{name:"",latitude:Float,longitude:Float,review_score:"",website:"",distance:"",price:" 1=cheap5=most expnesive",menu:""}]'
        message_for_restaurant=f'provide me 10 restarunts in {city} return me as json like that{more_data}'
        retries = 3  # Maximum number of retries
            
        for _ in range(retries):
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": message_for_restaurant}],
                )
                answer1 = completion.choices[0].message.content
                data = json.loads(answer1)
                restaurants = data["restaurants"]
                return restaurants
            except Exception as e:
                print('Error:', str(e))
                print('Retrying...')
                continue  # Retry the API call
            
        else:
            print('Failed after retries. Not good with ChatGPT')



def save_to_db(restaurant_for_data,attraction_for_data,hotels_for_data):
    try:
        for attraction in attraction_for_data:
                
            name1 = (attraction['name'])
            check_name=Attraction.objects.filter(name=name1).first()
            if not check_name:   
                                
                latitude1 = attraction['latitude']if 'latitude' in attraction else ''
                longitude1 = attraction['longitude']if 'longitude' in attraction else ''
                photos1 = attraction['photos']if 'photos' in attraction else ''
                review_score1 = attraction['review_score']if 'review_score' in attraction else ''
                website1 = attraction['website']if 'website' in attraction else ''
                hours_popular1 = attraction['hours_popular']if 'hours_popular' in attraction else ''
                description = attraction['description']if 'description' in attraction else ''
                distance1 = attraction['distance']if 'distance' in attraction else ''
                hours1 = attraction['hours']if 'hours' in attraction else ''
                address1 = attraction['address']if 'address' in attraction else ''
                tips1 = attraction['tips']if 'tips' in attraction else ''
                tel1 = attraction['tel']if 'tel' in attraction else ''
                city_obj=attraction['city_obj']if 'city_obj' in attraction else ''
                place_id=attraction["place_id"] if "place_id" in attraction else ''
                city_obj=City.objects.filter(id=city_obj).first()

                atrc_query = Attraction(
                    name=name1,
                    city=city_obj,
                    latitude=latitude1,
                    longitude=longitude1,
                    photos=photos1,
                    review_score=review_score1,
                    description=description,
                    website=website1,
                    hours_popular=hours_popular1,
                    distance=distance1,
                    hours=hours1,
                    tel=tel1,
                    address=address1,
                    tips=tips1,
                    place_id=place_id
                )
                atrc_query.save()
                print(f"Save attraction successfully{name1}")
        for restaurnt in restaurant_for_data:
            name = (restaurnt['name'])
            check_name1=Restaurant.objects.filter(name=name).first()
            if not check_name1:   
                                    
                latitude = restaurnt['latitude']if 'latitude' in restaurnt else ''
                longitude = restaurnt['longitude']if 'longitude' in restaurnt else ''
                photos = restaurnt['photos']if 'photos' in restaurnt else ''
                review_score = restaurnt['review_score']if 'review_score' in restaurnt else ''
                website = restaurnt['website']if 'website' in restaurnt else ''
                social_media = restaurnt['social_media']if 'social_media' in restaurnt else ''
                menu = restaurnt['menu']if 'menu' in restaurnt else ''
                distance = restaurnt['distance']if 'distance' in restaurnt else ''
                hours_resta = restaurnt['hours']if 'hours' in restaurnt else ''
                address_res = restaurnt['address']if 'address' in restaurnt else ''
                tel_res = restaurnt['tel']if 'tel' in restaurnt else ''
                price = restaurnt['price']if 'price' in restaurnt else ''
                place_id1=restaurnt["place_id"] if "place_id" in restaurnt else ''
                city_obj=restaurnt['city_obj']if 'city_obj' in restaurnt else ''
                city_obj=City.objects.filter(id=city_obj).first()
                resta_query = Restaurant(
                        name=name,
                        city=city_obj,
                        latitude=latitude,
                        longitude=longitude,
                        photos=photos,
                        review_score=review_score,
                        menu=menu,
                        social_media=social_media,
                        website=website,
                        price=price,
                        distance=distance,
                        hours=hours_resta,
                        tel=tel_res,
                        address=address_res,
                        place_id=place_id1
                    )
                resta_query.save()
                print(f"Save restaurants successfully {name}")
        
        for hotel in hotels_for_data:
            name12 = (hotel['name'])
            check_name12=Hotels_foursqaure.objects.filter(name=name).first()
            if not check_name12:  
                latitude12 = hotel['latitude']if 'latitude' in hotel else ''
                longitude12 = hotel['longitude']if 'longitude' in hotel else ''
                photos12 = hotel['photos']if 'photos' in hotel else ''
                rating12 = hotel['review_score']if 'review_score' in hotel else ''
                website12 = hotel['website']if 'website' in hotel else ''
                description12 = hotel['description']if 'description' in hotel else ''
                city_obj=hotel['city_obj']if 'city_obj' in hotel else ''
                place_id2=attraction["place_id"] if "place_id" in restaurnt else ''
                city_obj=City.objects.filter(id=city_obj).first()
                hotels_query = Hotels_foursqaure(
                name=name12,
                city=city_obj,
                latitude=latitude12,
                longitude=longitude12,
                photos=photos12,
                review_score=rating12,
                website=website12,
                description=description12,
                place_id=place_id2
                )
                hotels_query.save()
                print("Save hotels successfully")

    except Exception as e:
        print ('can"t save now',e)



def quick_from_data_base(country,answer_dict,process_city,request_left):
    
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
    try:
        existing_country = Country.objects.filter(name=country).first()
        country_id = existing_country.id
        # existing_country.increase_popularity()

    except:
        print("Country does not exist")
    if not existing_country:
        query_for_country = Country(name=country)
        query_for_country.save()
        country_id = query_for_country.id
    executor = ThreadPoolExecutor()
    for city_data in answer_dict["cities"]:
        city_name = city_data["city"]
        existing_city = City.objects.filter(city=city_name).first()
        if existing_city:
            attract = Attraction.objects.filter(city_id=existing_city.id).values()
            attractions_list = list(attract)
            attractions = sort_attractions_by_distance(attractions=attractions_list, first_attraction=attractions_list[0])
            first_5_attractions = attractions[:5]
            remaining_attractions = attractions[5:]
            # Shuffle the remaining attractions randomly
            random.shuffle(remaining_attractions)
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

    executor.shutdown()
    check=True
    answer_from_data1=generate_schedule(answer_dict,country,check)
    total_prices=answer_from_data1['total_prices']
    total_transport_private_taxi=answer_from_data1["total_transport_private_taxi"]
    total_food_prices=answer_from_data1['total_food_prices']
    costs={
        "total_prices":total_prices,
        "total_transport_private_taxi":total_transport_private_taxi,
        "total_food_prices":total_food_prices,
    }
    end_result=answer_from_data1["schedule"]
    answer=({'answer' :end_result,"itinerary_description":itinerary_description,"request_left":request_left,"costs":costs})
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
    "place_id": place_id,
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
    place_id = attracs['place_id']
    image = flickr_api(name=name_attrac,latitude=lat,longitude=lng)
    place = {
        "name": name_attrac,
        "latitude": lat,
        "longitude": lng,
        "review_score": rating1,
        "place_id": place_id,
        "photos":image,
        "city_obj":city_obj.id
    }
    attractions.append(place)
    

def hotel_from_google(hotel, city_obj, hotels):
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
    "place_id": place_id,
    "photos":final_url,
    "city_obj":city_obj.id
}
    hotels.append(place)