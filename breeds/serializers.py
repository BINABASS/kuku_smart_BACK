from rest_framework import serializers
from .models import Breed, BreedActivity, BreedCondition, BreedFeeding, ConditionType, FoodType

class ConditionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionType
        fields = ['id', 'name']

class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ['id', 'name', 'description']

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name', 'description']

class BreedActivitySerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    activity_type = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = BreedActivity
        fields = ['id', 'breed', 'activity_type', 'age', 'breed_activity_status']

class BreedConditionSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    condition_type = ConditionTypeSerializer()

    class Meta:
        model = BreedCondition
        fields = ['id', 'breed', 'condition_min', 'condition_max', 'condition_status', 'condition_type']

class BreedFeedingSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    food_type = FoodTypeSerializer()

    class Meta:
        model = BreedFeeding
        fields = ['id', 'breed', 'food_type', 'quantity', 'age', 'frequency', 'breed_feed_status']
