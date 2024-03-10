from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import QueryChatGPT,Attraction,Restaurant,City


class SerializerQueryChatGPT(serializers.ModelSerializer):
    class Meta:
        model = QueryChatGPT
        fields = '__all__'


class SerializerAttractions(serializers.ModelSerializer):
    city_id = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), source='city')

    class Meta:
        model = Attraction
        fields = ['id', 'name', 'latitude', 'longitude', 'photos', 'review_score', 'description', 'website',
                  'hours_popular', 'distance', 'real_price', 'hours', 'tel', 'address', 'place_id', 'tips', 'city_id']

class SerializerRestaurant(serializers.ModelSerializer):
    city_id = serializers.PrimaryKeyRelatedField(queryset=City.objects.all(), source='city')

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'latitude', 'longitude', 'photos', 'review_score', 'website', 'category', 'price',
                  'tips', 'hours', 'tel', 'address', 'place_id', 'city_id']


   