from django.shortcuts import render
from rest_framework import generics
from .models import Place
from .serializer import PlaceSerializer
from .permissions import IsOwnerOrReadOnly

class PlaceList(generics.ListCreateAPIView):
  # permission_classes = (IsOwnerOrReadOnly,)
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer

class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
  # permission_classes = (IsOwnerOrReadOnly,)
  queryset = Place.objects.all()
  serializer_class = PlaceSerializer
