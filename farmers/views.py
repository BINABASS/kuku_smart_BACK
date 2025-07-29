from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Farmer, Farm
from .serializers import FarmerSerializer, FarmSerializer

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsAuthenticated]

class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
    permission_classes = [IsAuthenticated]
