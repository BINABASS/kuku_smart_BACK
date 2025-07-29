from rest_framework import serializers
from .models import CustomUser, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'profile_picture', 'about_me', 'education', 'experience', 'skills',
            'address', 'phone', 'linkedin', 'twitter', 'created_at', 'updated_at'
        ]

class UserSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    phone = serializers.CharField(source='phone_number', required=False)
    address = serializers.CharField(required=False, allow_blank=True)
    farm_name = serializers.CharField(required=False, allow_blank=True)
    notifications_enabled = serializers.BooleanField(default=True, required=False)
    email_notifications = serializers.BooleanField(default=True, required=False)
    sms_notifications = serializers.BooleanField(default=False, required=False)

    class Meta:
        model = CustomUser
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name',
            'phone',
            'address',
            'farm_name',
            'notifications_enabled',
            'email_notifications',
            'sms_notifications',
            'role',
            'is_admin',
            'is_farmer'
        ]
        read_only_fields = ['id', 'username', 'role', 'is_admin', 'is_farmer']

    def get_role(self, obj):
        if obj.is_admin:
            return 'admin'
        elif obj.is_farmer:
            return 'farmer'
        else:
            return 'manager'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Add default values for fields that don't exist in the model
        if 'address' not in data or data['address'] is None:
            data['address'] = ''
        if 'farm_name' not in data or data['farm_name'] is None:
            data['farm_name'] = ''
        if 'notifications_enabled' not in data:
            data['notifications_enabled'] = True
        if 'email_notifications' not in data:
            data['email_notifications'] = True
        if 'sms_notifications' not in data:
            data['sms_notifications'] = False
        return data
