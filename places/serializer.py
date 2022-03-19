from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ['id', 'visitor', 'place', 'description', 'created_at', 'updated_at', ]
    model = Place
