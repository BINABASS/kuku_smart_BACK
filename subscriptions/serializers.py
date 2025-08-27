from rest_framework import serializers
from subscriptions.models import (
    SubscriptionType, Resource, FarmerSubscription, 
    FarmerSubscriptionResource, Payment
)
from accounts.models import Farmer

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ['id', 'user', 'phone_number', 'address']

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class FarmerSubscriptionSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer(read_only=True)
    subscription_type = SubscriptionTypeSerializer(read_only=True)
    
    class Meta:
        model = FarmerSubscription
        fields = '__all__'

class FarmerSubscriptionResourceSerializer(serializers.ModelSerializer):
    farmer_subscription = FarmerSubscriptionSerializer(read_only=True)
    resource = ResourceSerializer(read_only=True)
    
    class Meta:
        model = FarmerSubscriptionResource
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    farmer_subscription = FarmerSubscriptionSerializer(read_only=True)
    
    class Meta:
        model = Payment
        fields = '__all__'
