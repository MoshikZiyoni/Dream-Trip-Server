
import json
import requests
from dotenv import load_dotenv
import os
import flickrapi

load_dotenv()


            
def flickr_api(name,latitude,longitude):
  api_key =os.environ.get('flickr_key')
  api_secret =os.environ.get('flickr_secret')
  image_list = []
  flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')
  # Search for photos by tags (landmark name)
  photos = flickr.photos.search(text=name, per_page=1, extras='url_o',sort='relevance')
  if len(photos['photos']['photo']) == 0:
    # No photos found for the attraction name, search by latitude and longitude
    photos = flickr.photos.search(lat=latitude, lon=longitude, per_page=1, extras='url_o', sort='relevance')
    print ("len is 0")
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
              return image_url
            #   image_list.append(image_url)
          else:
              return (image_url=="")
# print(flickr_api(name="Manta Ray",latitude= 32.0853,longitude= 34.7818))

api_key_foursqaure=os.environ.get('FOURSQUARE')

def foursquare_restaurant(landmarks):
    url = "https://api.foursquare.com/v3/places/search?"
    try:
        headers = {
            "accept": "application/json",
            "Authorization": api_key_foursqaure+'='
        }
        query= {
            # 'query': f"attractions in {city_name},{country}",
            'categories':'13000',
            "ll" :  f"{landmarks[0]},{landmarks[1]}",
            'radius':5000,
            'limit' : 20,
            'fields':'geocodes,name,rating,price,website,photos,social_media,menu,hours,location,tel,tastes,tips,categories'
        }
        response = requests.get(url, params=query,headers=headers)

        response_text=(response.text)
        jsonto=json.loads(response_text)
        reslut=jsonto['results']
        return (reslut)
    except:
        headers = {
            "accept": "application/json",
            "Authorization": api_key_foursqaure
        }
        query= {
            # 'query': f"attractions in {city_name},{country}",
            'categories':'13000',
            "ll" :  f"{landmarks[0]},{landmarks[1]}",
            'radius':5000,
            'limit' : 20,
            'fields':'geocodes,name,rating,price,website,photos,social_media,menu,hours,location,tel,tastes,tips,categories'
        }
        response = requests.get(url, params=query,headers=headers)

        response_text=(response.text)
        jsonto=json.loads(response_text)
        reslut=jsonto['results']
        return (reslut)

def foursquare_attraction(landmarks,city_name,country):
    url1 = "https://api.foursquare.com/v3/places/search?"
    try:
        headers = {
            "accept": "application/json",
            "Authorization": api_key_foursqaure+'='
        }

        query1= {
            'query': f"attractions in {city_name},{country}",
            'categories':'10027,10025,10055,10068,16000',
            "ll" :  f"{landmarks[0]},{landmarks[1]}",
            'radius':8000,
            'limit' : 20,
            'fields':'description,geocodes,name,rating,distance,website,photos,menu,hours_popular,hours,location,tel,tips'

        }
        response1 = requests.get(url1, params=query1,headers=headers)

        response_text1=(response1.text)
        jsonto1=json.loads(response_text1)
        reslut=jsonto1['results']
        # print('Attracion reslut!!!!!! : ',reslut)
        return reslut
    except:
        headers = {
            "accept": "application/json",
            "Authorization": api_key_foursqaure
        }

        query1= {
            'query': f"attractions in {city_name},{country}",
            'categories':'10027,10025,10055,10068,16000',
            "ll" :  f"{landmarks[0]},{landmarks[1]}",
            'radius':8000,
            'limit' : 20,
            'fields':'description,geocodes,name,rating,distance,website,photos,menu,hours_popular,hours,location,tel,tips'

        }
        response1 = requests.get(url1, params=query1,headers=headers)

        response_text1=(response1.text)
        jsonto1=json.loads(response_text1)
        reslut=jsonto1['results']
        # print('Attracion reslut!!!!!! : ',reslut)
        return reslut

def foursquare_hotels(landmarks):
    try:
        url = "https://api.foursquare.com/v3/places/search?"

        headers = {
            "accept": "application/json",
            "Authorization": api_key_foursqaure+'='
        }
        query= {
            'categories':'19014',
            "ll" :  f"{landmarks[0]},{landmarks[1]}",
            'radius':5000,
            'limit' : 20,
            
            'fields':'geocodes,name,rating,website,photos,hours,location,tel,description,tips'
        }
        response = requests.get(url, params=query,headers=headers,timeout=5)
        
        response_text=(response.text)
        jsonto=json.loads(response_text)
        reslut=jsonto['results']
        return (reslut)
    except:
        url = "https://api.foursquare.com/v3/places/search?"

        headers = {
            "accept": "application/json",
            "Authorization": api_key_foursqaure
        }
        query= {
            'categories':'19014',
            "ll" :  f"{landmarks[0]},{landmarks[1]}",
            'radius':5000,
            'limit' : 20,
            
            'fields':'geocodes,name,rating,website,photos,hours,location,tel,description,tips'
        }
        response = requests.get(url, params=query,headers=headers,timeout=5)
        
        response_text=(response.text)
        jsonto=json.loads(response_text)
        reslut=jsonto['results']
        return (reslut)



def foursquare_night_life(landmarks):
    url = "https://api.foursquare.com/v3/places/search?"
    try:
        headers = {
            "accept": "application/json",
            "Authorization": api_key_foursqaure+'='
        }
        query= {
            'categories':'10032',
            "ll" :  f"{landmarks[0]},{landmarks[1]}",
            'radius':5000,
            'limit' : 20,
            
            'fields':'geocodes,name,rating,website,photos,hours,location,tel,description,tips'
        }
        response = requests.get(url, params=query,headers=headers,timeout=5)

        response_text=(response.text)
        jsonto=json.loads(response_text)
        reslut=jsonto['results']
        return (reslut)
    except:
        headers = {
            "accept": "application/json",
            "Authorization": api_key_foursqaure
        }
        query= {
            'categories':'10032',
            "ll" :  f"{landmarks[0]},{landmarks[1]}",
            'radius':5000,
            'limit' : 20,
            
            'fields':'geocodes,name,rating,website,photos,hours,location,tel,description,tips'
        }
        response = requests.get(url, params=query,headers=headers,timeout=5)

        response_text=(response.text)
        jsonto=json.loads(response_text)
        reslut=jsonto['results']
        return (reslut)


def my_night_life(landmarks):
    url=os.environ.get('night_life_url')
    query={
        "latitude": landmarks[0],
        "longitude": landmarks[1], 
    }
    try:
        response = requests.get(url, json=query, timeout=3)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        response_text = response.text
        jsonto = json.loads(response_text)
    except requests.Timeout:
        # Handle timeout (no response within 3 seconds)
        print ('timeout for nightlife')
        jsonto = {'night_life': ''}
    except requests.RequestException as e:
        # Handle other request exceptions (e.g., network error)
        print(f"Request Exception: {e}")
        jsonto = {'night_life': ''}
    
    if len(jsonto) <= 0:
        jsonto = {'night_life': ''}
    return jsonto


def sunset_api(landmarks):
    url=os.environ.get('sunset_api')
    query={
        "latitude": landmarks[0],
        "longitude": landmarks[1], 
    }
    try:
        response = requests.post(url, json=query, timeout=3)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        response_text = response.text
        jsonto = json.loads(response_text)
        # print (response_text)
    except requests.Timeout:
        print ('timeout for sunset')
        jsonto = {'sunset': ''}
    except requests.RequestException as e:
        print(f"Request Exception: {e}")
        jsonto = {'sunset': ''}
    
    if len(jsonto) <= 0:
        jsonto = {'sunset': ''}
        
    # print ('sunset!!!!!',jsonto)
    return jsonto



