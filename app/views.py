import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import run_long_poll_async
from app.models import Attraction, Country, QueryChatGPT,City, Restaurant
from django.core.cache import cache
# from threading import Thread
# from app.wikipediaapi import process_query



@api_view(['GET', 'POST'])
def gpt_view(request):
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
            answer=({'answer' :answer_from_data['answer'],"request_left":request_left})
            return Response(answer)
        
        result1=(run_long_poll_async(ourmessage))
        
        result1=result1,{"request_left":request_left}

        return  JsonResponse(result1,safe=False)
    except Exception as e:
        print(f'error: {e}')
        return  Response("An error occurred while processing your request.")
    