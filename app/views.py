import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import run_long_poll_async
from app.models import QueryChatGPT,City
from django.core.cache import cache
import requests
import os


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

        # Define variables
        mainland = request.data['mainland']
        travelers = request.data['travelers']
        budget = request.data['budget']
        durring = request.data['durring']
        question1 = '{"country": "..", "cities": [{"city": "", "description": "",landmarks:[latitude,longitude], "travelDay": }]}'
        ourmessage=f"Create a {budget} {durring} {travelers} trip to {mainland} in the following JSON structure:{question1}"
        answer_from_data = QueryChatGPT.objects.filter(question__exact=ourmessage).values('answer').first()
        if answer_from_data:
            print('answer in data')
            # parsed_data = json.loads(answer_from_data['answer'])
            # cities_landmarks = [(city['city'], city['landmarks']) for city in parsed_data['cities']]
            
                
            answer=({'answer' :answer_from_data['answer'],"request_left":request_left})
            return Response(answer)
        
        result1=(run_long_poll_async(ourmessage))
        
        result1=result1,{"request_left":request_left}

        return  JsonResponse(result1,safe=False)
    except Exception as e:
        print(f'error: {e}')
        return  Response("An error occurred while processing your request.")
    