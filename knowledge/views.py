from django.shortcuts import render
from rest_framework import viewsets, permissions
from knowledge.models import (
    PatientHealth, Recommendation, ExceptionDisease, 
    Anomaly, Medication
)
from knowledge.serializers import (
    PatientHealthSerializer, RecommendationSerializer, ExceptionDiseaseSerializer,
    AnomalySerializer, MedicationSerializer
)

# Create your views here.

class PatientHealthViewSet(viewsets.ModelViewSet):
    queryset = PatientHealth.objects.all()
    serializer_class = PatientHealthSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = [permissions.IsAuthenticated]

class ExceptionDiseaseViewSet(viewsets.ModelViewSet):
    queryset = ExceptionDisease.objects.all()
    serializer_class = ExceptionDiseaseSerializer
    permission_classes = [permissions.IsAuthenticated]

class AnomalyViewSet(viewsets.ModelViewSet):
    queryset = Anomaly.objects.all()
    serializer_class = AnomalySerializer
    permission_classes = [permissions.IsAuthenticated]

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticated]
