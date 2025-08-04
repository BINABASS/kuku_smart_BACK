from rest_framework import serializers
from .models import Farmer, Farm
from users.serializers import UserSerializer
from users.models import CustomUser

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = ['id', 'name', 'address', 'phone', 'email', 'registration_date', 'status']

class FarmerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    farm = FarmSerializer(read_only=True)
    farm_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    user_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)
    email = serializers.EmailField(write_only=True, required=False)  # For creating user

    class Meta:
        model = Farmer
        fields = ['id', 'user', 'user_id', 'farm', 'farm_id', 'first_name', 'last_name', 'phone', 'address', 'registration_date', 'status', 'email']
        read_only_fields = ['id', 'registration_date']

    def create(self, validated_data):
        # Extract email for user creation
        email = validated_data.pop('email', None)
        user_id = validated_data.pop('user_id', None)
        farm_id = validated_data.pop('farm_id', None)
        
        # Create user if email is provided and user_id is not
        if email and not user_id:
            try:
                user = CustomUser.objects.get(email=email)
                user_id = user.id
            except CustomUser.DoesNotExist:
                # Create new user
                user = CustomUser.objects.create(
                    email=email,
                    username=email,
                    is_active=True
                )
                user_id = user.id
        
        # Ensure we have a user_id
        if not user_id:
            raise serializers.ValidationError("Either user_id or email must be provided")
        
        validated_data['user_id'] = user_id
        if farm_id:
            validated_data['farm_id'] = farm_id
            
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Handle nested user creation if needed
        user_id = validated_data.pop('user_id', None)
        farm_id = validated_data.pop('farm_id', None)
        email = validated_data.pop('email', None)
        
        if user_id:
            validated_data['user_id'] = user_id
        elif email:
            try:
                user = CustomUser.objects.get(email=email)
                validated_data['user_id'] = user.id
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("User with provided email does not exist")
        
        if farm_id:
            validated_data['farm_id'] = farm_id
            
        return super().update(instance, validated_data)
