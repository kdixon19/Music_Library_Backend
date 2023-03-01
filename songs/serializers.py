from rest_framework import serializers
from .models import Songs


#Serializer file, converts models into JSON objects and vice versa

class Serializer (serializers.ModelSerializer):
    class Meta:
        model = Songs
        field = ['title', 'artist','album','release_date','genre']
        depth = 1