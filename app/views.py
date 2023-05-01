import json
from concurrent.futures import ThreadPoolExecutor
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai
from app.chat import run_long_poll_async
from app.chat2 import run_long_poll_async1
from app.models import QueryChatGPT
import asyncio

@api_view(['GET', 'POST'])
def gpt_view(request):
    print (request.data)
    try:
        # Define variables
        mainland = request.data['mainland']
        travelers = request.data['travelers']
        budget = request.data['budget']
        durring = request.data['durring']
        question1 = '{"country":"..","cities":[{"city":,"description":,"attractions":["name":]["descrpition":]"travelDay":type(integer)}]}'
        # question2 = 'attractions":["name":]["descrpition":],"travelDay":type(integer)}'
        # message2 = f"provide me attractions to do in {request.data['mainland']} for {request.data['durring']} put the answer in the following JSON structure {question2}"

        # Process first message
        ourmessage = f"provide me a Trip to {mainland}, for {travelers} trip, budget {budget} {durring}, put the answer in the following JSON structure {question1}"
        answer_from_data = QueryChatGPT.objects.filter(question__exact=ourmessage).values('answer').first()
        if answer_from_data:
            print('answer in data')
            return Response(answer_from_data['answer'])

        # Run the two coroutines asynchronously
        result1=(run_long_poll_async(ourmessage))

        # Wait for both coroutines to complete
        return  JsonResponse(result1,safe=False)
    except Exception as e:
        print(f'error: {e}')
        return  Response("An error occurred while processing your request.")
    
@api_view(['GET', 'POST'])
def attractions(request):
    try:
        print (request.data,'REQUESTTTTTTTT')
        if request.method == 'POST':
            if len(request.POST) > 0:
                try:
                    data = None
                    for key in request.POST:
                        print (key,'KEYYYYYYYY')
                        try:
                            data = json.loads(key)
                            break
                        except json.JSONDecodeError:
                            pass
                    if data is None:
                        raise json.JSONDecodeError('No valid JSON data found', '', 0)
                    cities = data['cities']
                    city_names = [city['city'] for city in cities]
                    question2 = f'"city": {city_names} [{{"attractions": {{"name":,"descrpition":}}}}]'
                    message2 = f'Give me no more than 2 attractions for each city in this JSON format: {question2}'
                    result2 = run_long_poll_async1(message2)
                    return JsonResponse(result2, safe=False)
                except (json.JSONDecodeError, KeyError) as e:
                    return JsonResponse({'error': str(e)}, status=400)
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    except Exception as e:
        print(f'error: {e}')
        return  Response("An error occurred while processing your request.")

    # # Create the two event loops
    # loop1 = asyncio.new_event_loop()
    # loop2 = asyncio.new_event_loop()

    # # Set the event loops for the tasks
    # asyncio.set_event_loop(loop1)
    # asyncio.set_event_loop(loop2)

    # # Create the tasks
    # message2 = f"provide me attractions to do in {request.data['mainland']} for {request.data['durring']} put the answer in the following JSON structure {question2}"
    # task2 = loop2.create_task(run_long_poll_async1(message2))
    # task1 = loop1.create_task(run_long_poll_async(ourmessage))
    

    # # Start the tasks in separate threads
    # thread2 = threading.Thread(target=loop2.run_until_complete, args=(task2,))
    # thread2.start()
    # thread1 = threading.Thread(target=loop1.run_until_complete, args=(task1,))
    # thread1.start()
    

    # # Wait for both tasks to finish and get the results
    # thread1.join()
    # result1 = task1.result()

    # thread2.join()
    # result2 = task2.result()

    # mainresult=result1+result2
    # query = QueryChatGPT(question=ourmessage, answer=mainresult)
    # query.save()
    # return JsonResponse(mainresult, safe=False)

