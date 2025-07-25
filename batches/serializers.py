from rest_framework import serializers
from .models import ActivityType, ActivitySchedule, Batch, BatchActivity, BatchFeeding
from breeds.models import Breed
from farmers.models import Farm

class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = '__all__'

class ActivityScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivitySchedule
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    breed_name = serializers.CharField(source='breed.name', read_only=True)
    
    class Meta:
        model = Batch
        fields = '__all__'
        read_only_fields = ('farm_name', 'breed_name')

class BatchActivitySerializer(serializers.ModelSerializer):
    breed_activity_name = serializers.CharField(source='breed_activity.activity_name', read_only=True)
    
    class Meta:
        model = BatchActivity
        fields = '__all__'
        read_only_fields = ('breed_activity_name',)

class BatchFeedingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchFeeding
        fields = '__all__'
