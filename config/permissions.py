from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """Allow reads to everyone authenticated; writes only to admins."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        user = request.user
        if not user or not user.is_authenticated:
            return False
        # Accept Django admin flags or explicit ADMINISTRATOR role if present
        return bool(getattr(user, 'is_staff', False) or getattr(user, 'is_superuser', False) or getattr(user, 'role', '').upper() == 'ADMINISTRATOR')


