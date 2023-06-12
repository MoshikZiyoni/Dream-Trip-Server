# # import json
# # import os
# # import time
# # import openai
# # from dotenv import load_dotenv
# # import requests
# # from urllib.parse import quote
# # load_dotenv()
# # key = os.environ.get('TRIP_ADVISOR_KEY')

# # city_name = 'jerusalem'
# # landmarks = [31.7776, 35.2344]
# # print("City:", city_name, landmarks)
# # url = f"https://api.content.tripadvisor.com/api/v1/location/nearby_search?"
# # headers = {"accept": "application/json"}
# # params = {
# #     'latLong': quote(f"{landmarks[0]}, {landmarks[1]}"),  # URL-encode the latLong values
# #     'key' : {key},
# #     # 'searchQuery': city_name+country,
# #     'category': 'attractions,restaurants',
# #     'radius': '5',
# #     'radiusUnit':'km',
# #     'language' : 'en'
# # }
# # full_url = requests.Request('GET', url, params=params).prepare().url
# # print("Full URL:", full_url)
# # response = requests.get(url, headers=headers, params=params)
# # print(response)



# {
#   "country": "Israel",
#   "cities": [
#     {
#       "city": "Jerusalem",
#       "description": "Jerusalem is one of the oldest cities in the world with a rich history, holy sites, and a rich cultural heritage. It is the spiritual center of Judaism, Christianity, and Islam.",
#       "landmarks": [
#         31.778345,
#         35.225078
#       ],
#       "travelDay": 1,
#       "attractions": [
#         {
#           "location_id": "325133",
#           "name": "Notre Dame (Jerusalem)",
#           "distance": "0.13988998098329575",
#           "bearing": "northeast",
#           "address_obj": {
#             "street1": "HaTsanhanim Rd. 3",
#             "street2": "",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "9120402",
#             "address_string": "HaTsanhanim Rd. 3, Jerusalem 9120402 Israel"
#           }
#         },
#         {
#           "location_id": "21020997",
#           "name": "Jerusalem City Hall Visitor Center",
#           "distance": "0.14713812145642557",
#           "bearing": "north",
#           "address_obj": {
#             "street1": "Safra Square 3",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "address_string": "Safra Square 3, Jerusalem Israel"
#           }
#         },
#         {
#           "location_id": "8809383",
#           "name": "HaimToGo",
#           "distance": "0.11522842738752362",
#           "bearing": "north",
#           "address_obj": {
#             "street1": "Ta Doar 11596",
#             "street2": "Gilo",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "9111402",
#             "address_string": "Ta Doar 11596 Gilo, Jerusalem 9111402 Israel"
#           }
#         },
#         {
#           "location_id": "19912602",
#           "name": "Israel in Color",
#           "distance": "0.08677132298413011",
#           "bearing": "northwest",
#           "address_obj": {
#             "street1": "Jaffa Gate",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "9414105",
#             "address_string": "Jaffa Gate, Jerusalem 9414105 Israel"
#           }
#         },
#         {
#           "location_id": "17424676",
#           "name": "Nissim Slama - Guide et Conferencier - Tour Guide & Lecturer",
#           "distance": "0.07812943663584473",
#           "bearing": "northwest",
#           "address_obj": {
#             "street1": " Jaffa Gate 1",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "9250307",
#             "address_string": "Jaffa Gate 1, Jerusalem 9250307 Israel"
#           }
#         },
#         {
#           "location_id": "13378465",
#           "name": "Easy driver",
#           "distance": "0.02493240123759995",
#           "bearing": "east",
#           "address_obj": {
#             "street1": "Yaffo gate",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "44828",
#             "address_string": "Yaffo gate, Jerusalem 44828 Israel"
#           }
#         },
#         {
#           "location_id": "10364745",
#           "name": "I Am Jerusalem",
#           "distance": "0.06366760701206406",
#           "bearing": "south",
#           "address_obj": {
#             "street1": "Rehov Yizhak Kariv 6",
#             "street2": "Sderot Mamilla",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "94106",
#             "address_string": "Rehov Yizhak Kariv 6 Sderot Mamilla, Jerusalem 94106 Israel"
#           }
#         },
#         {
#           "location_id": "12693202",
#           "name": "Artmosphere Gallery",
#           "distance": "0.07087016432443383",
#           "bearing": "south",
#           "address_obj": {
#             "street1": "Alrov Mamilla Avenue",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "94149",
#             "address_string": "Alrov Mamilla Avenue, Jerusalem 94149 Israel"
#           }
#         },
#         {
#           "location_id": "2613077",
#           "name": "Mamilla Mall",
#           "distance": "0.05282990829748297",
#           "bearing": "southwest",
#           "address_obj": {
#             "street2": "",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "",
#             "address_string": "Jerusalem Israel"
#           }
#         },
#         {
#           "location_id": "1758011",
#           "name": "Pontifical Institute Notre Dame of Jerusalem Center - The Shroud Exhibition",
#           "distance": "0.12735931013822174",
#           "bearing": "northeast",
#           "address_obj": {
#             "street1": "Paratroopers Road #3",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "91204",
#             "address_string": "Paratroopers Road #3, Jerusalem 91204 Israel"
#           }
#         }
#       ],
#       "restaurants": [
#         {
#           "location_id": "25409632",
#           "name": "Segafredo Zanetti",
#           "distance": "0.08991504051149923",
#           "bearing": "northeast",
#           "address_obj": {
#             "street1": "New Gate",
#             "street2": "4",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "address_string": "New Gate 4, Jerusalem Israel"
#           }
#         },
#         {
#           "location_id": "17804627",
#           "name": "Churros Cafe",
#           "distance": "0.09198402799255909",
#           "bearing": "northeast",
#           "address_obj": {
#             "street1": "Freres_ Street, New Gate, Old City",
#             "street2": "New Gate, Old City",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "address_string": "Freres_ Street, New Gate, Old City New Gate, Old City, Jerusalem Israel"
#           }
#         },
#         {
#           "location_id": "21117245",
#           "name": "La Patisserie Abu Seir",
#           "distance": "0.09198402799255909",
#           "bearing": "northeast",
#           "address_obj": {
#             "street1": "New Gate 35",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "address_string": "New Gate 35, Jerusalem Israel"
#           }
#         },
#         {
#           "location_id": "23688878",
#           "name": "The Gateway",
#           "distance": "0.08862915135710481",
#           "bearing": "northeast",
#           "address_obj": {
#             "street1": "New Gate 9 , Jerusalem",
#             "street2": "Old City",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "9610316",
#             "address_string": "New Gate 9 , Jerusalem Old City, Jerusalem 9610316 Israel"
#           }
#         },
#         {
#           "location_id": "15835588",
#           "name": "EatWith: Osnat of Jerusalem",
#           "distance": "0.1758222427039205",
#           "bearing": "north",
#           "address_obj": {
#             "city": "Jerusalem",
#             "country": "Israel",
#             "address_string": "Jerusalem Israel"
#           }
#         },
#         {
#           "location_id": "1057301",
#           "name": "Cheese & Wine Rooftop Restaurant",
#           "distance": "0.12321867165590981",
#           "bearing": "north",
#           "address_obj": {
#             "street1": "Paratroopers Street 3",
#             "street2": "Notre Dame",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "91204",
#             "address_string": "Paratroopers Street 3 Notre Dame, Jerusalem 91204 Israel"
#           }
#         },
#         {
#           "location_id": "11530302",
#           "name": "Lebanese Restaurant",
#           "distance": "0.07812943663584473",
#           "bearing": "northwest",
#           "address_obj": {
#             "street1": "8 David",
#             "street2": "Jaffa Gate, Old City",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "9534700",
#             "address_string": "8 David Jaffa Gate, Old City, Jerusalem 9534700 Israel"
#           }
#         },
#         {
#           "location_id": "4291253",
#           "name": "Tomato",
#           "distance": "0.016687204519773995",
#           "bearing": "east",
#           "address_obj": {
#             "street1": "Malka shalmazion",
#             "street2": "Close to Yafo",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "address_string": "Malka shalmazion Close to Yafo, Jerusalem Israel"
#           }
#         },
#         {
#           "location_id": "7789289",
#           "name": "Cafe Greg",
#           "distance": "0.058959933980328824",
#           "bearing": "south",
#           "address_obj": {
#             "street1": "26 General Pierre Koenig",
#             "street2": "Hadar Mall",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "postalcode": "9346934",
#             "address_string": "26 General Pierre Koenig Hadar Mall, Jerusalem 9346934 Israel"
#           }
#         },
#         {
#           "location_id": "10797732",
#           "name": "Greg Cafe",
#           "distance": "0.05956815915262635",
#           "bearing": "south",
#           "address_obj": {
#             "street1": "Rehov Yitshak Kariv 6",
#             "street2": "Mamila Mall",
#             "city": "Jerusalem",
#             "country": "Israel",
#             "address_string": "Rehov Yitshak Kariv 6 Mamila Mall, Jerusalem Israel"
#           }
#         }
#       ]
#     }
#   ]
# }
# from geopy.geocoders import Nominatim

# geolocator = Nominatim(user_agent="your_app_name")

# # location = geolocator.geocode("1600 Amphitheatre Parkway, Mountain View, CA")
# # latitude = location.latitude
# # longitude = location.longitude

# # print (latitude,longitude)

# # attraction={'location_id': '24135714', 'name': "Museo Dell'Arte Salvata", 'distance': '0.15103240380361369', 'bearing': 'east', 'address_obj': {'street1': 'Via Giuseppe Romita 8', 'street2': 'Octagon Hall Of The National Roman Museum', 'city': 'Rome', 'country': 'Italy', 'postalcode': '00185', 'address_string': 'Via Giuseppe Romita 8 Octagon Hall Of The National Roman Museum, 00185 Rome Italy'}} 

# # {'location_id': '23586841', 'name': 'The Lodge Club Firenze', 'distance': '0.14052398442976793', 'bearing': 'northeast', 'address_obj': {'street1': 'Viale Giuseppe Poggi 1', 'city': 'Florence', 'state': 'Province of Florence', 'country': 'Italy', 'postalcode': '50125', 'address_string': 'Viale Giuseppe Poggi 1, 50125, Florence Italy'}}


# # address_obj = attraction['address_obj']
# # if 'street1' in address_obj and 'city' in address_obj and 'country' in address_obj:
# #     street = address_obj['street1']
# #     city = address_obj['city']
# #     country = address_obj['country']
# #     address_string = f"{street}, {city}, {country}"
# #     location = geolocator.geocode(address_string)
# #     latitude = location.latitude
# #     longitude = location.longitude
# #     print(f"Latitude: {latitude}, Longitude: {longitude}")


# location = geolocator.geocode("Prat de la Creu,andorra de vella,Andora")



latitude = -8.7776416
longitude = 13.2432628
landmarks=latitude,longitude

landmark_name = 'Place des Jacobins'
def flickr_api(attraction_name,latitude,longitude):
  import flickrapi
  api_key ='bf2ed6da714a97beef541c4708d527fa'
  api_secret = 'e2593a81ffab5ade'
  image_list = []
  flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
  # Search for photos by tags (landmark name)
  photos = flickr.photos.search(text=attraction_name, per_page=5, extras='url_o',sort='relevance')
  if len(photos['photos']['photo']) == 0:
        print (0)
        # No photos found for the attraction name, search by latitude and longitude
        photos = flickr.photos.search(lat=latitude, lon=longitude, per_page=5, extras='url_o', sort='relevance')

        if len(photos['photos']['photo']) == 0:
            print('No photos found for the attraction')
  # Extract the photo URLs
  if 'photos' in photos and 'photo' in photos['photos']:
      for photo in photos['photos']['photo']:
          photo_id = photo['id']  # URL of the original-sized photo
          flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
          # Get the sizes of the photo
          sizes = flickr.photos.getSizes(photo_id=photo_id)
          # Extract the URL of the image
          if 'sizes' in sizes and 'size' in sizes['sizes']:
              # Assuming you want the URL of the largest available size
              largest_size = sizes['sizes']['size'][-1]
              image_url = largest_size['source']
              image_list.append(image_url)
          else:
              print('No image URL available for the photo')
  return(image_list)

print (flickr_api(attraction_name="Mus\u00e9e des Beaux-Arts de Lyon", latitude= 45.767018, longitude= 4.833468))
