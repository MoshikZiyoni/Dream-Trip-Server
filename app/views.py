from django.shortcuts import render
from django.http import JsonResponse
from app.tasks import run_gpt_func

def gpt_view(request):
    question2='{"country":"..","cities":[{"city":,"description":,"attractions":["name":]["descrpition":],"travelDay":}]}'
    ourmessage=f"provide me a Trip to {request.data['mainland']} ,for {request.data['travelers']} trip,budget {request.data['budget']} {request.data['durring']},put the answer in the following JSON structure {question2}"
    run_gpt_func.delay(ourmessage)
    return JsonResponse({"message": "Task started in the background."})