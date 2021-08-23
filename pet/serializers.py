from rest_framework import serializers
from .models import Breed , Pet ,Order

class BreedSerializers(serializers.ModelSerializer):
    class Meta():
        model = Breed 
        fields = '__all__'

class PetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'

class OrderSerializers(serializers.ModelSerializer):
    class Meta():
        model = Order
        fields = '__all__'

