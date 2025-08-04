#!/usr/bin/env python3
"""
Test script to verify Farmers API functionality
"""

import os
import django
import requests
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kuku_smart.settings')
django.setup()

from django.contrib.auth import get_user_model
from farmers.models import Farmer, Farm
from rest_framework.authtoken.models import Token

User = get_user_model()

def test_farmers_api():
    """Test the farmers API endpoints"""
    
    base_url = "http://localhost:8000/api"
    
    print("🔍 Testing Farmers API...")
    print("=" * 50)
    
    # Get authentication token
    print("🔐 Getting authentication token...")
    try:
        # Try to get an existing user
        user = User.objects.first()
        if not user:
            print("❌ No users found in database")
            return
        
        # Get or create token
        token, created = Token.objects.get_or_create(user=user)
        print(f"✅ Using token for user: {user.email}")
        
        headers = {
            'Authorization': f'Token {token.key}',
            'Content-Type': 'application/json'
        }
        
    except Exception as e:
        print(f"❌ Error getting authentication token: {e}")
        return
    
    # Test 1: Check if API is accessible with authentication
    try:
        response = requests.get(f"{base_url}/farmers/", headers=headers)
        print(f"✅ GET /farmers/ - Status: {response.status_code}")
        if response.status_code == 200:
            farmers = response.json()
            print(f"   Found {len(farmers)} farmers")
            for farmer in farmers:
                print(f"   - {farmer.get('first_name', 'N/A')} {farmer.get('last_name', 'N/A')}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Error accessing farmers API: {e}")
    
    print("\n" + "=" * 50)
    
    # Test 2: Check database directly
    print("🔍 Checking database directly...")
    try:
        farmers_count = Farmer.objects.count()
        print(f"✅ Database has {farmers_count} farmers")
        
        for farmer in Farmer.objects.all():
            print(f"   - {farmer.first_name} {farmer.last_name} (ID: {farmer.id})")
            print(f"     User: {farmer.user.email if farmer.user else 'No user'}")
            print(f"     Farm: {farmer.farm.name if farmer.farm else 'No farm'}")
            print(f"     Status: {'Active' if farmer.status else 'Inactive'}")
    except Exception as e:
        print(f"❌ Error checking database: {e}")
    
    print("\n" + "=" * 50)
    
    # Test 3: Check farms API with authentication
    try:
        response = requests.get(f"{base_url}/farms/", headers=headers)
        print(f"✅ GET /farms/ - Status: {response.status_code}")
        if response.status_code == 200:
            farms = response.json()
            print(f"   Found {len(farms)} farms")
            for farm in farms:
                print(f"   - {farm.get('name', 'N/A')}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Error accessing farms API: {e}")
    
    print("\n" + "=" * 50)
    
    # Test 4: Check users API with authentication
    try:
        response = requests.get(f"{base_url}/users/", headers=headers)
        print(f"✅ GET /users/ - Status: {response.status_code}")
        if response.status_code == 200:
            users = response.json()
            print(f"   Found {len(users)} users")
            for user in users[:5]:  # Show first 5 users
                print(f"   - {user.get('email', 'N/A')}")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Error accessing users API: {e}")
    
    print("\n" + "=" * 50)
    
    # Test 5: Test creating a new farmer
    print("🧪 Testing farmer creation...")
    try:
        test_farmer_data = {
            "first_name": "Test",
            "last_name": "Farmer",
            "phone": "1234567890",
            "address": "Test Address",
            "status": True
        }
        
        response = requests.post(f"{base_url}/farmers/", 
                               json=test_farmer_data, 
                               headers=headers)
        print(f"✅ POST /farmers/ - Status: {response.status_code}")
        
        if response.status_code == 201:
            print("   ✅ Farmer created successfully!")
            created_farmer = response.json()
            print(f"   - ID: {created_farmer.get('id')}")
            print(f"   - Name: {created_farmer.get('first_name')} {created_farmer.get('last_name')}")
        else:
            print(f"   ❌ Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Error creating test farmer: {e}")

if __name__ == "__main__":
    test_farmers_api() 