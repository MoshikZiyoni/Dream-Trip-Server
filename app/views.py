from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import run_long_poll_async
from app.models import QueryChatGPT,City
from django.core.cache import cache
import json


@api_view(['GET', 'POST'])
def gpt_view(request):

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
        city_data = {}

        # Define variables
        mainland = request.data['mainland']
        travelers = request.data['travelers']
        budget = request.data['budget']
        durring = request.data['durring']
        question1 = '{"country": "..", "cities": [{"city": "", "description": "", "attractions": [{"name": "", "description": ""}],landmarks:[latitude,longitude], "travelDay": }]}'
        ourmessage=f"Create a {budget} {durring} {travelers} trip to {mainland} in the following JSON structure:{question1}"
        # ourmessage = f"provide me a Trip to {mainland}, for a {travelers} trip,have a budget {budget} plan to stay for {durring}, put the answer in the following JSON structure {question1}"
        answer_from_data = QueryChatGPT.objects.filter(question__exact=ourmessage).values('answer').first()
        if answer_from_data:
            print('answer in data')
            data = json.loads(answer_from_data['answer'])
            # Extract all city names
            cities = [city['city'] for city in data['cities']]
            for city in cities:
                city_object = City.objects.filter(city=city).first()

                if city_object:
                    latitude = city_object.latitude
                    longitude = city_object.longitude

                    # Add city data to the dictionary
                    city_data[city] = {'latitude': latitude, 'longitude': longitude}
                else:
                    print(f"City data not found for: {city}")            
            
            print (city_data)
            answer=({'answer' :answer_from_data['answer'],"request_left":request_left,'city_data':city_data})
            return Response(answer)
        
        result1=(run_long_poll_async(ourmessage))
        
        result1=result1,{"request_left":request_left}
        print (result1)

        return  JsonResponse(result1,safe=False)
    except Exception as e:
        print(f'error: {e}')
        return  Response("An error occurred while processing your request.")
    