from rest_framework import serializers
from subscriptions.models import (
    SubscriptionType, Resource, FarmerSubscription, 
    FarmerSubscriptionResource, Payment
)
from accounts.serializers import FarmerSerializer as AccountsFarmerSerializer

class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionType
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class FarmerSubscriptionSerializer(serializers.ModelSerializer):
    farmer = AccountsFarmerSerializer(read_only=True)
    subscription_type = SubscriptionTypeSerializer(read_only=True)
    
    class Meta:
        model = FarmerSubscription
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request.user, 'farmer_profile'):
            validated_data['farmer'] = request.user.farmer_profile
        return super().create(validated_data)

class FarmerSubscriptionResourceSerializer(serializers.ModelSerializer):
    farmer_subscription = serializers.PrimaryKeyRelatedField(queryset=FarmerSubscription.objects.all())
    resource = serializers.PrimaryKeyRelatedField(queryset=Resource.objects.all())
    
    class Meta:
        model = FarmerSubscriptionResource
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    farmer_subscription = FarmerSubscriptionSerializer(read_only=True)
    
    class Meta:
        model = Payment
        fields = '__all__'
