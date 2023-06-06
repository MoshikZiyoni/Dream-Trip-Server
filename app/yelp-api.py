# #  API_ENDPOINT_YELP = 'https://api.yelp.com/v3/businesses/search'
# #                 API_KEY_YELP=os.environ.get('API_KEY_YELP')
# #                 headers = {
# #                     'Authorization': f'Bearer {API_KEY_YELP}'
# #                 }
# #                 params = {
# #                     'location': city,
# #                     'latitude': landmarks[0],  # Replace with the actual latitude value
# #                     'longitude': landmarks[1],
# #                     'term': 'restaurants',
# #                     'radius': 1000,  # Set the desired radius in meters
# #                     'categories': 'restaurants',  # Limit results to the "restaurants" category
# #                     'limit': 10,  # Set the number of results to return
# #                     'sort_by': 'best_match'  # Sort the results by best match
# #                 }
# #                 response = requests.get(API_ENDPOINT_YELP, headers=headers, params=params)
# #                 if response.status_code == 200:
# #                     result = response.json()
# #                     businesses=result['businesses']
# #                     print (businesses)
# #                     name = result['name']
# #                     image = result['image']
# #                     price = result['price']
                    
# #                     # Process the result as needed
# #                 else:
# #                     print('Error occurred:', response.status_code)



# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# ###CHAT
# city_name='TLV'
# landmarks= [32.0853,34.781769]
# API_ENDPOINT_YELP = 'https://api.yelp.com/v3/businesses/search'
# API_KEY_YELP=os.environ.get('API_KEY_YELP')
# headers = {
#     'Authorization': f'Bearer {API_KEY_YELP}'
# }
# params = {
#      "location": "Paris",
#     "latitude": 48.8566,
#     "longitude": 2.3522,
#     'term': 'restaurants',
#     'radius': 40000,  # Set the desired radius in meters
#     'categories': 'restaurants',  # Limit results to the "restaurants" category
#     'limit': 10,  # Set the number of results to return
#     'sort_by': 'best_match'  # Sort the results by best match
# }
# response = requests.get(API_ENDPOINT_YELP, headers=headers, params=params)
# if response.status_code == 200:
#     result = response.json()
#     print (result)
#     # Process the result as needed
# else:
#     print('Error occurred:', response.status_code)