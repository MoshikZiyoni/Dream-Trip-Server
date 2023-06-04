import json
import os
import time
import openai
from dotenv import load_dotenv
import requests
from app.models import QueryChatGPT,City

# Load environment variables from .env file
load_dotenv()
def run_long_poll_async(ourmessage, retries=3, delay=1):
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
            city_list =[]
            answer1 = completion.choices[0].message.content
            # data = json.loads(answer1)
            # # Extract all city names
            # cities = [city['city'] for city in data['cities']]
            # for city in cities:
            #     city_list.append(city)
            # api_key = os.environ.get('GPS_KEY')

            # for city in city_list:
            #     geocoding_url = f'https://api.opencagedata.com/geocode/v1/json?q={city}&key={api_key}'

            #     response = requests.get(geocoding_url)
            #     data = response.json()

            #     if data['results']:
            #         latitude1 = data['results'][0]['geometry']['lat']
            #         longitude1 = data['results'][0]['geometry']['lng']
            #         existing_city = City.objects.filter(city=city).first()

            #         if not existing_city:
            #             city_query = City(city=city, latitude=latitude1, longitude=longitude1)
            #             city_query.save()
            #             print(f"City: {city} - Latitude: {latitude1}, Longitude: {longitude1}")
            #         else:
            #             print(f"City: {city} - Already exists in the database")
            #     else:
            #         print(f"City: {city} - Coordinates not found")
            query = QueryChatGPT(question=ourmessage, answer=answer1)
            query.save()
            # city_data_gpt = {}
            # for city in city_list:
            #     city_object = City.objects.filter(city=city).first()
            #     if city_object:
            #         city_data_gpt[city] = {
            #             'latitude': city_object.latitude,
            #             'longitude': city_object.longitude
            #         }
            #     else:
            #         print(f"City data not found for: {city}")            
            return answer1
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