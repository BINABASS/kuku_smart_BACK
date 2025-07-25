from rest_framework import serializers
from .models import Farmer, Farm
from users.serializers import UserSerializer

class FarmSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Farm
        fields = ['id', 'user', 'name', 'address', 'phone', 'email', 'registration_date', 'status']

class FarmerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Farmer
        fields = ['id', 'user', 'farm', 'created_at', 'updated_at']
