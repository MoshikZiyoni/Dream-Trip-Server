import asyncio
import threading
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import run_long_poll_async


@api_view(['GET', 'POST'])
def gpt_view(request):
    # question2='{"country":"..","cities":[{"city":,"description":,"attractions":["name":]["descrpition":],"travelDay":type(integer)}]}'
    question2='{"country":"..","cities":[{"city":,"description":,"travelDay":type(integer)}]}'
    ourmessage=f"provide me a Trip to {request.data['mainland']} ,for {request.data['travelers']} trip,budget {request.data['budget']} {request.data['durring']},put the answer in the following JSON structure {question2}"
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    task = loop.create_task(run_long_poll_async(ourmessage))

    # Start the task in a separate thread
    thread = threading.Thread(target=loop.run_until_complete, args=(task,))
    thread.start()

    # Wait for the task to finish and get the result
    thread.join()
    result = task.result()

    return JsonResponse(result, safe=False)


# @api_view(['GET'])
# def long_poll(request):
   
#     # Get the message to poll for from the query parameters
#     ourmessage = request.GET.get('ourmessage', '')
#     print ('ourmessage')

#     # Check if there is a message to poll for
#     if not ourmessage:
#         print ('NOT GOODDDDDDDDDDDDDDDDDDDDDDDDDDDD')
#         return Response({"message": "No message to poll for."})

#     # Poll for updates using the run_long_poll function
#     print ('start long poll')
#     result = run_long_poll(ourmessage)
#     if result:
#         print (result,'RESULTTTTTTTTTTTTTTTTTTTTTTTTTTTTT')
#         return JsonResponse(result, safe=False)  
    
#     # Return the response to the client
#     return JsonResponse({})

    # try:
    #     result = run_gpt_func(ourmessage)
    #     return JsonResponse(result,safe=False)
    # except:
    #     print ('The first attempt failed. Trying again...')
    #     try:
    #         result = run_gpt_app(ourmessage)
    #         return JsonResponse(result,safe=False)
    #     except:
    #         print ('Both attempts failed. Cannot generate response.')
    
    