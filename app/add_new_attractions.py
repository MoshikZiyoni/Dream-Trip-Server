import time
from app.models import CheckNewAttraction,City,Attraction
from django.http import JsonResponse
from rest_framework.decorators import api_view
import requests
from dotenv import load_dotenv
import os
from unidecode import unidecode
from django.db.models import Q

load_dotenv()

@api_view(['POST'])
def add_new_attraction(request):
    city_name=request.data.get('city_name')
    attraction_name=request.data.get('attraction_name')
    lat=request.data.get('lat')
    lon=request.data.get('lon')
    review_score=request.data.get('review_score','')
    description=request.data.get('description','')
    website=request.data.get('website','')
    price=request.data.get('price','')
    hours=request.data.get('hours','')
    tel=request.data.get('tel','')
    address=request.data.get('address','')
    tips=request.data.get('tips','')
    uploaded_image = request.FILES['image']
    
    normalized_city_name = unidecode(city_name)
    existing_city = City.objects.filter(Q(city__iexact=normalized_city_name) | Q(city__icontains=normalized_city_name)).first()
    if existing_city:

        url = "https://api.imgbb.com/1/upload"
        api_key = os.environ.get('imgbb')
        
        url = 'https://api.imgbb.com/1/upload'
        files = {'image': uploaded_image}
        params = {
            'key': api_key,
        }
        
        response = requests.post(url, files=files, data=params)
        print (response.text)
        photos=(response.json()["data"]["url"])
        print (photos,'@@@@@')

        CheckNewAttraction(
            city=existing_city,
            name=attraction_name,
            latitude=lat,
            longitude=lon,
            description=description,
            review_score=review_score,
            website=website,
            real_price=price,
            hours=hours,
            tel=tel,
            address=address,
            tips=tips,
            photos=photos).save()

        print ('ok')

@api_view(['POST'])
def approve_new_attraction(id):
    id=(id.data['id'])
    new_attraction=CheckNewAttraction.objects.get(id=id)
    # existing_city = City.objects.filter(city__iexact=new_attraction.city )
    # print(existing_city.id)
    # if existing_city:
    Attraction(
        city=new_attraction.city,
            name=new_attraction.name,
            latitude=new_attraction.latitude,
            longitude=new_attraction.longitude,
            description=new_attraction.description,
            review_score=new_attraction.review_score,
            website=new_attraction.website,
            real_price=new_attraction.real_price,
            hours=new_attraction.hours,
            tel=new_attraction.tel,
            address=new_attraction.address,
            tips=new_attraction.tips,
            photos=new_attraction.photos).save()
        
    time.sleep(3)
    new_attraction1=Attraction.objects.filter(name=new_attraction.name)
    print(new_attraction1.id,'@@@@@@@@')
        

