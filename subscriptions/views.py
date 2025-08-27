from django.shortcuts import render
from rest_framework import viewsets, permissions
from subscriptions.models import (
    SubscriptionType, Resource, FarmerSubscription, 
    FarmerSubscriptionResource, Payment
)
from subscriptions.serializers import (
    SubscriptionTypeSerializer, ResourceSerializer, FarmerSubscriptionSerializer,
    FarmerSubscriptionResourceSerializer, PaymentSerializer
)

# Create your views here.

class SubscriptionTypeViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionType.objects.all()
    serializer_class = SubscriptionTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class FarmerSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = FarmerSubscription.objects.all()
    serializer_class = FarmerSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

class FarmerSubscriptionResourceViewSet(viewsets.ModelViewSet):
    queryset = FarmerSubscriptionResource.objects.all()
    serializer_class = FarmerSubscriptionResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
