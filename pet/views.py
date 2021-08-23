from django.shortcuts import render
from . models import Breed , Pet ,Order
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import PetSerializers, OrderSerializers ,BreedSerializers
from rest_framework.response import Response

class pet_list(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializers
    
 
class pet_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializers
   
class order_list(generics.ListCreateAPIView):
    queryset =Order.objects.all()
    serializer_class = OrderSerializers
class breed_list(generics.ListCreateAPIView):
    queryset =Breed.objects.all()
    serializer_class = BreedSerializers 