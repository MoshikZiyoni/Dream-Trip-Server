import json
import os
import time
from app.trip_advisor import trip_advisor_attraction,trip_advisor_restaurants,flickr_api
from app.bs4 import google_search
import openai
from dotenv import load_dotenv
import requests
from app.models import QueryChatGPT,City
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
            for attempt_data in range(retries):
                try:
                    data = json.loads(answer1)
                    # # Extract all city names
                    api_key=os.environ.get('FOURSQUARE')
                    country = data['country']
                    for city_data  in data['cities']:
                        city_name = city_data ['city']
                        landmarks = city_data ['landmarks']
                        description = city_data ['description']
                        existing_city = City.objects.filter(city=city_name).first()
                        if existing_city:
                            print ('continue')
                            continue
                        if isinstance(landmarks, list):
                            print ('this is a list')
                            if len(landmarks)>2:
                                print (landmarks,'sucess to landmapr 0')
                                landmarks = landmarks[0]
                            else:
                                print('skip landmarks')

                        print("City:", city_name, landmarks)

                        url = "https://api.foursquare.com/v3/places/search?"

                        headers = {
                            "accept": "application/json",
                            "Authorization": api_key
                        }

                        query= {
                            'categories':'13000',
                            "ll" :  f"{landmarks[0]},{landmarks[1]}",
                            'radius':2500,
                            # 'sort': 'distance'
                        }
                        response = requests.get(url, params=query,headers=headers)

                        response_text=(response.text)
                        jsonto=json.loads(response_text)
                        # print (jsonto)
                        reslut=jsonto['results']
                        restaurants=[]
                        if len(reslut) == 0:
                            restaurant_=trip_advisor_restaurants(city_name,country,landmarks)
                            restaurants.append(restaurant_)
                        else:
                            for i in reslut:
                                # print (i)
                                name= (i['name'])
                                latitude = i['geocodes']['main']['latitude']
                                longitude = i['geocodes']['main']['longitude']
                                goog_result1=google_search(f"{name},{city_name},{country}")
                                restaurants_info={
                                    'name':name,
                                    'latitude':latitude,
                                    'longitude':longitude,
                                    'review_score': goog_result1['review_score'],
                                }
                                restaurants.append(restaurants_info)

                        url1 = "https://api.foursquare.com/v3/places/search?"

                        headers = {
                            "accept": "application/json",
                            "Authorization": api_key
                        }

                        query1= {
                            'categories':'10000,16000',
                            "ll" :  f"{landmarks[0]},{landmarks[1]}",
                            'radius':2500,
                            # 'sort': 'distance'
                        }
                        response1 = requests.get(url1, params=query1,headers=headers)

                        response_text1=(response1.text)
                        jsonto1=json.loads(response_text1)
                        reslut=jsonto1['results']
                        attractions=[]
                        if len(reslut)==0:
                            attractions_info_trip=trip_advisor_attraction(city_name,country,landmarks)
                            attractions.append(attractions_info_trip)
                           
                        else:
                            for i in reslut:
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
                                    
                        
                        existing_city = City.objects.filter(city=city_name).first()
                        if not existing_city:
                            city_query = City(country=country,city=city_name, latitude=landmarks[0], longitude=landmarks[1],attractions=attractions,description=description,restaurants=restaurants)
                            city_query.save()
                            print ('save successefuly for city')
                        
                        city_data['attractions'] = attractions
                        city_data['restaurants'] = restaurants
                    # print (data['cities'],'city dataaaaaaaaaaaaaaaaaaaaaaa')
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