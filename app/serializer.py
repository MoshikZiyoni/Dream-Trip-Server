from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import QueryChatGPT,Attraction,Restaurant


class SerializerQueryChatGPT(serializers.ModelSerializer):
    class Meta:
        model = QueryChatGPT
        fields = '__all__'


class SerializerAttractions(ModelSerializer):
    class Meta:
        model = Attraction
        fields = '__all__'


class SerializerRestaurant(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


   