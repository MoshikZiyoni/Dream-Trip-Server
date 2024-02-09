import requests,json
origin_lat = 40.7234 
origin_lon = -74.0060

destination_lat = 40.7589
destination_lon = -73.9851

api_key='05jhyj9cq8O8PmAJfXGMECLLa9i3t6qH'
# url = "https://api.transit.land/api/v1/plan"
# url = "https://transit.land/api/v2/rest/"
url = "https://transit.land/api/v2/rest/stops.geojson"


headers = {"Authorization": f"Token {api_key}"} 


# params = {"from": {"lat": origin_lat, "lon": origin_lon},
#         "to": {"lat": destination_lat, "lon": destination_lon},
#         "apikey":api_key
#         }
# params={
#     "bbox": "-122.4194,37.7749,-122.4080,37.7858",
#     "per_page": 100,
#     "api_key":api_key
# }
params={
    # "bbox": "34.7818064,32.0852997,34.7809,32.0853",
    "bbox": "34.732,32.055,34.855,32.146",

    "per_page": 100,
    "api_key":api_key
}
response = requests.get(url, params=params)

data=(response.json())
print(data)
# features = data['features']

# # Loop through each feature
# for feature in features:

#   # Extract properties
#   properties = feature['properties']

#   # Extract individual properties  
#   stop_name = properties['stop_name']
#   location_type = properties['location_type']
#   coordinates = feature['geometry']['coordinates']

#   # Print out values
#   print("stop_name: ",stop_name,"---", "location_type: ",location_type,"---", "coordinates: ",coordinates)
# plan = response.json()

# options = plan["plan"]["itineraries"]

# for option in options:
#    print(option["legs"][0]["route"]["agency"]["name"])