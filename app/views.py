from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import run_long_poll_async
from app.models import QueryChatGPT

from django.core.cache import cache

@api_view(['GET', 'POST'])
def gpt_view(request):
    email=request.data['email']
    if not email:
        return JsonResponse({'error': 'Email not provided'})

    # Check if the user's email exists in the request count dictionary
    request_count = cache.get(email, 0)
    # If the user has made more than 10 requests in the past 24 hours, block the request
    if request_count >= 10:
        return JsonResponse({'error': 'Too many requests'})

    # Otherwise, increment the request count and set the cache with the new value
    request_count += 1
    print (request_count)
    timeout_seconds = 24 * 60 * 60  # 24 hours in seconds
    cache.set(email, request_count, timeout=timeout_seconds)

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
        query=QueryChatGPT()
        query.question = ourmessage
        query.answer = result1
        query.save()
        # Wait for both coroutines to complete
        return  JsonResponse(result1,request_count,safe=False)
    except Exception as e:
        print(f'error: {e}')
        return  Response("An error occurred while processing your request.")
    
# @api_view(['GET', 'POST'])
# def get_user_email(request):
#     if request.method == 'POST':
#         email = (request.data['email'])
#         email_obj = Email(email=email, created_at=timezone.now())
#         email_obj.save()

#         return JsonResponse({'success': True})
#     else:
#         return JsonResponse({'success': False})
    

# Get the user's IP address or other identifier
    user_id = get_user_id(request)
 # Get the number of requests made by the user in the last 24 hours
    requests_made = cache.get(user_id, 0)

    # If the user has made more than 10 requests, return an error response
    if requests_made >= 10:
        return JsonResponse({'error': 'Rate limit exceeded'})

    # Process the request as usual
    print(request.data)

    # Increment the number of requests made by the user and store it in the cache for 24 hours
    cache.set(user_id, requests_made + 1, 24 * 60 * 60)