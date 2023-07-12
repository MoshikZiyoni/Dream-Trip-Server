import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.chat import run_long_poll_async
from app.models import Attraction, Country, QueryChatGPT,City, Restaurant
from django.core.cache import cache

from app.my_selenium import perform_search
# from threading import Thread
# from app.wikipediaapi import process_query



@api_view(['GET', 'POST'])
def gpt_view(request):
    # attractions = Attraction.objects.filter(review_score='0')
    # attractions=Attraction.objects.filter(review_score__exact='')

    # for attraction in attractions:
    #     # Call your function to generate a new review score
    #     new_review_score = perform_search(attraction.name)
    #     print ('new_review_score: ',new_review_score,len(new_review_score))
    #     if new_review_score==None or len(new_review_score)==0:
    #         attraction.review_score='4.0'
    #         attraction.save()
    #     else:
    #         # Update the attraction's review score
    #         attraction.review_score = str(new_review_score)
    #         attraction.save()
    # # exit
    # # exit
    # return 'ok'
    #####REAL PRICESSSSS
    # def extract_attraction_names(attractions):
    #     # attractions = Attraction.objects.all()
    #     attractions = Attraction.objects.filter(city__id=291)     
    #     for attraction in attractions[:10]:
    #         print (attraction.name)
    #         # attraction_names.append(attraction.name)
    #     return 'ok'
    # extract_attraction_names(attractions='')

#     def extract_attraction_names(attraction_prices):
#         attractions = Attraction.objects.filter(city__id=291)[:10]
#         for attraction in attractions:
#             attraction_name = attraction.name
#             if attraction_name in attraction_prices:
#                 attraction.real_price = attraction_prices[attraction_name]
#                 attraction.save()
#         return 'ok'
#     extract_attraction_names(attraction_prices = { "Yatch Club de Cannes": "free entry, membership fees vary 12", "Gare Maritime de Cannes": "free entry, event spaces available for rent 3", "Torch Cannes": "free entry, food and drinks prices vary", "Agence Cannes France": "real estate agency, prices vary depending on the property", "Plage du Mairie de Cannes": "free entry", "Pirates N' Paradise @ Cannes": 'escape game, 25 EUR per person ', "Ville de Cannes": "free entry", "Port de Cannes": 'free entry, boat parking fees vary ', "Cannes Sign": "free entry", "The Cannes Lions Beach": "free entry" }


# )
   
    
#     return 'ok'
    

    # QueryChatGPT.objects.all().delete()
    
    # City.objects.all().delete()
    # Attraction.objects.all().delete()
    # Restaurant.objects.all().delete()
    
    def populate_attractions(attractions_data):
        city2=City.objects.filter(city='Krabi')
        city_obj = city2[0]
        for attraction_data in attractions_data:
            
            attraction = Attraction(
                city_id=city_obj.id,
                name=attraction_data["name"],
                latitude=attraction_data["latitude"],
                longitude=attraction_data["longitude"],
                photos=attraction_data["photos"],
                review_score=attraction_data["review_score"],
                description=attraction_data["description"],
                website=attraction_data["website"],
                hours_popular=attraction_data["hours_popular"],
                distance=attraction_data["distance"],
                real_price=attraction_data["real_price"]
            )
            print (attraction_data["name"])
            attraction.save()
    populate_attractions(attractions_data = [
    {
        "city": "Krabi",
        "name": "Railay Beach",
        "latitude": 8.0126,
        "longitude": 98.8375,
        "photos": "",
        "review_score": "4.7",
        "description": "Visit Railay Beach, a stunning beach accessible only by boat. Enjoy the crystal-clear waters, limestone cliffs, and outdoor activities such as rock climbing and kayaking.",
        "website": "",
        "hours_popular": "Open 24 hours",
        "distance": 0,
        "real_price": "Free"
    },
    {
        "city": "Krabi",
        "name": "Phi Phi Islands",
        "latitude": 7.7407,
        "longitude": 98.7780,
        "photos": "",
        "review_score": "4.6",
        "description": "Explore the picturesque Phi Phi Islands, known for their white sandy beaches and crystal-clear waters. Take a boat tour, snorkel, or relax on the pristine beaches.",
        "website": "",
        "hours_popular": "Open all year round",
        "distance": 40,
        "real_price": "Varies"
    },
    {
        "city": "Krabi",
        "name": "Tiger Cave Temple (Wat Tham Sua)",
        "latitude": 8.0467,
        "longitude": 98.9225,
        "photos": "",
        "review_score": "4.5",
        "description": "Visit Tiger Cave Temple, a Buddhist temple known for its striking scenery and challenging climb to the top. Enjoy panoramic views of Krabi from the summit.",
        "website": "",
        "hours_popular": "Open daily",
        "distance": 10,
        "real_price": "Free"
    },
    {
        "city": "Krabi",
        "name": "Four Islands",
        "latitude": 7.7065,
        "longitude": 98.7625,
        "photos": "",
        "review_score": "4.4",
        "description": "Embark on a Four Islands tour, visiting Phra Nang Cave Beach, Chicken Island, Tup Island, and Poda Island. Enjoy snorkeling, swimming, and relaxing on these beautiful islands.",
        "website": "",
        "hours_popular": "Open all year round",
        "distance": 20,
        "real_price": "Varies"
    },
    {
        "city": "Krabi",
        "name": "Emerald Pool (Sa Morakot)",
        "latitude": 8.0105,
        "longitude": 99.6144,
        "photos": "",
        "review_score": "4.3",
        "description": "Take a refreshing dip in the Emerald Pool, a natural hot spring surrounded by lush rainforest. Enjoy the beautiful turquoise waters and the tranquility of the area.",
        "website": "",
        "hours_popular": "Open daily",
        "distance": 60,
        "real_price": "Varies"
    }
]

)
# You can now use this attractions_data list to populate your database.

    return 'ok'
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
        
        result1=(run_long_poll_async(ourmessage,mainland))
        
        result1=result1,{"request_left":request_left}

        return  JsonResponse(result1,safe=False)
    except Exception as e:
        print(f'error: {e}')
        return  Response("An error occurred while processing your request.")
    