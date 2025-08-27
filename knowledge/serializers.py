from rest_framework import serializers
from knowledge.models import (
    PatientHealth, Recommendation, ExceptionDisease, 
    Anomaly, Medication
)
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role']

class PatientHealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientHealth
        fields = '__all__'

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = '__all__'

class ExceptionDiseaseSerializer(serializers.ModelSerializer):
    recommendation = RecommendationSerializer(read_only=True)
    patient_health = PatientHealthSerializer(read_only=True)
    
    class Meta:
        model = ExceptionDisease
        fields = '__all__'

class AnomalySerializer(serializers.ModelSerializer):
    class Meta:
        model = Anomaly
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    anomaly = AnomalySerializer(read_only=True)
    recommendation = RecommendationSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Medication
        fields = '__all__'
