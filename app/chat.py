import json
import os
import time
import openai
from dotenv import load_dotenv
import requests
from app.models import QueryChatGPT,City
from urllib.parse import quote

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
            answer1 = completion.choices[0].message.content
            print(answer1)
            data = json.loads(answer1)
            # print (data,'dataaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            # # Extract all city names
            key = os.environ.get('TRIP_ADVISOR_KEY')
            country = data['country']
            for city in data['cities']:
                city_name = city['city']
                landmarks = city['landmarks']
                description = city['description']
                if isinstance(landmarks, list):
                    print ('this is a list')
                    if len(landmarks)>2:
                        print((len(landmarks)),'lenn')
                        print (landmarks,'sucess to landmapr 0')
                        landmarks = landmarks[0]
                    else:
                        print('skip landmarks')

                print("City:", city_name, landmarks)
                url = f"https://api.content.tripadvisor.com/api/v1/location/nearby_search?"
                headers = {"accept": "application/json"}
                params = {
                    'latLong': quote(f"{landmarks[0]}, {landmarks[1]}"),  # URL-encode the latLong values
                    'key' : {key},
                    # 'searchQuery': city_name+country,
                    'category': 'attractions',
                    'radius': '10',
                    'radiusUnit':'km',
                    'language' : 'en'
                }
                response = requests.get(url, headers=headers, params=params)
                print(response)
                result = response.json()
                print(result)
                attrcat=result['data']
                attractions = []
                for attraction in result['data']:
                    attractions.append(attraction)
                existing_city = City.objects.filter(city=city_name).first()
                if not existing_city:
                        city_query = City(country=country,city=city_name, latitude=landmarks[0], longitude=landmarks[1],attractions=attrcat,description=description)
                        city_query.save()
                        print ('save successefuly for city')
                city['attractions'] = attractions

            combined_data =json.dumps(data, indent=2)

            query = QueryChatGPT(question=ourmessage, answer=combined_data)
            query.save()
            return combined_data

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