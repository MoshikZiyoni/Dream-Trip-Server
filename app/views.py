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
#     attractions_with_price = Attraction.objects.filter(real_price="['price']")
#     for attraction in attractions_with_price:
#         print(attraction.name)
# # Extract all the real_price values for these attractions
#     real_prices = attractions_with_price.values_list('real_price', flat=True)

#     # Convert the result to a list if needed
#     real_prices_list = list(real_prices)

#     # Now you have a list of all the real_price values where price is equal to 'price'
#     # print(real_prices_list)

        
#     return 'ok'
#     def qiuick_attraction(cities_data):
#         for data in cities_data:
#                 country= (data['country'])
#                 city=data['city']
#                 latitude=data['latitude']
#                 longitude=data['longitude']
#                 landmarks=[latitude,longitude]
#                 city_obj=City.objects.filter(city=city).first()
#                 try:
#                     result1=foursquare_attraction(city,landmarks,country)
#                     attractions=[]
#                 except:
#                     print ('no attraction')
#                 try:
#                     for attrac in result1:
#                         process_attraction(attrac, city_obj, attractions)
#                 except:
#                     print ('no attraction1')




#     qiuick_attraction(cities_data = [
#     {'city': 'Osaka', 'latitude': 34.6937, 'longitude': 135.5023, 'country': 'Japan'},
#     {'city': 'Veliko Tarnovo', 'latitude': 43.0757, 'longitude': 25.6172, 'country': 'Bulgaria'},
#     {'city': 'São Paulo', 'latitude': -23.5505, 'longitude': -46.6333, 'country': 'Brazil'},
#     {'city': 'Hiroshima', 'latitude': 34.3853, 'longitude': 132.4553, 'country': 'Japan'},
#     {'city': 'Mendoza', 'latitude': -32.8895, 'longitude': -68.8458, 'country': 'Argentina'},
#     {'city': 'Nagoya', 'latitude': 35.1815, 'longitude': 136.9066, 'country': 'Japan'},
#     {'city': 'Cartagena', 'latitude': 10.391, 'longitude': -75.4794, 'country': 'Colombia'},
#     {'city': 'New York city', 'latitude': 40.7128, 'longitude': -74.0060, 'country': 'United States'},
#     {'city': 'Burgas', 'latitude': 42.5048, 'longitude': 27.4626, 'country': 'Bulgaria'},
#     {'city': 'Vanua Levu', 'latitude': -16.5980, 'longitude': 179.8749, 'country': 'Fiji'},
#     {'city': 'York', 'latitude': 53.9590, 'longitude': -1.0815, 'country': 'United Kingdom'},
#     {'city': 'Machu Picchu', 'latitude': -13.1631, 'longitude': -72.5450, 'country': 'Peru'},
#     {'city': 'Mexico city', 'latitude': 19.4326, 'longitude': -99.1332, 'country': 'Mexico'},
#     {'city': 'New York City', 'latitude': 40.7128, 'longitude': -74.0060, 'country': 'United States'},
#     {'city': 'Arequipa', 'latitude': -16.4090, 'longitude': -71.5375, 'country': 'Peru'},
#     {'city': 'Brasov', 'latitude': 45.6579, 'longitude': 25.6012, 'country': 'Romania'},
#     {'city': 'Torres del Paine', 'latitude': -51.2592, 'longitude': -72.3450, 'country': 'Chile'},
#     {'city': 'Kathmandu', 'latitude': 27.7172, 'longitude': 85.3240, 'country': 'Nepal'},
#     {'city': 'Cesky Krumlov', 'latitude': 48.8127, 'longitude': 14.3176, 'country': 'Czech Republic'},
#     {'city': 'Alicante', 'latitude': 38.3452, 'longitude': -0.4810, 'country': 'Spain'},
#     {'city': 'Queenstown', 'latitude': -45.0312, 'longitude': 168.6626, 'country': 'New Zealand'},
#     {'city': 'Kyoto', 'latitude': 35.0116, 'longitude': 135.7681, 'country': 'Japan'},
#     {'city': 'Zanzibar', 'latitude': -6.1652, 'longitude': 39.1982, 'country': 'Tanzania'},
#     {'city': 'Oaxaca', 'latitude': 17.0732, 'longitude': -96.7266, 'country': 'Mexico'},
#     {'city': 'Malaga', 'latitude': 36.7213, 'longitude': -4.4214, 'country': 'Spain'},
#     {'city': 'Angkor Wat', 'latitude': 13.4125, 'longitude': 103.8660, 'country': 'Cambodia'},
#     {'city': 'Easter Island', 'latitude': -27.1127, 'longitude': -109.3497, 'country': 'Chile'},
#     {'city': 'Petra', 'latitude': 30.3285, 'longitude': 35.4444, 'country': 'Jordan'},
#     {'city': 'Puno', 'latitude': -15.2349, 'longitude': -70.0503, 'country': 'Peru'},
#     {'city': 'Manchester', 'latitude': 53.4830, 'longitude': -2.2441, 'country': 'United Kingdom'},
#     {'city': 'Grand Canyon', 'latitude': 36.1069, 'longitude': -112.1129, 'country': 'United States'},
#     {'city': 'Cancún', 'latitude': 21.1619, 'longitude': -86.8515, 'country': 'Mexico'},
#     {'city': 'Fukuoka', 'latitude': 33.5904, 'longitude': 130.4017, 'country': 'Japan'},
#     {'city': 'Sihanoukville', 'latitude': 10.6093, 'longitude': 103.5296, 'country': 'Cambodia'},
#     {'city': 'Moscow', 'latitude': 55.7558, 'longitude': 37.6176, 'country': 'Russia'},
#     {'city': 'Denarau', 'latitude': -17.7700, 'longitude': 177.3800, 'country': 'Fiji'},
#     {'city': 'Bocas del Toro', 'latitude': 9.3358, 'longitude': -82.2471, 'country': 'Panama'},
#     {'city': 'Bilbao', 'latitude': 43.2630, 'longitude': -2.9350, 'country': 'Spain'},
#     {'city': 'Bali', 'latitude': -8.3405, 'longitude': 115.0920, 'country': 'Indonesia'},
#     {'city': 'Brasília', 'latitude': -15.8267, 'longitude': -47.9218, 'country': 'Brazil'},
#     {'city': 'Marrakesh', 'latitude': 31.6295, 'longitude': -7.9811, 'country': 'Morocco'},
#     {'city': 'Beqa Island', 'latitude': -18.2800, 'longitude': 178.0000, 'country': 'Fiji'},
#     {'city': 'Salar de Uyuni', 'latitude': -20.1333, 'longitude': -67.4891, 'country': 'Bolivia'},
#     {'city': 'Yokohama', 'latitude': 35.4437, 'longitude': 139.6380, 'country': 'Japan'},
#     {'city': 'Ibiza', 'latitude': 38.9067, 'longitude': 1.4203, 'country': 'Spain'},
#     {'city': 'Fernando de Noronha', 'latitude': -3.8400, 'longitude': -32.4100, 'country': 'Brazil'},
#     {'city': 'Bonito', 'latitude': -21.1257, 'longitude': -56.4828, 'country': 'Brazil'},
#     {'city': 'Beijing', 'latitude': 39.9042, 'longitude': 116.4074, 'country': 'China'},
#     {'city': 'Sapporo', 'latitude': 43.0621, 'longitude': 141.3544, 'country': 'Japan'},
#     {'city': 'Mérida', 'latitude': 20.9674, 'longitude': -89.5926, 'country': 'Mexico'},
#     {'city': 'Montego Bay', 'latitude': 18.4762, 'longitude': -77.8939, 'country': 'Jamaica'},
#     {'city': 'Zaragoza', 'latitude': 41.6488, 'longitude': -0.8891, 'country': 'Spain'},
# ])
#     return 'ok'

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



   


    # from django.db.models import Q

    # attractions = Attraction.objects.filter(distance__regex=r'^\d+$')
    # attraction_names_distances = attractions.values('name', 'distance')

    # for data in attraction_names_distances:
    #     name = data['name']
    #     distance = int(data['distance'])
    #     print(f"Name: {name}")
    # return 'ok'


#     def extract_attraction_data(attractions):
    
#         for attraction_data in attractions:
#             city = attraction_data["city"]

#             name = attraction_data["name"]
#             latitude = attraction_data["latitude"]
#             longitude = attraction_data["longitude"]
#             photos = flickr_api(name, latitude, longitude)
#             if photos==None:
#                 photos=""
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


#     extract_attraction_data( attractions=[
 
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

    # from django.db.models import Count

    # # Get the cities without attractions
    # cities_without_attractions = City.objects.annotate(num_attractions=Count('attractions')).filter(num_attractions=0)

    # # Get the cities without restaurants
    # cities_without_restaurants = City.objects.annotate(num_restaurants=Count('restaurants')).filter(num_restaurants=0)

    # # Print the results
    # print("Cities without attractions:")
    # for city in cities_without_attractions:
    #     print(city.city,',')

    # print("Cities without restaurants:")
    # for city in cities_without_restaurants:
    #     print(city.city,',')

    # return 'ok'

   
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
        question1 = '{"country": "..", "cities": [{"city": "", "description": "", "days_spent": "" }], "itinerary-description": ""}'
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
        combined_data = result1['answer']
        itinerary_description1 =result1['itinerary_description']
        main_restaurants = result1['main_restaurants']
        main_attractions = result1['main_attractions']

        result1={
            'answer':combined_data,
            'itinerary_description':itinerary_description1,
            'request_left':request_left
        }
        # result1=result1,{"request_left":request_left}

        return  JsonResponse(result1,safe=False)
    except Exception as e:
        print(f'error: {e}')
        traceback.print_exc() 
        return  Response("An error occurred while processing your request.")
    