
import json
import requests
from dotenv import load_dotenv
import os
load_dotenv()

api_key=os.environ.get('FOURSQUARE')
print(api_key)

def foursquare_hotels(landmarks):

    url = "https://api.foursquare.com/v3/places/search?"

    headers = {
        "accept": "application/json",
        "Authorization": api_key+'='
    }
    params= {
        'categories':'19014',
        "ll" :  f"{landmarks[0]},{landmarks[1]}",
        'radius':5000,
        'limit' : 20,
        
        'fields':'geocodes,name,rating,website,photos,hours,location,tel,description,tips'
    }
    response = requests.get(url, params=params,headers=headers,timeout=5)

    response_text=(response.text)
    jsonto=json.loads(response_text)
    print(jsonto)
    # reslut=jsonto['results']
    # return (reslut)
foursquare_hotels(landmarks=["32.0853","34.7818"])