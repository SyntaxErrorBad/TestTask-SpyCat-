from rest_framework import serializers
from ..models import Cat
from .mission import MissionSerializer

import requests


class CatSerializer(serializers.ModelSerializer):
    mission = MissionSerializer(read_only=True)

    class Meta:
        model = Cat
        fields = ['id', 'name', 'age', 'breed', 'salary', 'status', 'mission']

    def validate_breed(self, value):
        url = 'https://api.thecatapi.com/v1/breeds'
        response = requests.get(url)
        if response.status_code != 200:
            raise serializers.ValidationError('Failed to fetch breeds.')
        items = response.json()
        # проверяем, существует ли такая порода
        if any(item['name'] == value for item in items):
            return value
        raise serializers.ValidationError('Wrong Breed!')

