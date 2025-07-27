from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ItemViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'inventory/categories', CategoryViewSet)
router.register(r'inventory/items', ItemViewSet)
router.register(r'inventory/transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 