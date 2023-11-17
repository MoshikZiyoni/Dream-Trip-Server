from app.models import Attraction,Restaurant
from django.http import JsonResponse
from geopy.distance import geodesic
from rest_framework.decorators import api_view
from app.serializer import SerializerAttractions,SerializerRestaurant

@api_view(['POST'])
def show_all_attractions(request):
    if request.method == 'POST':
        # Access JSON data from request.data for POST requests
        cityID=request.data.get('city_id')
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
        return JsonResponse(serializer.data, status=200,safe=False)
    
    
    
@api_view(['POST'])
def show_all_restaurants(request):
    if request.method == 'POST':
        # Access JSON data from request.data for POST requests
        cityID=request.data.get('city_id')
        lon = request.data.get('longitude')
        lat = request.data.get('latitude')
        radius = request.data.get('radius', 10)
        center_point = (lat, lon)

        # all_restaurants = [
        #     obj for obj in Attraction.objects.all() if
        #     geodesic(center_point, (obj.latitude, obj.longitude)).km <= radius
        # ]
        all_restaurants=Restaurant.objects.filter(city_id=cityID)

        serializer = SerializerRestaurant(all_restaurants, many=True)
        
        return JsonResponse(serializer.data, status=200,safe=False)