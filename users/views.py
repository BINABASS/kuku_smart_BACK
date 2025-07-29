from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import CustomUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get', 'put'], url_path='profile')
    def profile(self, request):
        """Get or update the current user's profile"""
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data)
        
        elif request.method == 'PUT':
            serializer = self.get_serializer(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'message': 'Profile updated successfully',
                    'user': serializer.data
                })
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['put'], url_path='change-password')
    def change_password(self, request):
        """Change the current user's password"""
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        
        if not current_password or not new_password:
            return Response({
                'error': 'Both current_password and new_password are required'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Verify current password
        user = authenticate(username=request.user.email, password=current_password)
        if not user:
            return Response({
                'error': 'Current password is incorrect'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Set new password
        request.user.set_password(new_password)
        request.user.save()
        
        return Response({
            'message': 'Password changed successfully'
        })
