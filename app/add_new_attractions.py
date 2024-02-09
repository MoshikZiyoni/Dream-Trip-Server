from app.models import CheckNewAttraction,City
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

