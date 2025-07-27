from rest_framework import serializers
from .models import Subscription, SubscriptionPlan, Payment

class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    plan_name = serializers.CharField(source='plan.name', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    
    class Meta:
        model = Subscription
        fields = '__all__'
        read_only_fields = ('plan_name', 'user_email', 'farm_name')

class PaymentSerializer(serializers.ModelSerializer):
    subscription_user = serializers.CharField(source='subscription.user.email', read_only=True)
    subscription_plan = serializers.CharField(source='subscription.plan.name', read_only=True)
    
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ('subscription_user', 'subscription_plan') 