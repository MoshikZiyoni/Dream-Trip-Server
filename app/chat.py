import json
import os
import time
from app.trip_advisor import foursquare_attraction, foursquare_restaurant, trip_advisor_attraction,trip_advisor_restaurants,flickr_api
from app.bs4 import google_search
import openai
from dotenv import load_dotenv
import requests
from app.models import Attraction, QueryChatGPT,City, Restaurant
from urllib.parse import quote
from geopy.geocoders import Nominatim

# Load environment variables from .env file
load_dotenv()
def run_long_poll_async(ourmessage, retries=3, delay=1):
    geolocator = Nominatim(user_agent="dream-trip")
    print('Start GPT')
    try:
        api_key = os.environ.get('OPENAI_API_KEY')
        openai.api_key = api_key
    except:
        print('Key not found or invalid')

    for attempt in range(retries):
        try:
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": ourmessage}
                ]
            )
            answer1 = completion.choices[0].message.content
            print (answer1)
            for attempt_data in range(retries):
                try:
                    data = json.loads(answer1)
                    # # Extract all city names
                    api_key=os.environ.get('FOURSQUARE')
                    country = data['country']
                    for city_data  in data['cities']:
                        city_name = city_data ['city']
                        description = city_data ['description']
                        location = geolocator.geocode(f"{city_name},{country}")
                        landmarks=[location.latitude, location.longitude]
                        existing_city = City.objects.filter(city=city_name).first()
                        if existing_city:
                            # Add attractions and restaurants to city_data dictionary
                            attract=Attraction.objects.filter(city_id=existing_city.id).values()
                            attractions_list = list(attract)
                            city_data['attractions'] = attractions_list
                            restaura=Restaurant.objects.filter(city_id=existing_city.id).values()
                            restaurants_list = list(restaura)
                            city_data['restaurants']=restaurants_list
                            print ('continue')
                            continue
                        
                        print("City:", city_name, landmarks)
                        if not existing_city:
                            city_query = City(country=country,city=city_name, latitude=landmarks[0], longitude=landmarks[1],description=description)
                            city_query.save()
                            print ('save successefuly for city')
                        city_to_save=City.objects.filter(city=city_name)

                        
                        reslut=foursquare_restaurant(landmarks)
                        restaurants=[]
                        if len(reslut) == 0:
                            restaurant_=trip_advisor_restaurants(city_name,country,landmarks)
                            restaurants.append(restaurant_)
                        else:
                            for i in reslut:
                                
                                name= (i['name'])
                                latitude = i['geocodes']['main']['latitude']
                                longitude = i['geocodes']['main']['longitude']
                                flickr_photos1=flickr_api(name,latitude,longitude)
                                goog_result1=google_search(f"{name},{city_name},{country}")
                                
                                restaurants_info={
                                    'name':name,
                                    'latitude':latitude,
                                    'longitude':longitude,
                                    'photos':flickr_photos1,
                                    'review_score': goog_result1['review_score'],
                                }
                                restaurants.append(restaurants_info)
                                try:
                                    city_obj = city_to_save.first()  # Get the first city object
                                    if city_obj is not None:
                                        resta_query = Restaurant(name=name, city=city_obj, details=restaurants_info)
                                        resta_query.save()
                                    else:
                                        print(f"No city found for {city_name}")
                                except Exception as e:
                                    print(f"Error occurred: {e}")
                        
                        reslut1=foursquare_attraction(landmarks)
                        attractions=[]
                        if len(reslut1)==0:
                            attractions_info_trip=trip_advisor_attraction(city_name,country,landmarks)
                            attractions.append(attractions_info_trip)
                           
                        else:
                            for i in reslut1:
                                name= (i['name'])
                                latitude = i['geocodes']['main']['latitude']
                                longitude = i['geocodes']['main']['longitude']
                                flickr_photos=flickr_api(name,latitude,longitude)
                                goog_result=google_search(f"{name},{city_name},{country}")
                                attractions_info={
                                    'name':name,
                                    'latitude':latitude,
                                    'longitude':longitude,
                                    'photos':flickr_photos,
                                    'review_score': goog_result['review_score'],
                                    
                                }
                                attractions.append(attractions_info)
                                try:
                                    city_obj = city_to_save.first()  # Get the first city object
                                    if city_obj is not None:
                                        atrc_query = Attraction(name=name, city=city_obj, details=attractions_info)
                                        atrc_query.save()
                                    else:
                                        print(f"No city found for {city_name}")
                                except Exception as e:
                                    print(f"Error occurred: {e}")
                        
                        
                        city_data['attractions'] = attractions
                        city_data['restaurants'] = restaurants
                    combined_data =json.dumps(data, indent=2)
                    

                    query = QueryChatGPT(question=ourmessage, answer=combined_data)
                    query.save()
                    return combined_data
                except Exception as e:
                    print(f'Error occurred: {e}')
                    print(f'Retrying... (attempt {attempt_data + 1})')
                    time.sleep(delay)

        except openai.error.APIError as e:
            if e.status_code == 429:
                # If we hit the API rate limit, wait for a bit before trying again
                time.sleep(1)
            else:
                # If there's another API error, raise an exception
                raise
        except Exception as e:
            print(f'Error occurred: {e}')
            print(f'Retrying... (attempt {attempt + 1})')
            time.sleep(delay)

    # If all retries fail, return a default error message
    return "I'm sorry, an error occurred while generating the response. Please try again later."