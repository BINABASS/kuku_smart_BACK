from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import CustomUser

def get_user_permissions(user):
    """Get user permissions based on role"""
    if user.is_admin:
        return {
            'canManageUsers': True,
            'canManageBatches': True,
            'canManageDevices': True,
            'canViewAnalytics': True,
            'canManageSubscriptions': True,
            'canManageInventory': True,
            'canManageKnowledgeBase': True,
            'canManageFinancials': True,
            'canCreateManagerAccount': True,
            'canManageManagerAccounts': True
        }
    else:  # Manager role
        return {
            'canManageBatches': True,
            'canManageDevices': True,
            'canViewAnalytics': True,
            'canManageInventory': True,
            'canManageKnowledgeBase': True,
            'canManageFinancials': True,
            'canManageUsers': False,
            'canManageSubscriptions': False,
            'canCreateManagerAccount': False,
            'canManageManagerAccounts': False
        }

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            if not email or not password:
                return Response({
                    'error': 'Please provide both email and password'
                }, status=status.HTTP_400_BAD_REQUEST)

            user = authenticate(email=email, password=password)

            if user is None:
                return Response({
                    'error': 'Invalid email or password'
                }, status=status.HTTP_401_UNAUTHORIZED)

            token, created = Token.objects.get_or_create(user=user)
            
            # Determine user role
            role = 'admin' if user.is_admin else 'manager'
            
            # Get user name
            name = f"{user.first_name} {user.last_name}".strip() if user.first_name or user.last_name else user.username
            
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'role': role,
                    'name': name,
                    'permissions': get_user_permissions(user)
                }
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@method_decorator(csrf_exempt, name='dispatch')
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        username = request.data.get('username')
        role = request.data.get('role', 'manager')  # Default to manager
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')

        if not email or not password or not username:
            return Response({
                'error': 'Please provide email, password, and username'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create user with role
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_admin=(role == 'admin')
            )
            
            token = Token.objects.create(user=user)
            
            # Determine user role
            user_role = 'admin' if user.is_admin else 'manager'
            
            # Get user name
            name = f"{user.first_name} {user.last_name}".strip() if user.first_name or user.last_name else user.username
            
            return Response({
                'token': token.key,
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'role': user_role,
                    'name': name,
                    'permissions': get_user_permissions(user)
                }
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'error': str(e)
            }, status=status.HTTP_400_BAD_REQUEST)
