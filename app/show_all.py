from app.chat import process_attractions, process_restaurants
from app.models import Attraction,Restaurant,City
from django.http import JsonResponse
from geopy.distance import geodesic
from rest_framework.decorators import api_view
from app.serializer import SerializerAttractions,SerializerRestaurant
from django.core.cache import cache
from django.views.decorators.cache import cache_page

@cache_page(36000)
@api_view(['POST'])
def show_all_attractions(request):
    
    if request.method == 'POST':
        cityID=request.data.get('city_id')
        cache_key = f"serializer_attractions_{cityID}"
        show_all_attractions_cache=cache.get(cache_key)
        if show_all_attractions_cache is None:
            # Access JSON data from request.data for POST requests
            # lon = request.data.get('longitude')
            # lat = request.data.get('latitude')
            # radius = request.data.get('radius', 10)
            # print(radius)
            # center_point = (float(lat), float(lon))
            # all_attractions = [
            #     obj for obj in Attraction.objects.all() if
            #     geodesic(center_point, (obj.latitude, obj.longitude)).km <= radius
            # ]
            all_attractions=Attraction.objects.filter(city_id=cityID)
            serializer = SerializerAttractions(all_attractions, many=True)
            answer=serializer.data
            if len (answer)==0:
                city=City.objects.filter(id=cityID).first()
                answer=process_attractions(landmarks=[city.latitude,city.longitude], city_name=city.city, country=city.country, city_obj=city)
            cache.set(cache_key, answer, timeout=7 * 24 * 60 * 60)
            return JsonResponse(answer, status=200,safe=False)
        else:
            print('show all attraction cache')
            return JsonResponse(show_all_attractions_cache,safe=False)

    
@cache_page(36000)
@api_view(['POST'])
def show_all_restaurants(request):
    if request.method == 'POST':
        cityID=request.data.get('city_id')
        cache_key = f"serializer_restaurants_{cityID}"
        show_all_restaurants_cache=cache.get(cache_key)
        if show_all_restaurants_cache is None:
        # Access JSON data from request.data for POST requests
            # lon = request.data.get('longitude')
            # lat = request.data.get('latitude')
            # radius = request.data.get('radius', 10)
            # center_point = (lat, lon)

            # all_restaurants = [
            #     obj for obj in Attraction.objects.all() if
            #     geodesic(center_point, (obj.latitude, obj.longitude)).km <= radius
            # ]
            all_restaurants=Restaurant.objects.filter(city_id=cityID)

            serializer = SerializerRestaurant(all_restaurants, many=True)
            answer=serializer.data
            if len (answer)==0:
                city=City.objects.filter(id=cityID).first()
                answer=process_restaurants(landmarks=[city.latitude,city.longitude], city_name=city.city, city_obj=city)
            cache.set(cache_key, answer, timeout=7 * 24 * 60 * 60)
            return JsonResponse(answer, status=200,safe=False)
        else:
            JsonResponse(show_all_restaurants,safe=False)