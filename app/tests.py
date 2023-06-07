# import json
# import os
# import time
# import openai
# from dotenv import load_dotenv
# import requests
# from urllib.parse import quote
# load_dotenv()
# key = os.environ.get('TRIP_ADVISOR_KEY')

# city_name = 'jerusalem'
# landmarks = [31.7776, 35.2344]
# print("City:", city_name, landmarks)
# url = f"https://api.content.tripadvisor.com/api/v1/location/nearby_search?"
# headers = {"accept": "application/json"}
# params = {
#     'latLong': quote(f"{landmarks[0]}, {landmarks[1]}"),  # URL-encode the latLong values
#     'key' : {key},
#     # 'searchQuery': city_name+country,
#     'category': 'attractions,restaurants',
#     'radius': '5',
#     'radiusUnit':'km',
#     'language' : 'en'
# }
# full_url = requests.Request('GET', url, params=params).prepare().url
# print("Full URL:", full_url)
# response = requests.get(url, headers=headers, params=params)
# print(response)



landmarks= [{'latitude': 40.4168, 'longitude': -3.7038}, {'latitude': 40.4169, 'longitude': -3.7097}]
print (type(landmarks))