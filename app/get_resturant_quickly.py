# def foursquare_restaurant(city,landmark):
#         api_key=os.environ.get('FOURSQUARE')
#         url = "https://api.foursquare.com/v3/places/search?"
#         print(landmark[0])
#         headers = {
#             "accept": "application/json",
#             "Authorization": api_key
#         }

#         query = {
#             'categories': '13000',
#             "ll" :  f"{landmark[0]},{landmark[1]}",
#             'radius': 5000,
#             'limit': 10,
#             'fields':'distance,geocodes,name,rating,price,distance,website,photos,social_media,menu'
#         }

#         response = requests.get(url, params=query, headers=headers)
#         response_text = response.text
#         jsonto = json.loads(response_text)
#         results = jsonto['results']
#         city_obj = City.objects.filter(city=city).first()
#         if not city_obj:
#             pass
#         for i in results:
#             process_restaurant(city_obj=city_obj,restaur=i,restaurants=[])

#     def get_landmarks(city):
#         landmarks = {  # Example landmarks for Nantes, France
#         "Strasbourg": [48.5839, 7.7455],  # Example landmarks for Strasbourg, France
#         "Bordeaux": [44.8378, -0.5792],  # Example landmarks for Bordeaux, France
#         "Berlin": [52.5200, 13.4050],  # Example landmarks for Berlin, Germany
#         "Hamburg": [53.5511, 9.9937],  # Example landmarks for Hamburg, Germany
#         "Munich": [48.1351, 11.5820],  # Example landmarks for Munich, Germany
#     }
#         return landmarks.get(city, [])

#     # Example usage
#     cities = [
#         "Vienna",
        
#     ]

#     for city in cities:
#         landmark = get_landmarks(city)
#         print(landmark,'first')
#         foursquare_restaurant(city,landmark)

#     return 'ok'







