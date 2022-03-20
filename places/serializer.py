from rest_framework import serializers
from .models import Place

class PlaceSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'visitor', 'visit', 'description', 'created_at', 'updated_at')
    model = Place
