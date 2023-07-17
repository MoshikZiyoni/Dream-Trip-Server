from concurrent.futures import ThreadPoolExecutor
import json
from django.http import JsonResponse
import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import process_city, run_long_poll_async
from app.models import Attraction, Country, QueryChatGPT,City, Restaurant
from django.core.cache import cache

from app.my_selenium import perform_search
from app.trip_advisor import flickr_api, foursquare_attraction, foursquare_restaurant
from app.utils import extract_attraction_data, extract_restaraunt_data, generate_schedule, process_attraction, process_restaurant
# from threading import Thread
# from app.wikipediaapi import process_query
import os
import requests
import traceback
import re

@api_view(['GET', 'POST'])
def gpt_view(request):
    
    
    # def foursquare_restaurant(city,landmark):
    #     api_key=os.environ.get('FOURSQUARE')
    #     url = "https://api.foursquare.com/v3/places/search?"
    #     print(landmark[0])
    #     headers = {
    #         "accept": "application/json",
    #         "Authorization": api_key
    #     }

    #     query = {
    #         'query': f"restaurants in {city}",
    #         'categories': '13000',
    #         "ll" :  f"{landmark[0]},{landmark[1]}",
    #         'radius': 5000,
    #         'limit': 10,
    #         'fields':'distance,geocodes,name,rating,price,website,photos,social_media,menu'
    #     }

    #     response = requests.get(url, params=query, headers=headers)
    #     response_text = response.text
    #     jsonto = json.loads(response_text)
    #     results = jsonto['results']
    #     print(jsonto)
    #     city_obj = City.objects.filter(city=city).first()
    #     if not city_obj:
    #         pass
    #     # for i in results:
    #     #     process_restaurant(city_obj=city_obj,restaur=i,restaurants=[])
    #     #     print ('save sucess')
    # foursquare_restaurant(city='Manchester',landmark=[53.4808,2.2426])
    # return 'ok'
    # def foursquare_restaurant(city,landmark):
    #     api_key=os.environ.get('FOURSQUARE')
    #     url = "https://api.foursquare.com/v3/places/search?"
    #     print(landmark[0])
    #     headers = {
    #         "accept": "application/json",
    #         "Authorization": api_key
    #     }

    #     query = {
    #         'categories': '13000',
    #         "ll" :  f"{landmark[0]},{landmark[1]}",
    #         'radius': 5000,
    #         'limit': 10,
    #         'fields':'distance,geocodes,name,rating,price,distance,website,photos,social_media,menu'
    #     }

    #     response = requests.get(url, params=query, headers=headers)
    #     response_text = response.text
    #     jsonto = json.loads(response_text)
    #     results = jsonto['results']
    #     city_obj = City.objects.filter(city=city).first()
    #     if not city_obj:
    #         pass
    #     for i in results:
    #         process_restaurant(city_obj=city_obj,restaur=i,restaurants=[])

    # def get_landmarks(city):
    #     landmarks = {  # Example landmarks for Nantes, France
    #     "Vienna": [48.5839, 7.7455],  # Example landmarks for Strasbourg, France
    #     "Bordeaux": [44.8378, -0.5792],  # Example landmarks for Bordeaux, France
    #     "Berlin": [52.5200, 13.4050],  # Example landmarks for Berlin, Germany
    #     "Hamburg": [53.5511, 9.9937],  # Example landmarks for Hamburg, Germany
    #     "Munich": [48.1351, 11.5820],  # Example landmarks for Munich, Germany
    # }
    #     return landmarks.get(city, [])

    # # Example usage
    # cities = [
    #     "Vienna",
        
    # ]

    # for city in cities:
    #     landmark = get_landmarks(city)
    #     print(landmark,'first')
    #     foursquare_restaurant(city,landmark)

    # return 'ok'









    # attractions_without_real_price = Attraction.objects.filter(real_price__isnull=True) | Attraction.objects.filter(real_price='')
    # for attraction in attractions_without_real_price:
    #     print(attraction.name)  
    # return 'ok'  



   





    # def extract_attraction_data(attractions):
    
    #     for attraction_data in attractions:
    #         city = attraction_data["city"]

    #         name = attraction_data["name"]
    #         latitude = attraction_data["latitude"]
    #         longitude = attraction_data["longitude"]
    #         photos = flickr_api(name, latitude, longitude)
    #         if photos==None:
    #             photos=""
    #         review_score = attraction_data["review_score"]
    #         description = attraction_data["description"]
    #         website = attraction_data["website"]
    #         hours_popular = attraction_data["hours_popular"]
    #         distance = attraction_data["distance"]
    #         real_price = attraction_data["real_price"]
    #         website = website or ""
    #         hours_popular = hours_popular or ""
    #         print (name,latitude,longitude,review_score,description,website,hours_popular,distance,real_price)
    #         city_objs = City.objects.filter(city=city).first()
    #         if city_objs:
    #             print (city_objs.id,'AAAAAAA')
    #             # city_obj = city_objs[0]
    #             print (city_objs.id,'AAAAAAA')
    #             atrc_query = Attraction(
    #             name=name,
    #             city=city_objs,
    #             latitude=latitude,
    #             longitude=longitude,
    #             photos=photos,
    #             review_score=review_score,
    #             description=description,
    #             website=website,
    #             hours_popular=hours_popular,
    #             distance=distance,
    #             real_price=real_price
    #         )
    #             atrc_query.save()
    #             print("Save attraction successfully")
            

    #         else:
    #             print ("can't save")


#     extract_attraction_data( attractions=[
#   {
#     "city": "Altai", 
#     "name": "Khoton Nuur",
#     "latitude": 46.4500,
#     "longitude": 96.1500,
#     "photos": ["https://live.staticflickr.com/65535/52042651783_a79b62ed52_c.jpg"],
#     "review_score": 4.6,
#     "description": "Large scenic freshwater lake surrounded by forested mountains",
#     "website": "",
#     "hours_popular": "Always accessible",
#     "distance": "10 km north of Altai city",
#     "real_price": "Free entry"
#   },

#   {
#     "city": "Altai",
#     "name": "Tsambagarav Uul",
#     "latitude": 48.0167,
#     "longitude": 95.7167,
#     "photos": ["https://live.staticflickr.com/65535/52042652063_b459b06849_c.jpg"],
#     "review_score": 4.5,
#     "description": "Glaciated peak with scenic hiking trails and amazing mountain views",
#     "website": "",
#     "hours_popular": "Always open", 
#     "distance": "90 km northeast of Altai city",
#     "real_price": "Free entry"
#   },

#   {
#     "city": "Altai",
#     "name": "Biger Nuur",
#     "latitude": 46.2667,
#     "longitude": 96.2667,
#     "photos": ["https://live.staticflickr.com/65535/52042652343_a74062ed6b_c.jpg"],
#     "review_score": 4.3,
#     "description": "Picturesque freshwater lake surrounded by rolling steppe hills",
#     "website": "",
#     "hours_popular": "Always accessible",
#     "distance": "35 km south of Altai city",
#     "real_price": "Free entry"
#   },
  
#   {
#     "city": "Altai",
#     "name": "Khan Khokh Canyon",
#     "latitude": 48.0500,
#     "longitude": 89.9667,
#     "photos": ["https://live.staticflickr.com/65535/52042652618_9cba1ddc8c_c.jpg"],
#     "review_score": 4.5,
#     "description": "Colorful rock canyon with unusual formations along the Khukh River",
#     "website": "",
#     "hours_popular": "Open 24 hours",
#     "distance": "220 km northwest of Altai city",
#     "real_price": "Free entry"
#   },

#   {
#     "city": "Altai",
#     "name": "Turgen Canyon",
#     "latitude": 48.0833,
#     "longitude": 89.0333,
#     "photos": ["https://live.staticflickr.com/65535/52042652868_9a2ddb672c_c.jpg"],
#     "review_score": 4.4,
#     "description": "Deep river canyon featuring colorful rock formations and cliffs",
#     "website": "",
#     "hours_popular": "Always open",
#     "distance": "190 km northwest of Altai city",
#     "real_price": "Free entry"
#   },

#   {
#     "city": "Altai",
#     "name": "Altai Tavan Bogd National Park",
#     "latitude": 48.9667,
#     "longitude": 88.7500,
#     "photos": ["https://live.staticflickr.com/65535/52042653118_313c9d64ef_c.jpg"],
#     "review_score": 4.8,
#     "description": "Rugged alpine scenery with glaciers, peaks, lakes and endangered wildlife",
#     "website": "",
#     "hours_popular": "Always open",
#     "distance": "260 km northwest of Altai city", 
#     "real_price": "Free entry"
#   },

#   {
#     "city": "Altai",
#     "name": "Khull Nuur",
#     "latitude": 46.7667,
#     "longitude": 95.9667,
#     "photos": ["https://live.staticflickr.com/65535/52042653353_cc6d10d487_c.jpg"],
#     "review_score": 4.2,
#     "description": "Crystal clear lake surrounded by pine forest in the Mongol Altai Mountains",
#     "website": "",
#     "hours_popular": "Always accessible",
#     "distance": "65 km northeast of Altai city",
#     "real_price": "Free entry"
#   },

#   {
#     "city": "Altai",
#     "name": "Dayan Deereh Valley",
#     "latitude": 47.4000,
#     "longitude": 95.0500,
#     "photos": ["https://live.staticflickr.com/65535/52042653588_f1511b2d94_c.jpg"],
#     "review_score": 4.3,
#     "description": "Panoramic valley with rock formations, rivers and nomadic camps",
#     "website": "",
#     "hours_popular": "Always open",
#     "distance": "70 km east of Altai city",
#     "real_price": "Free entry" 
#   },

#   {
#     "city": "Altai",
#     "name": "Tolbo Lake",
#     "latitude": 46.5500,
#     "longitude": 90.8667,
#     "photos": ["https://live.staticflickr.com/65535/52042653818_9908863e5b_c.jpg"],
#     "review_score": 4.1,
#     "description": "Scenic freshwater lake surrounded by rolling grasslands",
#     "website": "",
#     "hours_popular": "Always accessible",
#     "distance": "90 km southwest of Altai city",
#     "real_price": "Free entry"
#   },

#   {
#     "city": "Altai",
#     "name": "Dayan Lake",
#     "latitude": 47.7167,
#     "longitude": 89.6000,
#     "photos": ["https://live.staticflickr.com/65535/52042654043_a7d7a0fd81_c.jpg"],
#     "review_score": 4.4,
#     "description": "Stunning deep blue glacial lake nestled amongst mountain peaks", 
#     "website": "",
#     "hours_popular": "Always accessible",
#     "distance": "160 km northwest of Altai city",
#     "real_price": "Free entry"  
#   }
# ]
# )
#     return 'ok'
    




#     def extract_restaurants_data(attractions):
        
#         for attraction_data in attractions:
#             city = attraction_data["city"]

#             name = attraction_data["name"]
#             latitude = attraction_data["latitude"]
#             longitude = attraction_data["longitude"]
#             photos = flickr_api(name, latitude, longitude)
#             if photos==None:
#                 photos=""
#             review_score = attraction_data["review_score"]
            
#             website = attraction_data["website"]
            
#             distance = attraction_data["distance"]
#             price = attraction_data["price"]
#             website = website or ""
#             print (name,latitude,longitude,review_score,website,distance,price)
#             city_objs = City.objects.filter(city=city).first()
#             if city_objs:
#                 print (city_objs.id,'AAAAAAA')
#                 # city_obj = city_objs[0]
#                 print (city_objs.id,'AAAAAAA')
#                 atrc_query = Restaurant(
#                 name=name,
#                 city=city_objs,
#                 latitude=latitude,
#                 longitude=longitude,
#                 photos=photos,
#                 review_score=review_score,
#                 website=website,
#                 distance=distance,
#                 price=price
#             )
#                 atrc_query.save()
#                 print("Save attraction successfully")
            

#             else:
#                 print ("can't save")
#     extract_restaurants_data(attractions  = [
  
   
# ])




#     return 'ok'

   
    # QueryChatGPT.objects.all().delete()
    
    # City.objects.all().delete()
    # Attraction.objects.all().delete()
    # Restaurant.objects.all().delete()
    

    
   
    email=request.data['email']
    if not email:
        return JsonResponse({'error': 'Email not provided'})

    # Check if the user's email exists in the request count dictionary
    request_count = cache.get(email, 0)
    # If the user has made more than 10 requests in the past 24 hours, block the request
    if request_count >= 100:
        return JsonResponse({'error': 'Too many requests'})

    # Otherwise, increment the request count and set the cache with the new value
    request_count += 1
    print (request_count)
    request_left=11-request_count
    timeout_seconds = 24 * 60 * 60  # 24 hours in seconds
    cache.set(email, request_count, timeout=timeout_seconds)
    try:

        # Define variables
        mainland = request.data['country']
        # adult = request.data['adult']
        # children = request.data['children']
        durring = request.data['durringDays']
        question1 = '{"country": "..", "cities": [{"city": "", "description": "", "days_spent": "" }]"itinerary-description":""}'
        # question1 = '{"country": "..", "cities": [{"city": "", "description": "",landmarks:{latitude : "float",longitude : "float"}, "travelDay": }]}'
        # ourmessage=f"Create a circular trip for {durring} days, visiting  {mainland} in the following JSON structure:{question1}. Ensure that each city is visited for at least 2 days. If the duration of the trip is less than or equal to 3 days, return only 1 city."
        ourmessage=f"Please suggest a round trip itinerary starting and ending at point A in {mainland}, considering {durring} available days. If {durring} is 3 or less, provide an itinerary with a single city. Ensure a minimum stay of 3 days in each city. Return the itinerary in the following JSON structure:{question1}"
        answer_from_data = QueryChatGPT.objects.filter(question__exact=ourmessage).values('answer').first()
        if answer_from_data:
            print('answer in data')
            answer_string = answer_from_data['answer']
            answer_string_modified = re.sub(r"(?<!\w)'(?!:)|(?<!:)'(?!\w)", '"', answer_string)
            answer_dict = json.loads(answer_string_modified)
            # itinerary_description = answer_dict.get('itinerary-description')
            country = answer_dict["country"]
            if country != mainland:
                print("Country is not mainland. Retrying...")
                
            
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
                    
                    city_data["attractions"] = attractions_list
                    restaura = Restaurant.objects.filter(city_id=existing_city.id).values()
                    restaurants_list = list(restaura)
                    city_data["restaurants"] = restaurants_list
                    print("Continue")
                    continue
                executor.submit(process_city, city_data, country, country_id)

            executor.shutdown()
            answer_from_data1=generate_schedule(answer_dict) 
            answer=({'answer' :answer_from_data1,"itinerary_description":itinerary_description,"request_left":request_left})
            return Response(answer)
        
        result1=(run_long_poll_async(ourmessage,mainland))
        
        result1=result1,{"request_left":request_left}

        return  JsonResponse(result1,safe=False)
    except Exception as e:
        print(f'error: {e}')
        traceback.print_exc() 
        return  Response("An error occurred while processing your request.")
    