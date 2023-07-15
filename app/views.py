from concurrent.futures import ThreadPoolExecutor
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import process_city, run_long_poll_async
from app.models import Attraction, Country, QueryChatGPT,City, Restaurant
from django.core.cache import cache

from app.my_selenium import perform_search
from app.trip_advisor import flickr_api
from app.utils import generate_schedule, process_attraction, process_restaurant
# from threading import Thread
# from app.wikipediaapi import process_query
import os
import requests
import traceback
import re

@api_view(['GET', 'POST'])
def gpt_view(request):
    
    # def foursquare_restaurant():
    #     city='Prague'
    #     api_key=os.environ.get('FOURSQUARE')

    #     landmarks=[50.0755,14.4378]
    #     url1 = "https://api.foursquare.com/v3/places/search?"

    #     headers = {
    #         "accept": "application/json",
    #         "Authorization": api_key
    #     }

    #     query1= {
    #         'query': f"attractions in {city},Czech Republic",
    #         'categories':'10027,10025,10055,10068,16000',
    #         "ll" :  f"{landmarks[0]},{landmarks[1]}",
    #         'radius':6000,
    #         'limit' : 10,
    #         'fields':'distance,geocodes,name,rating,distance,website,description,photos,menu,hours_popular'

    #     }
    #     response1 = requests.get(url1, params=query1,headers=headers)

    #     response_text1=(response1.text)
    #     jsonto1=json.loads(response_text1)
    #     reslut=jsonto1['results']
    #     city_obj = City.objects.filter(city=city).first()
    #     if not city_obj:
    #         pass
    #     for i in reslut:
    #         process_attraction(city_obj=city_obj,attrac=i,attractions=[])
            

    # foursquare_restaurant()
    # return 'ok'





#     def extract_attraction_data(attractions):
    
#         for attraction_data in attractions:
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


#     extract_attraction_data( attractions = [
# {
# "city": "Kutna Hora",
# "name": "Sedlec Ossuary",
# "latitude": 49.774444,
# "longitude": 15.264722,
# "photos": ["https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Kostnice\_Sedlec\_02.jpg/1920px-Kostnice\_Sedlec\_02.jpg"],
# "review_score": 4.5,
# "description": "The Sedlec Ossuary is a small Roman Catholic chapel famous for its interior decoration, which contains the skeletal remains of between 40,000 and 70,000 people.",
# "website": "http://www.ossuary.eu/",
# "hours_popular": "8:00 AM - 5:00 PM",
# "distance": "5 km from city center",
# "real_price": "100 CZK"
# },
# {
# "city": "Kutna Hora",
# "name": "St. Barbara's Church",
# "latitude": 49.766667,
# "longitude": 15.266667,
# "photos": ["https://upload.wikimedia.org/wikipedia/commons/thumb/0/01/Kutna\_Hora-st-barbora-unesco.JPG/1920px-Kutna\_Hora-st-barbora-unesco.JPG"],
# "review_score": 4.7,
# "description": "St. Barbara's Church is a Roman Catholic church and one of the most famous Gothic churches in central Europe.",
# "website": "https://www.khfarnost.cz/en/kostel-svate-barbory/",
# "hours_popular": "9:00 AM - 5:00 PM",
# "distance": "In city center",
# "real_price": "90 CZK"
# },
# {
# "city": "Kutna Hora",
# "name": "Italian Court",
# "latitude": 49.765278,
# "longitude": 15.267222,
# "photos": ["https://upload.wikimedia.org/wikipedia/commons/thumb/f/f8/Vla%C5%A1sk%C3%BD\_dv%C5%AFr\_%28Kutn%C3%A1\_Hora%29.jpg/1280px-Vla%C5%A1sk%C3%BD\_dv%C5%AFr\_%28Kutn%C3%A1\_Hora%29.jpg"],
# "review_score": 4.4,
# "description": "The Italian Court is the former seat of the Central Banking Office of Minting and the Royal Mining Board.",
# "website": "https://www.khfarnost.cz/en/italian-court/",
# "hours_popular": "10:00 AM - 6:00 PM",
# "distance": "In city center",
# "real_price": "90 CZK"
# },
# {
# "city": "Kutna Hora",
# "name": "Cathedral of Saint Barbara",
# "latitude": 49.766667,
# "longitude": 15.266667,
# "photos": ["https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Kutn%C3%A1\_Hora%2C\_chr%C3%A1m\_sv.*Barbory%2C\_n%C3%A1m.*%C4%8Ceskoslovensk%C3%BDch\_legion%C3%A1%C5%99%C5%AF\_-*panoramio.jpg/1920px-Kutn%C3%A1\_Hora%2C\_chr%C3%A1m\_sv.*Barbory%2C\_n%C3%A1m.*%C4%8Ceskoslovensk%C3%BDch\_legion%C3%A1%C5%99%C5%AF*-*panoramio.jpg"],
# "review_score": 4.7,
# "description": "Imposing Gothic cathedral dating back to the 14th century with an elaborate interior and valuable artwork.",
# "website": "https://www.khfarnost.cz/en/cathedral-of-st-barbara/",
# "hours_popular": "9:00 AM - 5:00 PM",
# "distance": "In city center",
# "real_price": "90 CZK"
# },
# {
# "city": "Kutna Hora",
# "name": "Czech Museum of Silver",
# "latitude": 49.771667,
# "longitude": 15.267222,
# "photos": ["https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Kutna\_Hora\_Muzeum\_stribra\_6.JPG/1920px-Kutna\_Hora\_Muzeum\_stribra\_6.JPG"],
# "review_score": 4.5,
# "description": "Museum housed in a renovated building dating from the 14th century displaying silver mining history.",
# "website": "https://cms-kh.cz/en/",
# "hours_popular": "10:00 AM - 6:00 PM",
# "distance": "10 minutes walk from city center",
# "real_price": "90 CZK"
# },
# {
# "city": "Kutna Hora",
# "name": "Hrádek - Czech Museum of Silver",
# "latitude": 49.766667,
# "longitude": 15.283333,
# "photos": ["https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Kutn%C3%A1\_Hora%2C\_Hr%C3%A1dek*-*Czech\_museum\_of\_silver%2C\_castle\_01.jpg/1920px-Kutn%C3%A1\_Hora%2C\_Hr%C3%A1dek*-*Czech\_museum\_of\_silver%2C\_castle\_01.jpg"],
# "review_score": 4.4,
# "description": "Gothic castle housing a branch of the Czech Museum of Silver focused on medieval mining.",
# "website": "https://cms-kh.cz/en/places/hradek/",
# "hours_popular": "10:00 AM - 6:00 PM",
# "distance": "2 km from city center",
# "real_price": "90 CZK"
# },
# {
# "city": "Kutna Hora",
# "name": "Stone House",
# "latitude": 49.765556,
# "longitude": 15.267222,
# "photos": ["https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Kutn%C3%A1\_Hora%2C\_Kamenn%C3%BD\_d%C5%AFm*-*panoramio.jpg/1280px-Kutn%C3%A1\_Hora%2C\_Kamenn%C3%BD\_d%C5%AFm*-\_panoramio.jpg"],
# "review_score": 4.5,
# "description": "The Stone House is an old burgher house from the 14th century made from stones instead of wood.",
# "website": "http://infocentrum.kutnahora.cz/en/stone-house/",
# "hours_popular": "10:00 AM - 5:00 PM",
# "distance": "In city center",
# "real_price": "90 CZK"
# },
# {
# "city": "Kutna Hora",
# "name": "Saint James Church",
# "latitude": 49.764722,
# "longitude": 15.265556,
# "photos": ["https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Kutn%C3%A1\_Hora%2C\_kostel\_sv.*Jakuba%2C\_pr%C5%AF%C4%8Del%C3%AD*-\_panoramio.jpg/1920px-Kutn%C3%A1\_Hora%2C\_kostel\_sv.*Jakuba%2C\_pr%C5%AF%C4%8Del%C3%AD*-\_panoramio.jpg"],
# "review_score": 4.5,
# "description": "St. James' Church is a Gothic church dedicated to Saint James the Greater located in the city center.",
# "website": "https://www.khfarnost.cz/en/st-james-church/",
# "hours_popular": "10:00 AM - 5:00 PM",
# "distance": "In city center",
# "real_price": "free"
# },
# {
# "city": "Kutna Hora",
# "name": "Kutna Hora Town Hall and Dačický House",
# "latitude": 49.765833,
# "longitude": 15.267222,
# "photos": ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Vla%C5%A1sk%C3%BD\_dv%C5%AFr\_a\_radnice\_v\_Kutn%C3%A9\_Ho%C5%99e.jpg/1920px-Vla%C5%A1sk%C3%BD\_dv%C5%AFr\_a\_radnice\_v\_Kutn%C3%A9\_Ho%C5%99e.jpg"],
# "review_score": 4.4,
# "description": "Historic town hall complex with Gothic and Renaissance architecture.",
# "website": "http://infocentrum.kutnahora.cz/en/town-hall/",
# "hours_popular": "10:00 AM - 6:00 PM",
# "distance": "In city center",
# "real_price": "90 CZK"
# }
# ])
#     return 'ok'
    




#     def extract_city_data(city_with_country):
#         for city_data in city_with_country:
#             country = city_data["country"]
#             city = city_data["city_name"]
#             description = city_data["description"]
#             latitude = city_data["latitude"]
#             longitude = city_data["longitude"]
#             try:
#                 existing_country = Country.objects.filter(name=country).first()
#                 country_id = existing_country.id
#             except:
#                 print("Country does not exist")
#             if not existing_country:
#                 query_for_country = Country(name=country)
#                 query_for_country.save()
#                 country_id = query_for_country.id
#             existing_city = City.objects.filter(city=city).first()

#             if not existing_city:
#                 city_query = City(
#                     country_id=country_id,
#                     city=city,
#                     latitude=latitude,
#                     longitude=longitude,
#                     description=description,
#                 )
#                 city_query.save()
#                 print('save success')
#     extract_city_data(city_with_country =[ {
#         "country": "India",
#         "city_name": "Pune",
#         "latitude": 18.5204,
#         "longitude": 73.8567,
#         "description": "Pune is a city in western India known for its educational institutions, historical landmarks, and cultural heritage."
#     },
#      {
#         "country": "India",
#         "city_name": "Jaipur",
#         "latitude": 26.9124,
#         "longitude": 75.7873,
#         "description": "Jaipur is the capital city of the Indian state of Rajasthan, famous for its rich history, magnificent palaces, and vibrant culture."
#     },
#      {
#         "country": "Japan",
#         "city_name": "Tokyo",
#         "latitude": 35.6895,
#         "longitude": 139.6917,
#         "description": "Tokyo is the capital and largest city of Japan, known for its bustling urban atmosphere, cutting-edge technology, and traditional temples."
#     },
#      {
#         "country": "Japan",
#         "city_name": "Yokohama",
#         "latitude": 35.4437,
#         "longitude": 139.638,
#         "description": "Yokohama is a city in Kanagawa Prefecture, located near Tokyo. It is known for its scenic waterfront, diverse food scene, and historic sites."
#     },
#     {
#         "country": "Japan",
#         "city_name": "Osaka",
#         "latitude": 34.6937,
#         "longitude": 135.5023,
#         "description": "Osaka is a major city in Japan's Kansai region, recognized for its modern architecture, vibrant street life, and renowned food culture."
#     },
#      {
#         "country": "Japan",
#         "city_name": "Nagoya",
#         "latitude": 35.1815,
#         "longitude": 136.9066,
#         "description": "Nagoya is the largest city in the Chubu region of Japan. It is known for its automotive industry, historical landmarks, and cultural attractions."
#     },
#      {
#         "country": "Japan",
#         "city_name": "Sapporo",
#         "latitude": 43.0621,
#         "longitude": 141.3544,
#         "description": "Sapporo is the capital city of Hokkaido's northernmost island. It is famous for its annual snow festival, ski resorts, and beer."
#     },
#      {
#         "country": "Japan",
#         "city_name": "Fukuoka",
#         "latitude": 33.5904,
#         "longitude": 130.4017,
#         "description": "Fukuoka is a vibrant city in southern Japan, renowned for its ancient temples, bustling shopping districts, and Hakata ramen."
#     },
#      {
#         "country": "Japan",
#         "city_name": "Kyoto",
#         "latitude": 35.0116,
#         "longitude": 135.7681,
#         "description": "Kyoto is a historic city in Japan known for its well-preserved temples, traditional wooden houses, and serene Zen gardens."
#     },
#      {
#         "country": "Japan",
#         "city_name": "Hiroshima",
#         "latitude": 34.3853,
#         "longitude": 132.4553,
#         "description": "Hiroshima is a city in southwestern Japan, famously associated with the tragic event of the atomic bombing in 1945. It now stands as a symbol of peace and reconciliation."
#     },
#      {
#         "country": "Spain",
#         "city_name": "Barcelona",
#         "latitude": 41.3851,
#         "longitude": 2.1734,
#         "description": "Barcelona is a vibrant city in northeastern Spain, known for its unique architecture, lively street life, and beautiful Mediterranean beaches."
#     },
#      {
#         "country": "Spain",
#         "city_name": "Valencia",
#         "latitude": 39.4699,
#         "longitude": -0.3763,
#         "description": "Valencia is a coastal city in eastern Spain, famous for its futuristic City of Arts and Sciences, delicious paella, and lively festivals."
#     },
#      {
#         "country": "Spain",
#         "city_name": "Seville",
#         "latitude": 37.3891,
#         "longitude": -5.9845,
#         "description": "Seville is the capital city of the Andalusia region in southern Spain, renowned for its stunning Moorish architecture, flamenco music, and vibrant street culture."
#     },
#      {
#         "country": "Spain",
#         "city_name": "Malaga",
#         "latitude": 36.7213,
#         "longitude": -4.4214,
#         "description": "Malaga is a city on Spain's Costa del Sol, known for its beautiful beaches, ancient ruins, and being the birthplace of renowned artist Pablo Picasso."
#     },
#      {
#         "country": "Spain",
#         "city_name": "Bilbao",
#         "latitude": 43.263,
#         "longitude": -2.935,
#         "description": "Bilbao is a city in northern Spain, famous for its avant-garde architecture, including the iconic Guggenheim Museum, as well as its rich Basque culture and cuisine."
#     },
#      {
#         "country": "Spain",
#         "city_name": "Granada",
#         "latitude": 37.1773,
#         "longitude": -3.5986,
#         "description": "Granada is a city in southern Spain, renowned for its stunning Alhambra palace, Moorish heritage, and vibrant flamenco scene."
#     },
#      {
#         "country": "Spain",
#         "city_name": "Alicante",
#         "latitude": 38.3452,
#         "longitude": -0.481,
#         "description": "Alicante is a coastal city in southeastern Spain, known for its beautiful beaches, historic castle, and lively promenade, the Explanada de España."
#     },
#      {
#         "country": "Spain",
#         "city_name": "Zaragoza",
#         "latitude": 41.6488,
#         "longitude": -0.8891,
#         "description": "Zaragoza is a city in northeastern Spain, renowned for its rich historical heritage, including the Basilica of Our Lady of the Pillar and the Aljafería Palace."
#     }
# ]
# )


    

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
    