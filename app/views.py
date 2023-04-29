import asyncio
import threading
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import run_long_poll_async
from app.models import QueryChatGPT


@api_view(['GET', 'POST'])
def gpt_view(request):
    question1 = '{"country":"..","cities":[{"city":,"description":,"travelDay":type(integer)}]}'
    question2 = 'attractions":["name":]["descrpition":],"travelDay":type(integer)}'

    # Process first message
    ourmessage = f"provide me a Trip to {request.data['mainland']} ,for {request.data['travelers']} trip,budget {request.data['budget']} {request.data['durring']},put the answer in the following JSON structure {question1}"
    try:
        answer_from_data = QueryChatGPT.objects.filter(question__exact=ourmessage)
        if answer_from_data.exists():
            data = answer_from_data.values('answer')[0]
            answer = data['answer']
            print('answer in data')
            return Response(answer) 
        else:
            print('Not Found')
    except:
        print('Internal Server Error')
    loop1 = asyncio.new_event_loop()
    asyncio.set_event_loop(loop1)
    task1 = loop1.create_task(run_long_poll_async(ourmessage))

    # Start the first task in a separate thread
    thread1 = threading.Thread(target=loop1.run_until_complete, args=(task1,))
    thread1.start()

    # Process second message
    message2 = f"provide me attractions to do in {request.data['mainland']} for {request.data['durring']} put the answer in the following JSON structure {question2}"
    loop2 = asyncio.new_event_loop()
    asyncio.set_event_loop(loop2)
    task2 = loop2.create_task(run_long_poll_async(message2))

    # Start the second task in a separate thread
    thread2 = threading.Thread(target=loop2.run_until_complete, args=(task2,))
    thread2.start()

    # Wait for both tasks to finish and get the results
    thread1.join()
    result1 = task1.result()

    thread2.join()
    result2 = task2.result()
    mainresult=result1+result2
    query = QueryChatGPT(question=ourmessage, answer=mainresult)
    query.save()
    return JsonResponse(mainresult, safe=False)
