#!/usr/bin/env python3
"""
Test authentication and API endpoints
"""

import os
import django
import requests
import json

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kuku_smart.settings')
django.setup()

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

def test_authentication():
    """Test authentication flow"""
    
    base_url = "http://localhost:8000/api"
    
    print("🔍 Testing Authentication...")
    print("=" * 50)
    
    # Get first user and token
    user = User.objects.first()
    if not user:
        print("❌ No users found")
        return
    
    token, created = Token.objects.get_or_create(user=user)
    print(f"✅ Using user: {user.email}")
    print(f"✅ Token: {token.key}")
    
    headers = {
        'Authorization': f'Token {token.key}',
        'Content-Type': 'application/json'
    }
    
    # Test 1: Check if token works
    try:
        response = requests.get(f"{base_url}/users/", headers=headers)
        print(f"✅ GET /users/ - Status: {response.status_code}")
        if response.status_code == 200:
            users = response.json()
            print(f"   Found {len(users)} users")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Error testing users API: {e}")
    
    # Test 2: Check farmers API
    try:
        response = requests.get(f"{base_url}/farmers/", headers=headers)
        print(f"✅ GET /farmers/ - Status: {response.status_code}")
        if response.status_code == 200:
            farmers = response.json()
            print(f"   Found {len(farmers)} farmers")
        else:
            print(f"   Error: {response.text}")
    except Exception as e:
        print(f"❌ Error testing farmers API: {e}")
    
    # Test 3: Test creating a farmer
    try:
        test_farmer = {
            "first_name": "Test",
            "last_name": "Farmer",
            "phone": "1234567890",
            "email": "testfarmer@example.com",
            "address": "Test Address",
            "status": True
        }
        
        response = requests.post(f"{base_url}/farmers/", 
                               json=test_farmer, 
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
        print(f"❌ Error creating farmer: {e}")

if __name__ == "__main__":
    test_authentication() 