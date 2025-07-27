from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import CustomUser
from farmers.models import Farm, Farmer
from breeds.models import Breed, FoodType, ConditionType
from batches.models import Batch, ActivityType
from devices.models import Device
from sensors.models import Sensor
from subscriptions.models import SubscriptionPlan, Subscription
from inventory.models import Category as InventoryCategory, Item
from knowledge_base.models import Category as KnowledgeCategory, Article, FAQ
from financials.models import Income, Expense, Budget
from analytics.models import AnalyticsData, Alert
from datetime import datetime, timedelta
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Set up test data for the Kuku Smart application'

    def handle(self, *args, **options):
        self.stdout.write('Setting up test data...')
        
        # Create test users
        self.create_test_users()
        
        # Create farms
        self.create_farms()
        
        # Create breeds and related data
        self.create_breeds()
        
        # Create batches
        self.create_batches()
        
        # Create devices and sensors
        self.create_devices_and_sensors()
        
        # Create subscriptions
        self.create_subscriptions()
        
        # Create inventory
        self.create_inventory()
        
        # Create knowledge base
        self.create_knowledge_base()
        
        # Create financial data
        self.create_financial_data()
        
        # Create analytics data
        self.create_analytics_data()
        
        self.stdout.write(self.style.SUCCESS('Test data setup completed successfully!'))

    def create_test_users(self):
        # Create admin user
        admin_user, created = CustomUser.objects.get_or_create(
            email='admin@poultryfarm.com',
            defaults={
                'username': 'admin',
                'first_name': 'Farm',
                'last_name': 'Administrator',
                'is_admin': True,
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write('Created admin user: admin@poultryfarm.com / admin123')
        
        # Create manager user
        manager_user, created = CustomUser.objects.get_or_create(
            email='manager@poultryfarm.com',
            defaults={
                'username': 'manager',
                'first_name': 'Farm',
                'last_name': 'Manager',
                'is_admin': False,
                'is_staff': False
            }
        )
        if created:
            manager_user.set_password('manager123')
            manager_user.save()
            self.stdout.write('Created manager user: manager@poultryfarm.com / manager123')

    def create_farms(self):
        # Create test farm
        farm, created = Farm.objects.get_or_create(
            name='Test Poultry Farm',
            defaults={
                'address': '123 Farm Road, Nairobi, Kenya',
                'phone': '+254700123456',
                'email': 'farm@poultryfarm.com',
                'user': CustomUser.objects.get(email='manager@poultryfarm.com')
            }
        )
        if created:
            self.stdout.write('Created test farm')

    def create_breeds(self):
        # Create food types
        food_types = ['Starter Feed', 'Grower Feed', 'Layer Feed', 'Broiler Feed']
        for food_name in food_types:
            FoodType.objects.get_or_create(name=food_name)
        
        # Create condition types
        condition_types = ['Temperature', 'Humidity', 'Light', 'Ventilation']
        for condition_name in condition_types:
            ConditionType.objects.get_or_create(name=condition_name)
        
        # Create breeds
        breeds_data = [
            {'name': 'Broiler', 'description': 'Fast-growing meat chicken'},
            {'name': 'Layer', 'description': 'Egg-laying chicken'},
            {'name': 'Dual Purpose', 'description': 'Both meat and egg production'},
        ]
        
        for breed_data in breeds_data:
            Breed.objects.get_or_create(
                name=breed_data['name'],
                defaults={'description': breed_data['description']}
            )
        
        self.stdout.write('Created breeds and related data')

    def create_batches(self):
        # Create activity types
        activity_types = ['Vaccination', 'Feeding', 'Cleaning', 'Health Check', 'Weighing']
        for activity_name in activity_types:
            ActivityType.objects.get_or_create(activity_type=activity_name)
        
        # Create test batch
        farm = Farm.objects.first()
        breed = Breed.objects.first()
        
        if farm and breed:
            batch, created = Batch.objects.get_or_create(
                farm=farm,
                defaults={
                    'breed': breed,
                    'arrive_date': datetime.now().date(),
                    'init_age': 1,
                    'quantity': 1000,
                    'init_weight': 50,
                    'batch_status': 1
                }
            )
            if created:
                self.stdout.write('Created test batch')

    def create_devices_and_sensors(self):
        farm = Farm.objects.first()
        
        # Create devices
        devices_data = [
            {'name': 'Temperature Sensor 1', 'type': 'sensor', 'status': 'online'},
            {'name': 'Humidity Monitor', 'type': 'sensor', 'status': 'online'},
            {'name': 'Feeding Controller', 'type': 'controller', 'status': 'online'},
            {'name': 'Lighting System', 'type': 'controller', 'status': 'online'},
        ]
        
        for device_data in devices_data:
            device, created = Device.objects.get_or_create(
                name=device_data['name'],
                defaults={
                    'type': device_data['type'],
                    'status': device_data['status'],
                    'farm': farm,
                    'location': 'Main House',
                    'firmware_version': '1.0.0'
                }
            )
            
            # Create sensors for sensor devices
            if device_data['type'] == 'sensor':
                sensor_type = 'temperature' if 'Temperature' in device_data['name'] else 'humidity'
                Sensor.objects.get_or_create(
                    name=f"{device_data['name']} Sensor",
                    defaults={
                        'type': sensor_type,
                        'device': device,
                        'current_value': random.uniform(20, 30) if sensor_type == 'temperature' else random.uniform(40, 70),
                        'unit': '°C' if sensor_type == 'temperature' else '%',
                        'status': 'active',
                        'location': 'Main House'
                    }
                )
        
        self.stdout.write('Created devices and sensors')

    def create_subscriptions(self):
        # Create subscription plans
        plans_data = [
            {'name': 'Basic Plan', 'type': 'basic', 'price': 29.99, 'duration_days': 30},
            {'name': 'Premium Plan', 'type': 'premium', 'price': 59.99, 'duration_days': 30},
            {'name': 'Enterprise Plan', 'type': 'enterprise', 'price': 99.99, 'duration_days': 30},
        ]
        
        for plan_data in plans_data:
            plan, created = SubscriptionPlan.objects.get_or_create(
                name=plan_data['name'],
                defaults={
                    'type': plan_data['type'],
                    'price': plan_data['price'],
                    'duration_days': plan_data['duration_days'],
                    'max_devices': 10 if plan_data['type'] == 'basic' else 50,
                    'max_sensors': 50 if plan_data['type'] == 'basic' else 200,
                    'max_batches': 5 if plan_data['type'] == 'basic' else 20,
                }
            )
        
        # Create subscription for manager
        user = CustomUser.objects.get(email='manager@poultryfarm.com')
        farm = Farm.objects.first()
        plan = SubscriptionPlan.objects.get(type='premium')
        
        if user and farm and plan:
            subscription, created = Subscription.objects.get_or_create(
                user=user,
                defaults={
                    'farm': farm,
                    'plan': plan,
                    'status': 'active',
                    'end_date': datetime.now() + timedelta(days=30),
                    'manager_name': f"{user.first_name} {user.last_name}"
                }
            )
            if created:
                self.stdout.write('Created subscription for manager')

    def create_inventory(self):
        farm = Farm.objects.first()
        
        # Create inventory categories
        categories_data = [
            {'name': 'Feed', 'description': 'Poultry feed and supplements'},
            {'name': 'Medicine', 'description': 'Veterinary medicines and vaccines'},
            {'name': 'Equipment', 'description': 'Farming equipment and tools'},
        ]
        
        for cat_data in categories_data:
            category, created = InventoryCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            
            # Create items for each category
            if cat_data['name'] == 'Feed':
                items_data = [
                    {'name': 'Starter Feed', 'type': 'feed', 'current_stock': 500, 'unit_price': 25.00},
                    {'name': 'Grower Feed', 'type': 'feed', 'current_stock': 300, 'unit_price': 22.00},
                    {'name': 'Layer Feed', 'type': 'feed', 'current_stock': 400, 'unit_price': 28.00},
                ]
            elif cat_data['name'] == 'Medicine':
                items_data = [
                    {'name': 'Vaccine A', 'type': 'medicine', 'current_stock': 50, 'unit_price': 15.00},
                    {'name': 'Antibiotic B', 'type': 'medicine', 'current_stock': 30, 'unit_price': 12.00},
                ]
            else:
                items_data = [
                    {'name': 'Watering System', 'type': 'equipment', 'current_stock': 5, 'unit_price': 150.00},
                    {'name': 'Feeding Troughs', 'type': 'equipment', 'current_stock': 20, 'unit_price': 45.00},
                ]
            
            for item_data in items_data:
                Item.objects.get_or_create(
                    name=item_data['name'],
                    defaults={
                        'type': item_data['type'],
                        'category': category,
                        'current_stock': item_data['current_stock'],
                        'unit_price': item_data['unit_price'],
                        'farm': farm,
                        'unit': 'kg' if item_data['type'] == 'feed' else 'pieces',
                        'min_stock_level': 50,
                        'max_stock_level': 1000
                    }
                )
        
        self.stdout.write('Created inventory data')

    def create_knowledge_base(self):
        # Create knowledge categories
        categories_data = [
            {'name': 'Feeding Guide', 'description': 'Poultry feeding best practices'},
            {'name': 'Health Management', 'description': 'Disease prevention and treatment'},
            {'name': 'Equipment Maintenance', 'description': 'Equipment care and maintenance'},
        ]
        
        for cat_data in categories_data:
            category, created = KnowledgeCategory.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            
            # Create articles for each category
            if cat_data['name'] == 'Feeding Guide':
                articles_data = [
                    {
                        'title': 'Proper Feeding Schedule for Broilers',
                        'content': 'This article covers the optimal feeding schedule for broiler chickens...',
                        'type': 'guide'
                    },
                    {
                        'title': 'Nutrition Requirements for Layers',
                        'content': 'Learn about the specific nutritional needs of laying hens...',
                        'type': 'guide'
                    }
                ]
            elif cat_data['name'] == 'Health Management':
                articles_data = [
                    {
                        'title': 'Common Poultry Diseases',
                        'content': 'Overview of common diseases and their symptoms...',
                        'type': 'guide'
                    }
                ]
            else:
                articles_data = [
                    {
                        'title': 'Maintaining Feeding Equipment',
                        'content': 'Regular maintenance tips for feeding systems...',
                        'type': 'tutorial'
                    }
                ]
            
            user = CustomUser.objects.first()
            for article_data in articles_data:
                Article.objects.get_or_create(
                    title=article_data['title'],
                    defaults={
                        'content': article_data['content'],
                        'type': article_data['type'],
                        'category': category,
                        'author': user,
                        'tags': ['poultry', 'management']
                    }
                )
            
            # Create FAQs
            if cat_data['name'] == 'Feeding Guide':
                FAQ.objects.get_or_create(
                    question='How often should I feed my chickens?',
                    defaults={
                        'answer': 'Chickens should be fed 2-3 times per day with access to feed at all times.',
                        'category': category,
                        'order': 1
                    }
                )
        
        self.stdout.write('Created knowledge base data')

    def create_financial_data(self):
        farm = Farm.objects.first()
        
        if farm:
            # Create income records
            income_types = ['egg_sales', 'meat_sales', 'subscription']
            for i in range(5):
                Income.objects.get_or_create(
                    farm=farm,
                    type=random.choice(income_types),
                    defaults={
                        'amount': random.uniform(1000, 5000),
                        'description': f'Income from {random.choice(income_types)}',
                        'date': datetime.now().date() - timedelta(days=i*7)
                    }
                )
            
            # Create expense records
            expense_types = ['feed', 'medicine', 'labor', 'equipment']
            for i in range(5):
                Expense.objects.get_or_create(
                    farm=farm,
                    type=random.choice(expense_types),
                    defaults={
                        'amount': random.uniform(200, 1500),
                        'description': f'Expense for {random.choice(expense_types)}',
                        'date': datetime.now().date() - timedelta(days=i*7)
                    }
                )
            
            # Create budget
            Budget.objects.get_or_create(
                farm=farm,
                type='monthly',
                category='Feed',
                defaults={
                    'allocated_amount': 5000.00,
                    'spent_amount': 3200.00,
                    'start_date': datetime.now().date(),
                    'end_date': datetime.now().date() + timedelta(days=30)
                }
            )
        
        self.stdout.write('Created financial data')

    def create_analytics_data(self):
        farm = Farm.objects.first()
        batch = Batch.objects.first()
        
        if farm and batch:
            # Create analytics data
            metrics = ['temperature', 'humidity', 'feed_consumption', 'weight_gain']
            for i in range(10):
                AnalyticsData.objects.get_or_create(
                    farm=farm,
                    batch=batch,
                    data_type='production',
                    metric_name=random.choice(metrics),
                    defaults={
                        'value': random.uniform(20, 30) if 'temperature' in metrics[i % len(metrics)] else random.uniform(1, 100),
                        'unit': '°C' if 'temperature' in metrics[i % len(metrics)] else 'kg',
                        'date': datetime.now().date() - timedelta(days=i)
                    }
                )
            
            # Create alerts
            Alert.objects.get_or_create(
                farm=farm,
                type='warning',
                title='High Temperature Alert',
                defaults={
                    'message': 'Temperature in House 1 is above normal range',
                    'is_read': False
                }
            )
        
        self.stdout.write('Created analytics data') 