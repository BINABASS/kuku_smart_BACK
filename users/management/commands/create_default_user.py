from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Creates a default admin user'

    def handle(self, *args, **options):
        try:
            # Create a superuser
            CustomUser.objects.create_superuser(
                email='admin@kukusmart.com',
                username='admin',
                password='admin123',
                is_farmer=False,
                is_admin=True
            )
            self.stdout.write(self.style.SUCCESS('Successfully created default admin user'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating default user: {str(e)}'))
