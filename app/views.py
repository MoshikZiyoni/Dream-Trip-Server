from django.shortcuts import render
from django.http import JsonResponse
from app.task2 import run_gpt_func
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def gpt_view(request):
    question2='{"country":"..","cities":[{"city":,"description":,"attractions":["name":]["descrpition":],"travelDay":}]}'
    ourmessage=f"provide me a Trip to {request.data['mainland']} ,for {request.data['travelers']} trip,budget {request.data['budget']} {request.data['durring']},put the answer in the following JSON structure {question2}"
    result = run_gpt_func(ourmessage)
    
    
    return JsonResponse(result,safe=False)