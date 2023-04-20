from django.http import JsonResponse
from django.shortcuts import render
import os
import openai
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import QueryChatGPT
from rest_framework import status
import traceback
import time


MAX_RETRIES = 3
WAIT_TIME = 5

@api_view(['GET', 'POST'])
def gpt_func(request):
    question2='{"country":"..","cities":[{"city":,"description":,"attractions":["name":]["descrpition":],"travelDay":}]}'
    ourmessage=f"provide me a Trip to {request.data['mainland']} ,for {request.data['travelers']} trip,budget {request.data['budget']} {request.data['durring']},put the answer in the following JSON structure {question2}"
    # print (ourmessage)
    try:
        answer_from_data=QueryChatGPT.objects.filter(question__exact=ourmessage)
        if answer_from_data.exists():
            data=answer_from_data.values('answer')[0]
            answer = data['answer']
            print ('answer in data')
            return JsonResponse(answer, status=status.HTTP_200_OK,safe=False)
        else:
            print('Not Found')
            
    except:
        print ('Internal Server Error')
    query = QueryChatGPT()
    query.question = ourmessage
    
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.environ.get('API_KEY')
##

    

    try_count = 0
    while try_count < MAX_RETRIES:
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=ourmessage,
                max_tokens=3000,
                temperature=0.9
            )
            ourdata = response.choices[-1]['text']

            query = QueryChatGPT()
            query.question = ourmessage
            query.answer = ourdata
            query.save()

            return JsonResponse(ourdata, safe=False)

        except Exception as e:
            print(f"An error occurred in try {try_count+1}: {e}")
            try_count += 1
            time.sleep(WAIT_TIME)

   
