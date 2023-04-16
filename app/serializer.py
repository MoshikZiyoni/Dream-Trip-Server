from rest_framework import serializers
from app.models import QueryChatGPT


class SerializerQueryChatGPT(serializers.ModelSerializer):
    class Meta:
        model = QueryChatGPT
        fields = '__all__'