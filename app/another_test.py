import requests

def get_driving_distance(api_key, origin_coords, destination_coords):
    url1=f'https://maps.googleapis.com/maps/api/directions/json?destination={destination_coords}&origin={origin_coords}&key={api_key}'
    response = requests.get(url1)
    data = response.json()
    print(data)


my_api_key = "AIzaSyAbnt3oN_YRb9fzxvai7xGbPBkgGSTg91U"
start_coords = (32.0853, 34.7818)  # Example starting coordinates
end_coords = (31.7683, 35.2137)   # Example destination coordinates

distance = get_driving_distance(my_api_key, start_coords, end_coords)
print(f"Driving distance: {distance}")
