from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, BudgetViewSet

router = DefaultRouter()
router.register(r'financials/income', IncomeViewSet)
router.register(r'financials/expenses', ExpenseViewSet)
router.register(r'financials/budgets', BudgetViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 