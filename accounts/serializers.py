from rest_framework import serializers
from accounts.models import User, Farmer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'date_joined']
        read_only_fields = ['id', 'date_joined']

class FarmerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Farmer
        fields = ['id', 'user', 'full_name', 'address', 'email', 'phone', 'created_date']
        read_only_fields = ['id', 'created_date']

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'role']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
