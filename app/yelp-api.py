# import requests
# from dotenv import load_dotenv
# import os
# import json
# load_dotenv()
# api_key = os.environ.get("API_KEY_YELP")

# url = "https://api.yelp.com/v3/businesses/search"

# headers = {
# "accept": "application/json",
# "Authorization":f"Bearer {api_key}" 
# }
# params= {
#     "location":'paris',
#     "latitude":48.8566,
#     "longitude":2.3522,
#     "radius":8000,
#     "categories":"hotels",
#     "limit":10,
# }

# response = requests.get(url,params=params, headers=headers)

# parsed_data = json.loads(response.text)

# # Access the "businesses" field containing the list of hotels
# hotels = parsed_data.get("businesses", [])

# # Extract relevant information from each hotel
# for hotel in hotels:
#     name = hotel.get("name", "")
#     rating = hotel.get("rating", "")
#     image_url=hotel.get("image_url","")
#     landmarks=hotel.get("coordinates","")
#     url=hotel.get("url","")
#     address = ", ".join(hotel.get("location", {}).get("display_address", []))

#     print(f"Hotel Name: {name}")
#     print(f"Rating: {rating}")
#     print(f"Address: {address}")
#     print(f"photo: {image_url}")
#     print(f"landmarks: {landmarks}")
#     print(f"url: {url}")
#     print("---")