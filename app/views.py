import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import process_city, run_long_poll_async
from app.models import Attraction, Country, QueryChatGPT,City, Restaurant
from django.core.cache import cache
from app.my_selenium import perform_search
from app.trip_advisor import flickr_api, foursquare_attraction, foursquare_hotels, foursquare_restaurant
from app.utils import extract_attraction_data, extract_restaraunt_data, generate_schedule, process_attraction, process_hotel, process_restaurant, quick_from_data_base
import traceback
import re
from django.db.models import Q
import random
import os
import requests
@api_view(['GET', 'POST'])
def gpt_view(request):

    
    # from django.db.models import Count
    # cities_without_hotels = City.objects.filter(hotels__isnull=True)

    # for city in cities_without_hotels:
    #     print(city.city)
    #     try:
    #         landmarks=[city.latitude,city.longitude]
    #         result=foursquare_hotels(landmarks)
    #         hotels= []
    #         if len(result) == 0:
    #             continue
    #         for hotel in result:
    #             process_hotel(hotel=hotel, city_obj=city, hotels=hotels)    
    #     except Exception as e:
    #         print ('NOT GOOOODDDDDDDDDDDDDDDDDD',e)

    # return 'ok'



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


#     def qiuick_attraction+restarunt(cities_data):
#         for data in cities_data:
#                 country= (data['country'])
#                 try:
#                     existing_country = Country.objects.filter(name=country).first()
#                     country_id = existing_country.id
#                 except:
#                     print ('country not exist')
#                     country_query=Country(name=country)
#                     country_query.save()
#                     existing_country = Country.objects.filter(name=country).first()
#                     country_id = existing_country.id
#                     print (country_id)
                
#                 city=data['city']
#                 latitude=data['latitude']
#                 longitude=data['longitude']
#                 landmarks=[latitude,longitude]
#                 description=data['description']
#                 city_obj=City.objects.filter(city=city).first()
#                 if city_obj:
#                     print ('continue')
#                     continue
#                     try:
#                         result1=foursquare_attraction(city_name=city,landmarks=landmarks,country=country)
#                         attractions=[]
#                     except:
#                         print ('no attraction')
#                     try:
#                         for attrac in result1:
#                             process_attraction(attrac, city_obj, attractions)
#                     except:
#                         print ('no attraction1')
#                     try:
#                         result=foursquare_restaurant(landmarks)
#                         for resta in result:
#                             restaurants=[]
#                             process_restaurant(resta,city_obj,restaurants)
#                     except:
#                         print ('no restarunt')
#                 else:
#                     city_query = City(
#                     country_id=country_id,
#                     city=city,
#                     latitude=latitude,
#                     longitude=longitude,
#                     description=description,
#                 )
#                     city_query.save()
#                     print("Save successfully for city")
#                     try:
#                         result1=foursquare_attraction(city_name=city,landmarks=landmarks,country=country)
#                         attractions=[]
#                     except:
#                         print ('no attraction')
#                     try:
#                         for attrac in result1:
#                             process_attraction(attrac, city_obj, attractions)
#                     except:
#                         print ('no attraction1')
#                     try:
#                         result=foursquare_restaurant(landmarks)
#                         for restaur in result:
#                             restaurants=[]
#                             process_restaurant(restaur,city_obj,restaurants)
#                     except:
#                         print ('no restarunt')



#     qiuick_attraction(cities_data = [
#  ])
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
#                 # name=name,
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
#             city_objs = City.objects.filter(id=308).first()
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
#    {
#         "city": "Fernando de Noronha", 
#         "name": "Restaurante Cuscuz",
#         "latitude": -3.853056,
#         "longitude": -32.422222,
#         "photos": ["https://media-cdn.tripadvisor.com/media/photo-s/0d/6c/5b/0b/restaurante-cuscuz.jpg"],
#         "review_score": 5.0,
#         "website": "",
#         "distance": "In town",
#         "price": 2
#     },
#     {
#         "city": "Fernando de Noronha",
#         "name": "Restaurante Doce de Noronha",
#         "latitude": -3.852222,
#         "longitude": -32.422889,
#         "photos": ["https://media-cdn.tripadvisor.com/media/photo-s/11/f0/50/f8/photo3jpg.jpg"],
#         "review_score": 5.0,
#         "website": "",
#         "distance": "In town",
#         "price": 2
#     },
#     {
#         "city": "Fernando de Noronha",
#         "name": "Pizzaria Namoita",
#         "latitude": -3.853194,
#         "longitude": -32.42225,
#         "photos": ["https://media-cdn.tripadvisor.com/media/photo-s/11/f0/50/ef/photo0jpg.jpg"],
#         "review_score": 4.5,
#         "website": "",
#         "distance": "In town",
#         "price": 2
#     },
#     {
#         "city": "Fernando de Noronha",
#         "name": "Restaurante Teca",
#         "latitude": -3.853333,
#         "longitude": -32.422778,
#         "photos": ["https://media-cdn.tripadvisor.com/media/photo-f/18/99/60/a7/photo2jpg.jpg"],
#         "review_score": 4.0,
#         "website": "",
#         "distance": "In town",
#         "price": 2
#     },
#     {
#         "city": "Fernando de Noronha",
#         "name": "Pousada Maravilha - Restaurante",
#         "latitude": -3.855,
#         "longitude": -32.425278,
#         "photos": ["https://media-cdn.tripadvisor.com/media/photo-s/06/72/8f/83/pousada-maravilha.jpg"],
#         "review_score": 4.5,
#         "website": "",
#         "distance": "1 km from town",
#         "price": 3
#     },
#     {
#         "city": "Fernando de Noronha",
#         "name": "Restaurante Zé Maria",
#         "latitude": -3.853333,
#         "longitude": -32.422889,
#         "photos": ["https://media-cdn.tripadvisor.com/media/photo-w/19/6c/c0/bb/ze-maria.jpg"],
#         "review_score": 4.5,
#         "website": "",
#         "distance": "In town",
#         "price": 3  
#     },
#     {
#         "city": "Fernando de Noronha",
#         "name": "Restaurante Cachorro Velho",
#         "latitude": -3.852778,
#         "longitude": -32.422889,
#         "photos": ["https://media-cdn.tripadvisor.com/media/photo-s/0d/6c/5b/18/restaurante-cachorro-velho.jpg"],
#         "review_score": 4.5,
#         "website": "",
#         "distance": "In town",
#         "price": 2
#     },
#     {
#         "city": "Fernando de Noronha",
#         "name": "Picolé Café",
#         "latitude": -3.853333,
#         "longitude": -32.423889,
#         "photos": ["https://b.zmtcdn.com/data/reviews_photos/347/a27d3f28f3cb450d6d233adb43834347_1504710550.jpg"],
#         "review_score": 4.5,
#         "website": "",
#         "distance": "In town",
#         "price": 1
#     },
#     {
#         "city": "Fernando de Noronha",
#         "name": "Empório Sushi",
#         "latitude": -3.855,
#         "longitude": -32.4227778,
#         "photos": ["https://media-cdn.tripadvisor.com/media/photo-s/11/f7/a1/5e/sushi.jpg"],
#         "review_score": 4.5,
#         "website": "",
#         "distance": "In town",
#         "price": 3  
#     },
#     {
#         "city": "Fernando de Noronha",
#         "name": "Restaurante Natureza",
#         "latitude": -3.8508333,
#         "longitude": -32.4236111,
#         "photos": ["https://media-cdn.tripadvisor.com/media/photo-s/06/72/8f/7e/natureza.jpg"],
#         "review_score": 4.0,
#         "website": "",
#         "distance": "1 km from town",
#         "price": 2
#     }
# ])
# #     return 'ok'


    # def city_has_few_attractions():
    #     cities_with_few_attractions = []

    #     # Get all cities and their attraction count using the Django ORM
    #     cities = City.objects.all()

    #     for city in cities:
    #         # Count the number of attractions for each city
    #         attraction_count = city.attractions.count()

    #         # Check if the city has fewer than 10 attractions
    #         if attraction_count < 10:
    #             cities_with_few_attractions.append(city.city)

    #     return cities_with_few_attractions
    # print(city_has_few_attractions())
    # return 'ko'


    # from django.db.models import Count

    # Get the cities without attractions
    # cities_without_attractions = City.objects.annotate(num_attractions=Count('attractions')).filter(num_attractions=0)
    # cities_without_hotels=City.objects.annotate(num_hotels=Count('hotels')).filter(num_hotels=0)
    # for city in cities_without_hotels:
    #     print(city.city)
    # return 'ok'

    # # # Get the cities without restaurants
    # cities_without_restaurants = City.objects.annotate(num_restaurants=Count('restaurants')).filter(num_restaurants=0)

    # # Print the results
    # print("Cities without attractions:")
    # for city in cities_without_attractions:
    #     print(city.city,city.id,',')
    # attrac=Attraction.objects.filter(city_id=345).values()
    # for i in attrac:
    #     print(i)
    # return 'ok'
    # print("Cities without restaurants:")
    # for city in cities_without_restaurants:
    #     print(city.city,city.id,',')

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
            country = answer_dict["country"]
            answer=(quick_from_data_base(country=country,answer_dict=answer_string,process_city=process_city))
            answer=answer,{"request_left":request_left}
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

        return  JsonResponse(result1,safe=False)
    except Exception as e:
        print(f'error: {e}')
        traceback.print_exc() 
        return  Response("An error occurred while processing your request.")
    



@api_view(['GET', 'POST'])
def popular_country(request):
    top_countries = Country.objects.order_by('-popularity_score')[:6]
    country_names = []
    for country in top_countries:
        url = 'https://pixabay.com/api/'
        params = {'key':os.environ.get('pixabay_key'),'q':{country.name},'image_type':'landscape','orientation':'landscape'}

        response = requests.get(url, params=params)
        data = response.json()
        image_url = data['hits'][0]['largeImageURL']
        
        country_pair = [country.name, image_url]
        country_names.append(country_pair)
    return JsonResponse(country_names,safe=False)



@api_view(['GET', 'POST'])
def make_short_trip(request): 
    country=(request.data["country"])
    queries = QueryChatGPT.objects.filter(
            Q(question__icontains=country)     
        )
    
    pattern = r'\b(?:[7-9]|[1-2][0-9]|3[0-5])\b'
    result = []
    for query in queries:
        matches = re.findall(pattern, query.question)
        if matches:
            result.append(query)
        else:
            continue

    if result is not None:
        random_query=random.choice(result)
    else:
        random_query=random.choice(queries)
        print ('under 7 days')
    answer=(random_query.answer)
    new_result=(quick_from_data_base(country=country,answer_dict=answer,process_city=process_city))
    return JsonResponse(new_result,safe=False)