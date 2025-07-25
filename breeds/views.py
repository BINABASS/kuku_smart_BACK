from rest_framework import viewsets
from .models import Breed
from .serializers import BreedSerializer

class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
