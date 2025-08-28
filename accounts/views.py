from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from accounts.models import User, Farmer
from accounts.serializers import UserSerializer, FarmerSerializer, UserCreateSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Get current user profile"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def my_farm(self, request):
        """Get current farmer's farm information"""
        if hasattr(request.user, 'farmer_profile'):
            farmer = request.user.farmer_profile
            serializer = self.get_serializer(farmer)
            return Response(serializer.data)
        return Response({'error': 'User is not a farmer'}, status=status.HTTP_400_BAD_REQUEST)
