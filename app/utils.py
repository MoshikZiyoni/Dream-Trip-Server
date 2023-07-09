from app.models import Attraction, Restaurant
from app.trip_advisor import flickr_api
from app.wikipediaapi import process_query
import json
from datetime import datetime, timedelta

def process_attraction(attrac, city_obj, attractions):
    name1 = attrac.get("name", "")
    distance1 = attrac.get("distance", "")
    latitude1 = (
        attrac["geocodes"]["main"]["latitude"]
        if "geocodes" in attrac
        and "main" in attrac["geocodes"]
        and "latitude" in attrac["geocodes"]["main"]
        else ""
    )
    longitude1 = (
        attrac["geocodes"]["main"]["longitude"]
        if "geocodes" in attrac
        and "main" in attrac["geocodes"]
        and "longitude" in attrac["geocodes"]["main"]
        else ""
    )
    rating1 = attrac.get("rating", "0")
    website1 = attrac.get("website", "")
    hours_popular1 = attrac.get("hours_popular", "")
    description = attrac.get("description", "")
    distance1=attrac.get("distance","")
    if len(description)==0:
            try:
                wiki=process_query(name1)
                description=wiki[0]
                print ('descrption from wiki')
            except:
                 print ('descrption from wiki not gooodddddddddddddddd')
    photos1 = attrac.get("photos", "")
    if photos1:
        first_photo = photos1[0]
        prefix = first_photo.get("prefix", "")
        suffix = first_photo.get("suffix", "")
        url1 = f"{prefix}original{suffix}"
        photos1=url1
        
    else:
        photos1 = flickr_api(name1, latitude1, longitude1)
    

    attraction_info = {
        "name": name1,
        "latitude": latitude1,
        "longitude": longitude1,
        "photos": photos1,
        "review_score": rating1,
        "website": website1,
        "hours_popular": hours_popular1,
        "description": description,
        "distance":distance1,
    }

    attractions.append(attraction_info)
    atrc_query = Attraction(
        name=name1,
        city=city_obj,
        latitude=latitude1,
        longitude=longitude1,
        photos=photos1,
        review_score=rating1,
        description=description,
        website=website1,
        hours_popular=hours_popular1,
        distance=distance1
    )
    atrc_query.save()
    print("Save attraction successfully")


def process_restaurant(restaur, city_obj, restaurants):
    name = restaur.get("name", "")
    distance = restaur.get("distance", "")
    latitude = (
        restaur["geocodes"]["main"]["latitude"]
        if "geocodes" in restaur
        and "main" in restaur["geocodes"]
        and "latitude" in restaur["geocodes"]["main"]
        else ""
    )
    longitude = (
        restaur["geocodes"]["main"]["longitude"]
        if "geocodes" in restaur
        and "main" in restaur["geocodes"]
        and "longitude" in restaur["geocodes"]["main"]
        else ""
    )
    rating = restaur.get("rating", "0")
    price = restaur.get("price", "")
    website = restaur.get("website", "")
    social_media = restaur.get("social_media", "")
    try:
        instagram_handle = social_media.get("instagram", "")
        social_media = instagram_handle
    except:
        social_media = ""
        print ('no insta')
    menu = restaur.get("menu", "")
    hours_popular = restaur.get("hours_popular", "")
    distance=restaur.get("distance","")
    photos = restaur.get("photos", "")
    if photos:
        first_photo = photos[0]
        prefix = first_photo.get("prefix", "")
        suffix = first_photo.get("suffix", "")
        url = f"{prefix}original{suffix}"
        photos=url
    else:
        photos = flickr_api(name, latitude, longitude)
    restaurant_info = {
        "name": name,
        "latitude": latitude,
        "longitude": longitude,
        "photos": photos,
        "review_score": rating,
        "price": price,
        "website": website,
        "social_media": social_media,
        "menu": menu,
        "distance":distance,
        # "hours_popular": hours_popular,
    }
    restaurants.append(restaurant_info)
    resta_query = Restaurant(
        name=name,
        city=city_obj,
        latitude=latitude,
        longitude=longitude,
        photos=photos,
        review_score=rating,
        menu=menu,
        social_media=social_media,
        website=website,
        price=price,
        distance=distance
    )
    resta_query.save()
    print("Save restaurants successfully")




# def extract_data_from_combined_data(data):
#     # Extract the necessary information and create a new variable
#     extracted_data = {
#         "country": data["country"],
#         "cities": []
#     }

#     for city in data["cities"]:
#         city_data = {
#             "city": city["city"],
#             "attractions": [],
#             "restaurants": []
#         }
        
#         for attraction in city["attractions"]:
#             attraction_data = {
#                 "name": attraction["name"],
#                 "distance": attraction["distance"]
#             }
#             city_data["attractions"].append(attraction_data)
        
#         for restaurant in city["restaurants"]:
#             restaurant_data = {
#                 "name": restaurant["name"],
#                 "distance": restaurant["distance"]
#             }
#             city_data["restaurants"].append(restaurant_data)
        
#         extracted_data["cities"].append(city_data)

#     # Print the extracted data
#     # print((extracted_data))
#     return extracted_data


# from datetime import datetime, timedelta

# def create_schedule(data):
#     schedule = []
#     start_time = datetime.strptime('09:00', '%H:%M')
#     end_time = datetime.strptime('20:00', '%H:%M')
#     lunch_start_time = datetime.strptime('14:00', '%H:%M')
#     lunch_end_time = datetime.strptime('16:00', '%H:%M')

#     for city_data in data['cities']:
#         city = city_data['city']
#         attractions = city_data['attractions']
#         restaurants = city_data['restaurants']

#         city_schedule = {'city': city, 'attractions': [], 'restaurants': []}
#         current_time = start_time

#         for attraction in attractions:
#             name = attraction['name']
#             duration = timedelta(hours=2)

#             if current_time + duration <= end_time:
#                 lunch_restaurant = find_closest_restaurant(attraction, restaurants)
#                 city_schedule['attractions'].append({
#                     'name': name,
#                     'start_time': current_time.strftime('%H:%M'),
#                     'end_time': (current_time + duration).strftime('%H:%M'),
#                     'restaurant': lunch_restaurant
#                 })
#                 current_time += duration

#                 # Check if it's time for lunch break
#                 if current_time >= lunch_start_time and current_time < lunch_end_time:
#                     current_time = lunch_end_time
#             else:
#                 break

#         # Remaining restaurants added to the list
#         city_schedule['restaurants'] = restaurants

#         schedule.append(city_schedule)
#     print (schedule,'AAAA')
#     return schedule


# def find_closest_restaurant(attraction, restaurants):
#     attraction_distance = attraction['distance']
#     closest_restaurant = None
#     closest_distance = float('inf')

#     for restaurant in restaurants:
#         restaurant_distance = restaurant['distance']

#         if restaurant_distance < closest_distance:
#             closest_restaurant = restaurant
#             closest_distance = restaurant_distance

#     return closest_restaurant



def generate_schedule(data):
    cities = data['cities']
    num_attractions_per_day = 3
    attraction_duration = timedelta(hours=3)
    lunch_break_start = datetime.strptime('14:00', '%H:%M').time()
    lunch_break_end = datetime.strptime('16:00', '%H:%M').time()
    daily_schedule_end = datetime.strptime('19:00', '%H:%M').time()

    schedule = []

    for city in cities:
        city_name = city['city']
        city_description=city['description']
        attractions = city['attractions']
        restaurants = city['restaurants']
        days_spent = city['days_spent']

        num_attractions = min(len(attractions), num_attractions_per_day * days_spent)
        attractions_per_day = num_attractions // days_spent
        extra_attractions = num_attractions % days_spent

        start_time = datetime(year=1, month=1, day=1, hour=8, minute=0)

        for day in range(days_spent):
            day_schedule = []
            for i in range(attractions_per_day):
                attraction_index = day * attractions_per_day + i
                attraction = attractions[attraction_index]
                attraction_start = start_time + (attraction_duration * i)

                # Add lunch break if within attraction hours
                if lunch_break_start <= attraction_start.time() < lunch_break_end:
                    attraction_start += timedelta(hours=2)

                attraction_end = attraction_start + attraction_duration

                day_schedule.append({
                    'attraction':attraction,
                    # 'attraction': attraction['name'],
                    # 'latitude': attraction['latitude'],
                    # 'longitude': attraction['longitude'],
                    # 'photos': attraction['photos'],
                    # 'review_score': attraction['review_score'],
                    # 'website': attraction['website'],
                    # 'hours_popular': attraction['hours_popular'],
                    # 'description': attraction['description'],
                    'start_time': attraction_start.strftime('%H:%M'),
                    'end_time': attraction_end.strftime('%H:%M')
                })

            # Add extra attraction if available and within the schedule
            if extra_attractions > 0 and day_schedule[-1]['end_time'] < daily_schedule_end.strftime('%H:%M'):
                extra_attraction = attractions[num_attractions - extra_attractions]
                extra_attraction_start = start_time + (attraction_duration * (attractions_per_day + extra_attractions - 1))
                extra_attraction_end = extra_attraction_start + attraction_duration

                if extra_attraction_end.time() <= daily_schedule_end:
                    day_schedule.append({
                        'attraction': extra_attraction['name'],
                        'start_time': extra_attraction_start.strftime('%H:%M'),
                        'end_time': extra_attraction_end.strftime('%H:%M')
                    })
                    extra_attractions -= 1

            # Add lunch break
            lunch_start = datetime.combine(start_time.date(), lunch_break_start)
            lunch_end = datetime.combine(start_time.date(), lunch_break_end)
            day_schedule.append({
                'attraction': 'Lunch Break',
                'start_time': lunch_start.strftime('%H:%M'),
                'end_time': lunch_end.strftime('%H:%M')
            })

            start_time += timedelta(days=1)
            schedule.append({
                'city': city_name,
                'descrption':city_description,
                'day': day + 1,
                'schedule': day_schedule,
                
            })
        schedule.append({
            'restaurants':restaurants
        })
    # print(json.dumps(schedule,indent=2))

    return json.dumps(schedule,indent=2)

