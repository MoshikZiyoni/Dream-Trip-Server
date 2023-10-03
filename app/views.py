from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import process_city, run_long_poll_async
from app.models import ApplicationRating ,QueryChatGPT,Popular,City,Attraction,Restaurant, UserTrip, Users
from django.core.cache import cache
from app.utils import quick_from_data_base
import traceback
import re
from django.db.models import Q
import random
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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

geolocator = Nominatim(user_agent="dream-trip")

@api_view(['GET', 'POST'])
def gpt_view(request):

    email=request.data['email']
    if not email:
        return JsonResponse({'error': 'Email not provided'})
    request_left = user_requests_cache(email)

    try:

        # Define variables
        mainland = request.data['country']  
        print("mainland:",mainland)
        # adult = request.data['adult']
        # children = request.data['children']
        durring = request.data['durringDays']
        question1 = '{"country": "..", "cities": [{"city": "", "description": "", "days_spent": "" }], "itinerary-description": ""}'
        ourmessage=f"Please suggest a round trip itinerary starting and ending at point A in {mainland}, considering {durring} available days. If {durring} is 3 or less, provide an itinerary with a single city. Ensure a minimum stay of 3 days in each city. Return the itinerary in the following JSON structure:{question1}"
        answer_from_data = QueryChatGPT.objects.filter(question__exact=ourmessage).values('answer','id').first()
        if answer_from_data:
            print('answer in data')
            trip_id=answer_from_data['id'] 
            answer_string = answer_from_data['answer']   
            country = mainland
            answer=(quick_from_data_base(country=country,answer_dict=answer_string,request_left=request_left,trip_id=trip_id))
            return JsonResponse(answer,safe=False)
           
        
        result1=(run_long_poll_async(ourmessage,mainland))
        combined_data = result1['answer']
        itinerary_description1 =result1['itinerary_description']
        costs=result1['costs']
        trip_id=result1['trip_id']
        

        result1={
            "answer":combined_data,
            "itinerary_description":itinerary_description1,
            "request_left":request_left,
            "trip_id":trip_id
            
        }
        result1.update(costs)
        return  JsonResponse(result1,safe=False)
    except Exception as e:
        print(f'error: {e}')
        traceback.print_exc() 
        return  Response("An error occurred while processing your request.")
    



@api_view(['GET', 'POST'])
def popular_country(request):
    country_names=Popular.objects.all().values()
    country_names=list(country_names)
    return JsonResponse(country_names,safe=False)



@api_view(['GET', 'POST'])
def make_short_trip(request): 
    email=request.data['email']
    if not email:
        return JsonResponse({'error': 'Email not provided'})
    request_left = user_requests_cache(email)

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
    trip_id=(random_query.id)
    print (trip_id)
    new_result=(quick_from_data_base(country=country,answer_dict=answer,request_left=request_left,trip_id=trip_id))
    return JsonResponse(new_result,safe=False)


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
    if ApplicationRating.objects.get(user_email=email):
        return JsonResponse(True,safe=False)
    else:
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
                        'city':country,
                        'days': first_number,
                        'start_trip':trip_id['start_trip'],
                        'end_trip':trip_id['end_trip'],
                        'created_at':trip_id['created_at']
                    })
            else:
                print("No number found in the question.")

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
            print("not inside")
            # Add the new trip to liked trips
            UserTrip(liked_trips=trip_id,user_id=user,end_trip=end_trip,start_trip=start_trip).save()
            # user_trip.save()

            return Response({"message": f"Trip added to liked trips for email: {email}"})
        else:
            return Response({"message": f"Trip already exists in liked trips for email: {email}"})
    except Users.DoesNotExist:
        # If the UserTrip for the user doesn't exist, we create a new one
        Users(email=email).save()
        user = Users.objects.get(email=email)
        user_trip = UserTrip(user_id=user, liked_trips=trip_id,end_trip=end_trip,start_trip=start_trip)
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
            trip_to_delete=UserTrip.objects.get(liked_trips=trip_id)
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
    trip_id=int(request.data['trip_id'])
    request_left = user_requests_cache(email)
    request_left+=1    
    trip=QueryChatGPT.objects.get(id=trip_id)
    if trip:
            print('answer in data') 
            answer_string = trip.answer
            question=trip.question   
            country_match = re.search(r'in (\w+),', question)
            # Check if a match was found
            if country_match:
                country = country_match.group(1)  # Get the matched text and remove leading/trailing spaces
            print("Country:", country)
            answer=(quick_from_data_base(country=country,answer_dict=answer_string,request_left=request_left,trip_id=trip_id))
            return JsonResponse(answer,safe=False)







def user_requests_cache(email):
     # Check if the user's email exists in the request count dictionary
    request_count = cache.get(email, 0)
    # If the user has made more than 10 requests in the past 24 hours, block the request
    if request_count >= 100:
        return JsonResponse({'error': 'Too many requests'})

    # Otherwise, increment the request count and set the cache with the new value
    request_count += 1
    print (request_count)
    request_left=11-request_count
    timeout_seconds = 24 * 60 * 60  # 24 hoursin seconds
    cache.set(email, request_count, timeout=timeout_seconds)
    return request_left