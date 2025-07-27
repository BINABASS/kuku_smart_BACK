from rest_framework import serializers
from .models import Income, Expense, Budget

class IncomeSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    
    class Meta:
        model = Income
        fields = '__all__'
        read_only_fields = ('farm_name',)

class ExpenseSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    
    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ('farm_name',)

class BudgetSerializer(serializers.ModelSerializer):
    farm_name = serializers.CharField(source='farm.name', read_only=True)
    remaining_amount = serializers.ReadOnlyField()
    spent_percentage = serializers.ReadOnlyField()
    
    class Meta:
        model = Budget
        fields = '__all__'
        read_only_fields = ('farm_name', 'remaining_amount', 'spent_percentage') 