from rest_framework import serializers
from gpt_app.app.models import Search


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'