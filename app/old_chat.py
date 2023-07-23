# # import json
# # import os
# # import time
# # from app.trip_advisor import (
# #     foursquare_attraction,
# #     foursquare_restaurant,
# #     trip_advisor_attraction,
# #     trip_advisor_restaurants,
# # )
# # import openai
# # from dotenv import load_dotenv
# # from app.models import Attraction, Country, QueryChatGPT, City, Restaurant
# # from geopy.geocoders import Nominatim
# # import threading
# # from concurrent.futures import ThreadPoolExecutor
# # from app.utils import generate_schedule, process_attraction, process_restaurant, restaurant_GPT
# # from threading import Thread
# # from concurrent.futures import ThreadPoolExecutor
# # import queue

# # executor = ThreadPoolExecutor(max_workers=10)

# # # Load environment variables from .env file
# # load_dotenv()
# # geolocator = Nominatim(user_agent="dream-trip")
# # api_key = os.environ.get("FOURSQUARE")
# # import threading

# # restaurants = []
# # def process_city(city_data, country, country_id):
# #     restaurants_queue = queue.Queue()
# #     attractions_queue = queue.Queue()
# #     # attractions_queue.put(attractions)
# #     # restaurants_queue.put(restaurants)
# #     city_name = city_data["city"]
# #     description = city_data["description"]
# #     location = geolocator.geocode(f"{city_name},{country}")
# #     landmarks = [location.latitude, location.longitude]
# #     existing_city = City.objects.filter(city=city_name).first()

# #     print("City:", city_name, landmarks)
# #     if not existing_city:
# #         city_query = City(
# #             country_id=country_id,
# #             city=city_name,
# #             latitude=landmarks[0],
# #             longitude=landmarks[1],
# #             description=description,
# #         )
# #         city_query.save()
# #         print("Save successfully for city")
# #     city_data["latitude"] = landmarks[0]
# #     city_data["longitude"] = landmarks[1]
# #     city_to_save = City.objects.filter(city=city_name)
# #     city_objs = city_to_save.all()
# #     if city_objs:
# #         city_obj = city_objs[0]
# #     print(city_obj, "city_obj")

# #       # Initialize an empty list for restaurants

# #     restaurants_thread = threading.Thread(
# #         target=process_restaurants,
# #         args=(landmarks, city_name, country, city_obj, city_data, restaurants,restaurants_queue),
# #     )
# #     restaurants_thread.start()

# #     attractions_thread = threading.Thread(
# #         target=process_attractions,
# #         args=(landmarks, city_name, country, city_obj, city_data,attractions_queue),
# #     )
# #     attractions_thread.start()

# #     # Wait for the threads to complete
# #     restaurants_thread.join()
# #     attractions_thread.join()

# #     # attract = Attraction.objects.filter(city_id=city_obj.id).values()
# #     # attractions_list = list(attract)
# #     # resturaa=Restaurant.objects.filter(city_id=city_obj.id).values()
# #     # restaurant_list=list(resturaa)
# #     # city_data["attractions"] = attractions_list
# #     # city_data["restaurants"] = restaurant_list

    
# #     restaurants_data = list(restaurants_queue.queue)
# #     attractions_data = list(attractions_queue.queue)[0]
# #     try:
# #         restaurants_data = [json.loads(r) for r in {json.dumps(r) for r in restaurants_data}]
# #         attractions_data = [json.loads(a) for a in {json.dumps(a) for a in attractions_data}]
# #     except Exception as e:
# #         print ('not sucess with the SETTTTT',e)
    
# #     city_data["attractions"] = attractions_data
# #     city_data["restaurants"] = restaurants_data
# #     # print (restaurants_data)
# #     # print (attractions_data)
# #     return city_data


# # def process_restaurants(landmarks, city_name, country, city_obj, city_data, restaurants,restaurants_queue):
# #     reslut = foursquare_restaurant(landmarks)
# #     if len(reslut) == 0:
# #         print("Start TripAdvisor restaurant")
# #         # restaurant_ = trip_advisor_restaurants(city_name, country, landmarks)
# #         my_restaurant=restaurant_GPT(city=city_name)
# #         threads = []
# #         for restaur in my_restaurant:
# #             thread = Thread(target=process_restaurant, args=(restaur, city_obj, restaurants))
# #             thread.start()
# #             threads.append(thread)
# #             for thread in threads:
# #                 thread.join()
# #         # restaurants.append(restaurant_)
# #     else:
# #         threads = []
# #         for restaur in reslut:
# #             thread = Thread(target=process_restaurant, args=(restaur, city_obj, restaurants))
# #             thread.start()
# #             threads.append(thread)

# #         # Wait for all threads to complete
# #         for thread in threads:
# #             thread.join()
# #     restaurants = [json.loads(r) for r in {json.dumps(r) for r in restaurants}]

# #     restaurants_queue.put(restaurants)

# # def process_attractions(landmarks, city_name, country, city_obj, city_data,attractions_queue):
# #     reslut1 = foursquare_attraction(landmarks, city_name, country)
# #     attractions = []

# #     threads = []

# #     if len(reslut1) == 0:
# #         print("Start TripAdvisor attraction")
# #         attractions_info_trip = trip_advisor_attraction(city_name, country, landmarks)
# #         attractions.append(attractions_info_trip)
# #         print("TripAdvisor line 93")
# #     else:
# #         print("Start the else line 94")

# #         for attrac in reslut1:
# #             thread = Thread(target=process_attraction, args=(attrac, city_obj, attractions))
# #             thread.start()
# #             threads.append(thread)

# #         # Wait for all threads to complete
# #         for thread in threads:
# #             thread.join()

# #     # city_data["attractions"] = attractions
# #     attractions = [json.loads(a) for a in {json.dumps(a) for a in attractions}]

# #     attractions_queue.put(attractions)

# #     # return city_data





# # def run_long_poll_async(ourmessage, mainland, retries=3, delay=1):
# #     print("Start GPT")
# #     try:
# #         api_key = os.environ.get("OPENAI_API_KEY")
# #         openai.api_key = api_key
# #     except:
# #         print("Key not found or invalid")

# #     for attempt in range(retries):
# #         try:
# #             completion = openai.ChatCompletion.create(
# #                 model="gpt-3.5-turbo",
# #                 messages=[{"role": "user", "content": ourmessage}],
# #             )
# #             answer1 = completion.choices[0].message.content
# #             print(answer1)
# #             for attempt_data in range(retries):
# #                 try:
# #                     data = json.loads(answer1)
# #                     data1 = json.loads(answer1)
# #                     country = data["country"]
# #                     if country != mainland:
# #                         print("Country is not mainland. Retrying...")
# #                         break
                    
# #                     try:
# #                         itinerary_description=data['itinerary-description']
# #                     except:
# #                         pass
# #                     try:
# #                         itinerary_description=data['itinerary_description']
# #                     except:
# #                         pass
# #                     try:
# #                         existing_country = Country.objects.filter(name=country).first()
# #                         country_id = existing_country.id
# #                     except:
# #                         print("Country does not exist")
# #                     if not existing_country:
# #                         query_for_country = Country(name=country)
# #                         query_for_country.save()
# #                         country_id = query_for_country.id

# #                     executor = ThreadPoolExecutor()
# #                     for city_data in data["cities"]:
# #                         city_name = city_data["city"]
# #                         existing_city = City.objects.filter(city=city_name).first()
# #                         if existing_city:
# #                             attract = Attraction.objects.filter(city_id=existing_city.id).values()
# #                             attractions_list = list(attract)
# #                             city_data["attractions"] = attractions_list
# #                             restaura = Restaurant.objects.filter(city_id=existing_city.id).values()
# #                             restaurants_list = list(restaura)
# #                             city_data["restaurants"] = restaurants_list
# #                             print("Continue")
# #                             continue
# #                         executor.submit(process_city, city_data, country, country_id)

# #                     executor.shutdown()

# #                     combined_data=generate_schedule(data)
# #                     query = QueryChatGPT(question=ourmessage, answer=data1,itinerary_description=itinerary_description)
# #                     query.save()
                    
# #                     return {'answer':combined_data,'itinerary_description':itinerary_description}
# #                 except Exception as e:
# #                     print("Error occurred:", e)
# #                     print(f"Retrying... (attempt {attempt_data + 1})")
# #                     time.sleep(delay)

# #         except openai.error.APIError as e:
# #             try:
# #                 if e.status_code == 429:
# #                     time.sleep(1)
# #                 else:
# #                     raise
# #             except Exception as e:
# #                 print("Error occurred:", e)
# #         except Exception as e:
# #             print("Error occurred:", e)
# #             print(f"Retrying... (attempt {attempt + 1})")
# #             time.sleep(delay)

# #     return "I'm sorry, an error occurred while generating the response. Please try again later."















































# import json
# import os
# import time
# from app.trip_advisor import (
#     foursquare_attraction,
#     foursquare_restaurant,
#     trip_advisor_attraction,
#     trip_advisor_restaurants,
# )
# import openai
# from dotenv import load_dotenv
# from app.models import Attraction, Country, QueryChatGPT, City, Restaurant
# from geopy.geocoders import Nominatim
# import threading
# from concurrent.futures import ThreadPoolExecutor
# from app.utils import generate_schedule, process_attraction, process_restaurant, restaurant_GPT,handle_invalid_json
# from threading import Thread
# from concurrent.futures import ThreadPoolExecutor
# import queue
# from threading import Lock
# executor = ThreadPoolExecutor(max_workers=10)

# # Load environment variables from .env file
# load_dotenv()
# geolocator = Nominatim(user_agent="dream-trip")
# api_key = os.environ.get("FOURSQUARE")
# import threading

# new_attractions = []
# new_restaurants = []
# def process_city(city_data, country, country_id):
#     restaurants_queue = queue.Queue()
#     attractions_queue = queue.Queue()
#     # attractions_queue.put(attractions)
#     # restaurants_queue.put(restaurants)
#     city_name = city_data["city"]
#     description = city_data["description"]
#     location = geolocator.geocode(f"{city_name},{country}")
#     landmarks = [location.latitude, location.longitude]
#     existing_city = City.objects.filter(city=city_name).first()

#     print("City:", city_name, landmarks)
#     if not existing_city:
#         city_query = City(
#             country_id=country_id,
#             city=city_name,
#             latitude=landmarks[0],
#             longitude=landmarks[1],
#             description=description,
#         )
#         city_query.save()
#         print("Save successfully for city")
#     city_data["latitude"] = landmarks[0]
#     city_data["longitude"] = landmarks[1]
#     city_to_save = City.objects.filter(city=city_name)
#     city_objs = city_to_save.all()
#     if city_objs:
#         city_obj = city_objs[0]
#     print(city_obj, "city_obj")

#       # Initialize an empty list for restaurants

#     restaurants_thread = threading.Thread(
#         target=process_restaurants,
#         args=(landmarks, city_name, country, city_obj, city_data,restaurants_queue),
#     )
#     restaurants_thread.start()

#     attractions_thread = threading.Thread(
#         target=process_attractions,
#         args=(landmarks, city_name, country, city_obj, city_data,attractions_queue),
#     )
#     attractions_thread.start()

#     # Wait for the threads to complete
#     restaurants_thread.join()
#     attractions_thread.join()

#     # attract = Attraction.objects.filter(city_id=city_obj.id).values()
#     # attractions_list = list(attract)
#     # resturaa=Restaurant.objects.filter(city_id=city_obj.id).values()
#     # restaurant_list=list(resturaa)
#     # city_data["attractions"] = attractions_list
#     # city_data["restaurants"] = restaurant_list

    
#     restaurants_data = list(restaurants_queue.queue)
#     attractions_data = list(attractions_queue.queue)[0]
#     try:
#         restaurants_data = [json.loads(r) for r in {json.dumps(r) for r in restaurants_data}]
#         attractions_data = [json.loads(a) for a in {json.dumps(a) for a in attractions_data}]
#         new_attractions.append(attractions_data)
#         new_restaurants.append(restaurants_data)
#     except Exception as e:
#         print ('not sucess with the SETTTTT',e)
    
#     city_data["attractions"] = attractions_data
#     city_data["restaurants"] = restaurants_data
#     # print (restaurants_data)
#     # print (attractions_data)
#     return city_data


# def process_restaurants(landmarks, city_name, country, city_obj, city_data,restaurants_queue):
#     restaurants_lock = Lock()

# # In process_restaurant:
#     with restaurants_lock:
#         reslut = foursquare_restaurant(landmarks)
#         restaurants = []
#         if len(reslut) == 0:
#             print("Start TripAdvisor restaurant")
#             # restaurant_ = trip_advisor_restaurants(city_name, country, landmarks)
#             my_restaurant=restaurant_GPT(city=city_name)
#             threads = []
#             for restaur in my_restaurant:
#                 thread = Thread(target=process_restaurant, args=(restaur, city_obj, restaurants))
#                 thread.start()
#                 threads.append(thread)
#                 for thread in threads:
#                     thread.join()
#             # restaurants.append(restaurant_)
#         else:
#             threads = []
#             for restaur in reslut:
#                 thread = Thread(target=process_restaurant, args=(restaur, city_obj, restaurants))
#                 thread.start()
#                 threads.append(thread)

#             # Wait for all threads to complete
#             for thread in threads:
#                 thread.join()
#         restaurants = [json.loads(r) for r in {json.dumps(r) for r in restaurants}]

#         restaurants_queue.put(restaurants)

# def process_attractions(landmarks, city_name, country, city_obj, city_data,attractions_queue):
#     attractions_lock=Lock()
#     with attractions_lock:
#         reslut1 = foursquare_attraction(landmarks, city_name, country)
#         attractions = []

#         threads = []

#         if len(reslut1) == 0:
#             print("Start TripAdvisor attraction")
#             attractions_info_trip = trip_advisor_attraction(city_name, country, landmarks)
#             attractions.append(attractions_info_trip)
#             print("TripAdvisor line 93")
#         else:
#             print("Start the else line 94")

#             for attrac in reslut1:
#                 thread = Thread(target=process_attraction, args=(attrac, city_obj, attractions))
#                 thread.start()
#                 threads.append(thread)

#             # Wait for all threads to complete
#             for thread in threads:
#                 thread.join()

#         # city_data["attractions"] = attractions
#         attractions = [json.loads(a) for a in {json.dumps(a) for a in attractions}]

#         attractions_queue.put(attractions)

#     # return city_data





# def run_long_poll_async(ourmessage, mainland, retries=3, delay=1):
#     print("Start GPT")
#     try:
#         api_key = os.environ.get("OPENAI_API_KEY")
#         openai.api_key = api_key
#     except:
#         print("Key not found or invalid")

#     for attempt in range(retries):
#         try:
#             completion = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=[{"role": "user", "content": ourmessage}],
#             )
#             answer1 = completion.choices[0].message.content
#             print(answer1)
#             for attempt_data in range(retries):
#                 try:
#                     data = handle_invalid_json(answer1)
#                     if data is None:
#                         # Handle JSON parsing error, e.g., log or raise an exception
#                         print("Failed to parse JSON response.")
#                         break
#                     data1 = data
#                     country = data["country"]
#                     if country != mainland:
#                         print("Country is not mainland. Retrying...")
#                         break
                    
#                     try:
#                         itinerary_description=data['itinerary-description']
#                     except:
#                         pass
#                     try:
#                         itinerary_description=data['itinerary_description']
#                     except:
#                         pass
#                     try:
#                         existing_country = Country.objects.filter(name=country).first()
#                         country_id = existing_country.id
#                     except:
#                         print("Country does not exist")
#                     if not existing_country:
#                         query_for_country = Country(name=country)
#                         query_for_country.save()
#                         country_id = query_for_country.id
#                         print ('save country success')

#                     executor = ThreadPoolExecutor()

#                     for city_data in data["cities"]:
#                         city_data_lock = Lock()
#                         with city_data_lock:
#                             city_name = city_data["city"]
#                             existing_city = City.objects.filter(city=city_name).first()
#                             if existing_city:
#                                 attract = Attraction.objects.filter(city_id=existing_city.id).values()
#                                 attractions_list = list(attract)
#                                 city_data["attractions"] = attractions_list
#                                 restaura = Restaurant.objects.filter(city_id=existing_city.id).values()
#                                 restaurants_list = list(restaura)
#                                 city_data["restaurants"] = restaurants_list
#                                 print("Continue")
#                                 continue
#                             else:
#                                 executor.submit(process_city, city_data, country, country_id)
                    
#                     executor.shutdown()

#                     combined_data=generate_schedule(data)
#                     query = QueryChatGPT(question=ourmessage, answer=data1,itinerary_description=itinerary_description)
#                     query.save()
                    
#                     return {'answer':combined_data,'itinerary_description':itinerary_description,'new_restaurants':new_restaurants,'new_attractions':new_attractions}
#                 except Exception as e:
#                     print("Error occurred:", e)
#                     print(f"Retrying... (attempt {attempt_data + 1})")
#                     time.sleep(delay)

#         except openai.error.APIError as e:
#             try:
#                 if e.status_code == 429:
#                     time.sleep(1)
#                 else:
#                     raise
#             except Exception as e:
#                 print("Error occurred:", e)
#         except Exception as e:
#             print("Error occurred:", e)
#             print(f"Retrying... (attempt {attempt + 1})")
#             time.sleep(delay)

#     return "I'm sorry, an error occurred while generating the response. Please try again later."




