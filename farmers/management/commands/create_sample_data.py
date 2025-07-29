from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from farmers.models import Farm, Farmer
from users.models import CustomUser

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample farms and farmers data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create sample users
        user1, created = CustomUser.objects.get_or_create(
            email='farmer1@example.com',
            defaults={
                'username': 'farmer1',
                'first_name': 'John',
                'last_name': 'Doe',
                'is_farmer': True
            }
        )
        if created:
            user1.set_password('password123')
            user1.save()
            self.stdout.write(f'Created user: {user1.email}')
        
        user2, created = CustomUser.objects.get_or_create(
            email='farmer2@example.com',
            defaults={
                'username': 'farmer2',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'is_farmer': True
            }
        )
        if created:
            user2.set_password('password123')
            user2.save()
            self.stdout.write(f'Created user: {user2.email}')
        
        # Create sample farms
        farm1, created = Farm.objects.get_or_create(
            user=user1,
            defaults={
                'name': 'Smart Poultry Farm',
                'address': '123 Farm Road, Dar es Salaam',
                'phone': '+255123456789',
                'email': 'info@smartpoultry.com',
                'status': True
            }
        )
        if created:
            self.stdout.write(f'Created farm: {farm1.name}')
        
        farm2, created = Farm.objects.get_or_create(
            user=user2,
            defaults={
                'name': 'Zanzibar Chicken Co-op',
                'address': '456 Coastal Drive, Zanzibar',
                'phone': '+255987654321',
                'email': 'info@zanzibarchicken.com',
                'status': True
            }
        )
        if created:
            self.stdout.write(f'Created farm: {farm2.name}')
        
        # Create sample farmers
        farmer1, created = Farmer.objects.get_or_create(
            user=user1,
            defaults={
                'farm': farm1,
                'first_name': 'John',
                'last_name': 'Doe',
                'phone': '+255123456789',
                'address': '123 Farm Road, Dar es Salaam',
                'status': True
            }
        )
        if created:
            self.stdout.write(f'Created farmer: {farmer1.first_name} {farmer1.last_name}')
        
        farmer2, created = Farmer.objects.get_or_create(
            user=user2,
            defaults={
                'farm': farm2,
                'first_name': 'Jane',
                'last_name': 'Smith',
                'phone': '+255987654321',
                'address': '456 Coastal Drive, Zanzibar',
                'status': True
            }
        )
        if created:
            self.stdout.write(f'Created farmer: {farmer2.first_name} {farmer2.last_name}')
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!')) 