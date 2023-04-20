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
            return Response(answer, status=status.HTTP_200_OK)
        else:
            print('Not Found')
            
    except:
        print ('Internal Server Error')
    query = QueryChatGPT()
    query.question = ourmessage
    query.save()
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.environ.get('API_KEY')
##

    

    response=openai.Completion.create(
        model="text-davinci-003",
        prompt=ourmessage,
        max_tokens=700,
        temperature=0.9
        )
    ourdata=response.choices[-1]['text']
    query.answer = ourdata
    query.save()
    return JsonResponse(ourdata,safe=False)
