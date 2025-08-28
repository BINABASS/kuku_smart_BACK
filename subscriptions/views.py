from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from subscriptions.models import (
    SubscriptionType, Resource, FarmerSubscription, 
    FarmerSubscriptionResource, Payment
)
from subscriptions.serializers import (
    SubscriptionTypeSerializer, ResourceSerializer, FarmerSubscriptionSerializer,
    FarmerSubscriptionResourceSerializer, PaymentSerializer
)
from config.permissions import IsAdminOrReadOnly

# Create your views here.

class SubscriptionTypeViewSet(viewsets.ModelViewSet):
    queryset = SubscriptionType.objects.all()
    serializer_class = SubscriptionTypeSerializer
    permission_classes = [IsAdminOrReadOnly]

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=False, methods=['get'], url_path='my')
    def my_resources(self, request):
        """Return resources available to the current farmer based on subscriptions."""
        user = request.user
        if not hasattr(user, 'farmer_profile'):
            return Response({'detail': 'User is not a farmer'}, status=status.HTTP_400_BAD_REQUEST)

        farmer = user.farmer_profile
        # Filter active subscriptions if there is a status field; otherwise include all
        fs_qs = FarmerSubscription.objects.filter(farmer=farmer)
        fsr_qs = FarmerSubscriptionResource.objects.filter(farmer_subscription__in=fs_qs).select_related('resource')
        resources = Resource.objects.filter(id__in=fsr_qs.values_list('resource_id', flat=True)).distinct()
        serializer = self.get_serializer(resources, many=True)
        return Response(serializer.data)

class FarmerSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = FarmerSubscription.objects.all()
    serializer_class = FarmerSubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_staff or getattr(user, 'is_superuser', False) or getattr(user, 'role', '').upper() == 'ADMINISTRATOR':
            return qs
        if hasattr(user, 'farmer_profile'):
            return qs.filter(farmer=user.farmer_profile)
        return qs.none()

    def perform_create(self, serializer):
        farmer = getattr(self.request.user, 'farmer_profile', None)
        serializer.save(farmer=farmer)

class FarmerSubscriptionResourceViewSet(viewsets.ModelViewSet):
    queryset = FarmerSubscriptionResource.objects.all()
    serializer_class = FarmerSubscriptionResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_staff or getattr(user, 'is_superuser', False) or getattr(user, 'role', '').upper() == 'ADMINISTRATOR':
            return qs
        if hasattr(user, 'farmer_profile'):
            return qs.filter(farmer_subscription__farmer=user.farmer_profile)
        return qs.none()

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_staff or getattr(user, 'is_superuser', False) or getattr(user, 'role', '').upper() == 'ADMINISTRATOR':
            return qs
        if hasattr(user, 'farmer_profile'):
            return qs.filter(farmer_subscription__farmer=user.farmer_profile)
        return qs.none()
