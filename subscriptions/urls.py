from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet, SubscriptionPlanViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'subscription-plans', SubscriptionPlanViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 