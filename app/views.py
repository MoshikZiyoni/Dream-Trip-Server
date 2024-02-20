from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from app.chat import run_long_poll_async
from app.models import ApplicationRating ,QueryChatGPT,Popular,City,Attraction,Restaurant, UserTrip, Users,Country
from django.core.cache import cache
from app.utils import quick_from_data_base
import traceback
import re
from django.db.models import Q
import random
import json
# from rest_framework.authtoken.models import Token
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
from datetime import date
# from collections import Counter
# from django.db.models import Count
# from itertools import combinations
# from django.db.models.functions import Lower
# from selenium.webdriver.common.by import By
# import base64
# import requests
# from selenium import webdriver
# import os
# import ast
from geopy.geocoders import Nominatim
import base64
import json
import os
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from unidecode import unidecode
from rest_framework.decorators import api_view
from selenium import webdriver
from app.models import Attraction,City
import random
import time
import requests
import re
from selenium.webdriver.common.by import By
from django.db.models import Q
from geopy.geocoders import Nominatim
import math
from geopy.distance import geodesic
from dotenv import load_dotenv



@api_view(['GET', 'POST'])
def gpt_view(request):
    

   
#     for item in average_meal_costs:
#         country = Country.objects.get(name=item['country'])
#         country.average_food = item['cost']
#         country.save()
#     return 'k'  

    # resta=Restaurant.objects.filter(city_id=366).values()
    
    
    # for i in resta:
    #     print (i['name'])
    #     print (i['category'])
    #     # if len(i.category)==0:
    #     #     with open('my_list.txt', 'a', encoding='utf-8') as f:
    #     #         data_to_write = f"restaurts_name: ', {i.name}, 'city_name: ',{i.city.city}\n"
    #     #         f.write(data_to_write)
            
            
    # return 'kk'


    # cities_without_hotels = City.objects.filter(attractions__isnull=True)

    # for city in cities_without_hotels:
    #     print(city.country.name, city.city)
    #     # try:
    #     #     landmarks=[city.latitude,city.longitude]
    #     #     result=foursquare_hotels(landmarks)
    #     #     hotels= []
    #     #     if len(result) == 0:
    #     #         continue
    #     #     for hotel in result:
    #     # #         process_hotel(hotel=hotel, city_obj=city, hotels=hotels)    
    #     # except Exception as e:
    #     #     print ('NOT GOOOODDDDDDDDDDDDDDDDDD',e)

    # return 'ok'
   
    email=request.data['email']
    if not email:
        return JsonResponse({'error': 'Email not provided'})
    request_left = user_requests_cache(email)
    try:
        if request_left==False:
            return JsonResponse({'error': 'Too many requests'})    
    except:
        pass
    

    try:

        # Define variables
        mainland = request.data['country']  
        print("mainland:",mainland)
        # adult = request.data['adult']
        # children = request.data['children']
        durring = request.data['durringDays'] 
        print(durring)       
        if durring>30:
            response_data = {
            'error': 'Too many days.'
        }
            return JsonResponse(response_data,status=404 , safe=False)
        question1 = '{"country": "..", "cities": [{"city": "", "description": "", "days_spent": "" }], "itinerary-description": ""}'
        ourmessage=f"Please suggest a round trip itinerary starting and ending at point A in {mainland}, considering {durring} available days. If {durring} is 3 or less, provide an itinerary with a single city. Ensure a minimum stay of 3 days in each city. Return the itinerary in the following JSON structure:{question1}"
        answer_from_data = QueryChatGPT.objects.filter(question__exact=ourmessage).values('answer','id').first()
        if answer_from_data:
            print('answer in data')
            trip_id=answer_from_data['id']
            answer_string = answer_from_data['answer']   
            country = mainland
            cache_key = f"Trip_{trip_id}"
            cache_trip_id=cache.get(cache_key)
            if cache_trip_id is None:
                answer=(quick_from_data_base(country=country,answer_dict=answer_string,request_left=request_left,trip_id=trip_id,durring=durring))
                cache.set(cache_key, answer, timeout=7 * 24 * 60 * 60)
                return JsonResponse(answer,safe=False)
            else:
                print ('answr cache')
                return JsonResponse(cache_trip_id,safe=False)

        
        result1=(run_long_poll_async(ourmessage,mainland,durring))
        combined_data = result1['answer']
        itinerary_description1 =result1['itinerary_description']
        costs=result1['costs']
        trip_id=result1['trip_id']
        

        result1={
            "answer":combined_data,
            "itinerary_description":itinerary_description1,
            "request_left":request_left,
            "trip_id":trip_id,
            "days":durring
            
        }
        result1.update(costs)
        return  JsonResponse(result1,safe=False)
    except Exception as e:
        print(f'error: {e}')
        traceback.print_exc() 
        return  Response("An error occurred while processing your request.")
    


@cache_page(36000)
@api_view(['GET', 'POST'])
def popular_country(request):
    cache_key = f"popular"
    popular = cache.get(cache_key)
    if popular is None:
        country_names=Popular.objects.all().values()
        country_names=list(country_names)
        cache.set(cache_key, country_names, timeout=7 * 24 * 60 * 60)
        return JsonResponse(country_names,safe=False)
    else:
        print ('cache')
        return JsonResponse(popular,safe=False)

# cache_key = f"query{query.question}"
#         cache_for_query = cache.get(cache_key)
#         if cache_for_query is None:

@api_view(['GET', 'POST'])
def make_short_trip(request): 
    email=request.data['email']
    if not email:
        return JsonResponse({'error': 'Email not provided'})
    request_left = user_requests_cache(email)
    try:
        if request_left==False:
            return JsonResponse({'error': 'Too many requests'})    
    except:
        pass
    country=(request.data["country"])
    queries = QueryChatGPT.objects.filter(
            Q(question__icontains=country)     
        )
    
    pattern = r'\b(?:[7-9]|[1-2][0-9]|3[0-5])\b'
    # Use re.search to find the first match of the pattern in the question
    result = []
    for query in queries:
        days_match = re.search(r'\b\d+\b', query.question)
        if days_match:
                first_number = int(days_match.group())
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
    trip_id=(random_query.id)
    print (trip_id)
    cache_key = f"trip-id{trip_id}"
    short_trip_cache = cache.get(cache_key)
    if short_trip_cache is None:
        new_result=(quick_from_data_base(country=country,answer_dict=answer,request_left=request_left,trip_id=trip_id,durring=first_number))
        days={"days":first_number}
        new_result.update(days)
        cache.set(cache_key, new_result, timeout=7 * 24 * 60 * 60)
        return JsonResponse(new_result,safe=False)
    else:
        print('short_trip_cache')
        return (JsonResponse(short_trip_cache,safe=False))


@api_view(['GET', 'POST'])
def out_applaction_score(request):
    score=request.data['score']
    email=request.data['email']
    name=request.data['name']
    photo=request.data['picture'] if request.data['picture'] else ''
    review=request.data['review'] if request.data['review'] else ''
    rating_to_save=ApplicationRating(rating=score,user_email=email,user_name=name,user_picture=photo,review=review)
    rating_to_save.save()
    return JsonResponse('success',safe=False)


@api_view(['GET','POST'])
def check_before_rate(request):
    email=request.data['email']
    try:
         check=ApplicationRating.objects.filter(user_email=email)
         if check:
            print ('True')
            return JsonResponse(True,safe=False)
    except:
        print ('False')
        return JsonResponse(False,safe=False)


@api_view(['POST'])
def user_trip(request):
    try:
        trip_details = []
        email = request.data.get('email')
        _user=Users.objects.get(email=email)
        trips = _user.usertrip.all().values()
        print(trips)
            
        for trip_id in trips:
            trip=QueryChatGPT.objects.get(id=trip_id['liked_trips'])
            question=trip.question
            itinerary_description=trip.itinerary_description
            pattern = r'\b\d+\b'
            # Use re.search to find the first match of the pattern in the question
            days_match = re.search(pattern, question)
            country_match = re.search(r'in (\w+),', question)

            # Check if a match was found
            if country_match:
                country = country_match.group(1)  # Get the matched text and remove leading/trailing spaces
                print("Country:", country)
            else:
                print("No country name found in the question.")
            # Check if a match was found
            if days_match:
                first_number = int(days_match.group())  # Convert the matched text to an integer
                trip_details.append({
                'country':country,
                'days': first_number,
                'start_trip':trip_id['start_trip'],
                'end_trip':trip_id['end_trip'],
                'created_at':trip_id['created_at'],
                'trip_id':trip_id['id']
                 })
                       
            else:
                print("No number found in the question.")
        print (trip_details)
        return JsonResponse(trip_details,safe=False)
    except:
        return JsonResponse("You don't have trips yet",safe=False)


@api_view(['POST'])
def user_add_trip(request):
    # UserTrip.objects.all().delete()
    email = request.data.get('email')
    end_trip = str(request.data.get('end_trip'))
    start_trip = str(request.data.get('start_trip'))
    trip_id = str(request.data.get('trip_id'))
       

        # Check if the user has any existing liked trips
    try:
            # Check if the user exists
        user = Users.objects.get(email=email)
        user_trip = UserTrip.objects.filter(user_id=user).values('liked_trips')
        liked_trips_list = [entry['liked_trips'] for entry in user_trip]
        if trip_id not in liked_trips_list:
            # Add the new trip to liked trips
            user_trip1=UserTrip(liked_trips=trip_id,user_id=user,end_trip=end_trip,start_trip=start_trip)
            user_trip1.created_at=date.today()
            formatted_date = user_trip1.created_at.strftime('%d/%m/%Y')

            # formatted_date =user_trip1.formatted_created_date()
            user_trip1.created_at = formatted_date
            user_trip1.save()
            print("new trip add successfuly")
            return Response({"message": f"Trip added to liked trips for email: {email}"})
        else:
            return Response({"message": f"Trip already exists in liked trips for email: {email}"})
    except Users.DoesNotExist:
        # If the UserTrip for the user doesn't exist, we create a new one
        Users(email=email).save()
        user = Users.objects.get(email=email)
        user_trip = UserTrip(user_id=user, liked_trips=trip_id,end_trip=end_trip,start_trip=start_trip)
        user_trip.created_at=date.today()
        formatted_date = user_trip.created_at.strftime('%d/%m/%Y')

        # formatted_date =user_trip.formatted_created_date()
        user_trip.created_at = formatted_date
        user_trip.save()
        return Response({"message": f"Trip added to liked trips for NEW email: {email}"})

    except Exception as e:
        print(e)
        return Response({"message": f"Trip not saved successfully"})



@api_view(['DELETE'])
def user_delete_trip(request):
    email=request.data['email']
    trip_id=str(request.data['trip_id'])
    try:
        delete_the_user_trip = Users.objects.get(email=email)
        if delete_the_user_trip:
            trip_to_delete=UserTrip.objects.get(id=trip_id)
            if trip_to_delete:
                trip_to_delete.delete()
                return JsonResponse({'message': f'Trip {trip_id} removed from liked trips for email: {email}'})
            else:
                return JsonResponse({'message': f'Trip {trip_id} not found in liked trips for email: {email}'})
    except Users.DoesNotExist:
        return JsonResponse({'error': 'User not found'})



@api_view(['GET','POST'])
def user_single_trip(request):
    email=request.data['email']
    trip_id=(request.data['trip_id'])
    print(trip_id)
    user_trip_id = UserTrip.objects.get(id=trip_id)
    real_trip_id=(user_trip_id.liked_trips)
    request_left = user_requests_cache(email)
    try:
        if request_left==False:
            return JsonResponse({'error': 'Too many requests'})    
    except:
        pass
    request_left+=1    
    trip=QueryChatGPT.objects.get(id=real_trip_id)
    pattern = r'\b\d+\b'
    
    if trip:
            print('answer in data') 
            answer_string = trip.answer
            question=trip.question   
            # Use re.search to find the first match of the pattern in the question
            durring = re.search(pattern, question)
            if durring:
                first_number = int(durring.group())
                print(first_number,'@@@')
            country_match = re.search(r'in (\w+),', question)
            # Check if a match was found
            if country_match:
                country = country_match.group(1)  # Get the matched text and remove leading/trailing spaces
            print("Country:", country)
            answer=(quick_from_data_base(country=country,answer_dict=answer_string,request_left=request_left,trip_id=trip_id,durring=int(first_number)))
            return JsonResponse(answer,safe=False)
    else:
        return JsonResponse('not good',safe=False)


@cache_page(36000)
@api_view(['GET','POST'])
def country_list(request):
    cache_key = f"country_list"
    country_cache=cache.get(cache_key)
    if country_cache is None:
        # email=request.data['email']
        # print(email)
        countries=Country.objects.all()
        countries_list = [country.name for country in countries]
        countries_list.sort()

        cache.set(cache_key, countries_list, timeout=7 * 24 * 60 * 60)
        return JsonResponse(countries_list,safe=False)
    else:
        print ('country_cache')
        return JsonResponse(country_cache,safe=False)




def user_requests_cache(email):
    # Check if the user's email exists in the request count dictionary
    request_count = cache.get(email, 0)
    # If the user has made more than 10 requests in the past 24 hours, block the request
    if int(request_count) == 15:
        return False

    # Otherwise, increment the request count and set the cache with the new value
    request_count += 1
    print(request_count)
    request_left = 11 - request_count
    timeout_seconds = 24 * 60 * 60  # 24 hours in seconds
    cache.set(email, request_count, timeout=timeout_seconds)
    return request_left



