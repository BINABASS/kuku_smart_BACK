from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from farmers.models import Farm

class Income(models.Model):
    INCOME_TYPES = [
        ('egg_sales', 'Egg Sales'),
        ('meat_sales', 'Meat Sales'),
        ('live_bird_sales', 'Live Bird Sales'),
        ('subscription', 'Subscription'),
        ('consultation', 'Consultation'),
        ('other', 'Other'),
    ]
    
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=INCOME_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'financial_income_tb'
        verbose_name = _('Income')
        verbose_name_plural = _('Income')
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.get_type_display()} - {self.amount}"

class Expense(models.Model):
    EXPENSE_TYPES = [
        ('feed', 'Feed'),
        ('medicine', 'Medicine'),
        ('labor', 'Labor'),
        ('equipment', 'Equipment'),
        ('utilities', 'Utilities'),
        ('transport', 'Transport'),
        ('maintenance', 'Maintenance'),
        ('other', 'Other'),
    ]
    
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=EXPENSE_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'financial_expenses_tb'
        verbose_name = _('Expense')
        verbose_name_plural = _('Expenses')
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.get_type_display()} - {self.amount}"

class Budget(models.Model):
    BUDGET_TYPES = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('yearly', 'Yearly'),
    ]
    
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=BUDGET_TYPES)
    category = models.CharField(max_length=100)
    allocated_amount = models.DecimalField(max_digits=10, decimal_places=2)
    spent_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'financial_budgets_tb'
        verbose_name = _('Budget')
        verbose_name_plural = _('Budgets')
    
    def __str__(self):
        return f"{self.category} - {self.allocated_amount}"
    
    @property
    def remaining_amount(self):
        return self.allocated_amount - self.spent_amount
    
    @property
    def spent_percentage(self):
        if self.allocated_amount > 0:
            return (self.spent_amount / self.allocated_amount) * 100
        return 0
