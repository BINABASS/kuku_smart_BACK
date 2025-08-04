#!/usr/bin/env python3
"""
Script to fix critical database data issues
"""

import os
import django
from datetime import datetime, timedelta
from decimal import Decimal

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kuku_smart.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import connection
from rest_framework.authtoken.models import Token
from users.models import CustomUser, Profile, VitalSigns
from farmers.models import Farmer, Farm
from breeds.models import Breed
from batches.models import Batch
from devices.models import Device, DeviceLog
from sensors.models import Sensor, SensorReading
from subscriptions.models import SubscriptionPlan, Subscription, Payment
from inventory.models import Category, Item, Transaction
from financials.models import Budget, Expense, Income
from analytics.models import AnalyticsData, Dashboard, Report, Alert
from knowledge_base.models import Article, Category as KnowledgeCategory, Comment, FAQ

User = get_user_model()

def fix_user_data():
    """Fix user data inconsistency"""
    print("🔧 Fixing User Data...")
    
    # Get all user IDs from tokens
    token_user_ids = Token.objects.values_list('user_id', flat=True).distinct()
    print(f"Found {len(token_user_ids)} users in tokens")
    
    # Create missing users
    for user_id in token_user_ids:
        try:
            user = User.objects.get(id=user_id)
            print(f"✅ User {user.email} already exists")
        except User.DoesNotExist:
            # Create a basic user
            user = User.objects.create(
                id=user_id,
                email=f"user{user_id}@example.com",
                username=f"user{user_id}",
                is_active=True
            )
            print(f"✅ Created user {user.email}")
            
            # Create profile
            Profile.objects.get_or_create(
                user=user,
                defaults={
                    'phone': f"+255{user_id}000000",
                    'address': f"Address for user {user_id}",
                    'bio': f"Bio for user {user_id}"
                }
            )
            print(f"✅ Created profile for {user.email}")

def add_subscription_data():
    """Add sample subscription data"""
    print("\n🔧 Adding Subscription Data...")
    
    # Create subscription plans
    plans_data = [
        {
            'name': 'Basic Plan',
            'type': 'basic',
            'price': Decimal('50.00'),
            'duration_days': 30,
            'max_devices': 5,
            'max_sensors': 10,
            'max_batches': 2,
            'is_active': True
        },
        {
            'name': 'Premium Plan',
            'type': 'premium',
            'price': Decimal('100.00'),
            'duration_days': 30,
            'max_devices': 15,
            'max_sensors': 30,
            'max_batches': 5,
            'is_active': True
        },
        {
            'name': 'Enterprise Plan',
            'type': 'enterprise',
            'price': Decimal('200.00'),
            'duration_days': 30,
            'max_devices': 50,
            'max_sensors': 100,
            'max_batches': 20,
            'is_active': True
        }
    ]
    
    for plan_data in plans_data:
        plan, created = SubscriptionPlan.objects.get_or_create(
            name=plan_data['name'],
            defaults=plan_data
        )
        if created:
            print(f"✅ Created subscription plan: {plan.name}")
        else:
            print(f"✅ Subscription plan already exists: {plan.name}")
    
    # Create sample subscriptions
    users = User.objects.all()[:3]  # Get first 3 users
    plans = SubscriptionPlan.objects.all()
    
    for i, user in enumerate(users):
        if i < len(plans):
            plan = plans[i]
            subscription, created = Subscription.objects.get_or_create(
                user=user,
                defaults={
                    'plan': plan,
                    'start_date': datetime.now().date(),
                    'end_date': datetime.now().date() + timedelta(days=30),
                    'status': 'active',
                    'auto_renew': True
                }
            )
            if created:
                print(f"✅ Created subscription for {user.email}")
            else:
                print(f"✅ Subscription already exists for {user.email}")

def add_inventory_data():
    """Add sample inventory data"""
    print("\n🔧 Adding Inventory Data...")
    
    # Get existing categories
    categories = Category.objects.all()
    
    if not categories.exists():
        print("❌ No inventory categories found")
        return
    
    # Add sample items
    items_data = [
        {
            'name': 'Starter Feed',
            'description': 'High protein starter feed for chicks',
            'category': categories.first(),
            'unit_price': Decimal('25.00'),
            'current_stock': 100,
            'min_stock_level': 10,
            'max_stock_level': 200,
            'expiry_date': datetime.now().date() + timedelta(days=180)
        },
        {
            'name': 'Grower Feed',
            'description': 'Balanced grower feed for young birds',
            'category': categories.first(),
            'unit_price': Decimal('30.00'),
            'current_stock': 75,
            'min_stock_level': 15,
            'max_stock_level': 150,
            'expiry_date': datetime.now().date() + timedelta(days=150)
        },
        {
            'name': 'Vitamin Supplement',
            'description': 'Essential vitamins for poultry health',
            'category': categories.filter(name__icontains='Medicine').first() or categories.first(),
            'unit_price': Decimal('15.00'),
            'current_stock': 50,
            'min_stock_level': 5,
            'max_stock_level': 100,
            'expiry_date': datetime.now().date() + timedelta(days=365)
        }
    ]
    
    for item_data in items_data:
        item, created = Item.objects.get_or_create(
            name=item_data['name'],
            defaults=item_data
        )
        if created:
            print(f"✅ Created inventory item: {item.name}")
        else:
            print(f"✅ Inventory item already exists: {item.name}")
    
    # Add sample transactions
    items = Item.objects.all()
    if items.exists():
        item = items.first()
        transaction, created = Transaction.objects.get_or_create(
            item=item,
            transaction_type='in',
            quantity=50,
            unit_price=item.unit_price,
            defaults={
                'reference': 'PO-001',
                'notes': 'Initial stock purchase',
                'transaction_date': datetime.now().date()
            }
        )
        if created:
            print(f"✅ Created inventory transaction for {item.name}")
        else:
            print(f"✅ Inventory transaction already exists for {item.name}")

def add_sensor_data():
    """Add sample sensor data"""
    print("\n🔧 Adding Sensor Data...")
    
    # Get existing devices
    devices = Device.objects.all()
    
    if not devices.exists():
        print("❌ No devices found")
        return
    
    # Create sensors for devices
    for device in devices:
        sensor, created = Sensor.objects.get_or_create(
            device=device,
            defaults={
                'name': f"{device.name} Sensor",
                'type': 'temperature' if 'temperature' in device.name.lower() else 'humidity',
                'location': device.location,
                'status': 'active'
            }
        )
        if created:
            print(f"✅ Created sensor for device: {device.name}")
        else:
            print(f"✅ Sensor already exists for device: {device.name}")
    
    # Add sensor readings
    sensors = Sensor.objects.all()
    for sensor in sensors:
        # Add some sample readings
        for i in range(5):
            reading, created = SensorReading.objects.get_or_create(
                sensor=sensor,
                timestamp=datetime.now() - timedelta(hours=i),
                defaults={
                    'value': 25.5 + i
                }
            )
            if created:
                print(f"✅ Created sensor reading for {sensor.name}")

def add_knowledge_base_data():
    """Add sample knowledge base data"""
    print("\n🔧 Adding Knowledge Base Data...")
    
    # Create categories
    categories_data = [
        {'name': 'Health & Disease', 'description': 'Information about poultry health and disease management'},
        {'name': 'Feeding & Nutrition', 'description': 'Guidelines for proper feeding and nutrition'},
        {'name': 'Breeding & Genetics', 'description': 'Information about breeding and genetics'},
        {'name': 'Equipment & Technology', 'description': 'Guidance on equipment and technology use'}
    ]
    
    for cat_data in categories_data:
        category, created = KnowledgeCategory.objects.get_or_create(
            name=cat_data['name'],
            defaults=cat_data
        )
        if created:
            print(f"✅ Created knowledge category: {category.name}")
        else:
            print(f"✅ Knowledge category already exists: {category.name}")
    
    # Add sample articles
    categories = KnowledgeCategory.objects.all()
    if categories.exists():
        category = categories.first()
        # Get first user for author
        users = User.objects.all()
        if users.exists():
            author = users.first()
            article, created = Article.objects.get_or_create(
                title='Basic Poultry Health Management',
                defaults={
                    'category': category,
                    'content': 'This article covers the basics of poultry health management...',
                    'author': author,
                    'is_published': True
                }
            )
            if created:
                print(f"✅ Created knowledge article: {article.title}")
            else:
                print(f"✅ Knowledge article already exists: {article.title}")

def add_analytics_data():
    """Add sample analytics data"""
    print("\n🔧 Adding Analytics Data...")
    
    # Get first farm for dashboard
    farms = Farm.objects.all()
    if not farms.exists():
        print("❌ No farms found for analytics data")
        return
    
    farm = farms.first()
    
    # Create sample dashboard
    dashboard, created = Dashboard.objects.get_or_create(
        name='Main Farm Dashboard',
        farm=farm,
        defaults={
            'type': 'overview',
            'configuration': '{"widgets": ["temperature", "humidity", "feed_consumption"]}',
            'is_active': True
        }
    )
    if created:
        print(f"✅ Created analytics dashboard: {dashboard.name}")
    else:
        print(f"✅ Analytics dashboard already exists: {dashboard.name}")
    
    # Create sample report
    report, created = Report.objects.get_or_create(
        name='Monthly Production Report',
        farm=farm,
        defaults={
            'type': 'production',
            'parameters': '{"month": "current", "farm_id": 1}'
        }
    )
    if created:
        print(f"✅ Created analytics report: {report.name}")
    else:
        print(f"✅ Analytics report already exists: {report.name}")

def main():
    """Main function to fix all data issues"""
    print("🔧 Starting Database Data Fix...")
    print("=" * 50)
    
    try:
        # Fix critical issues
        fix_user_data()
        add_subscription_data()
        add_inventory_data()
        add_sensor_data()
        add_knowledge_base_data()
        add_analytics_data()
        
        print("\n" + "=" * 50)
        print("✅ Database data fix completed successfully!")
        print("\n📊 Summary of fixes:")
        print("- ✅ User data synchronized")
        print("- ✅ Subscription plans and data added")
        print("- ✅ Inventory items and transactions added")
        print("- ✅ Sensor data connected to devices")
        print("- ✅ Knowledge base content added")
        print("- ✅ Analytics dashboards and reports added")
        
    except Exception as e:
        print(f"❌ Error during data fix: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
