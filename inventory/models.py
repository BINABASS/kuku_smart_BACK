from django.db import models
from django.utils.translation import gettext_lazy as _
from farmers.models import Farm

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'inventory_categories_tb'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    
    def __str__(self):
        return self.name

class Item(models.Model):
    ITEM_TYPES = [
        ('feed', 'Feed'),
        ('medicine', 'Medicine'),
        ('equipment', 'Equipment'),
        ('supplies', 'Supplies'),
        ('tools', 'Tools'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=ITEM_TYPES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=20, default='pieces')
    current_stock = models.IntegerField(default=0)
    min_stock_level = models.IntegerField(default=0)
    max_stock_level = models.IntegerField(default=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'inventory_items_tb'
        verbose_name = _('Item')
        verbose_name_plural = _('Items')
    
    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('in', 'Stock In'),
        ('out', 'Stock Out'),
        ('adjustment', 'Adjustment'),
        ('return', 'Return'),
    ]
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPES)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'inventory_transactions_tb'
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')
        ordering = ['-transaction_date']
    
    def __str__(self):
        return f"{self.item.name} - {self.get_transaction_type_display()} - {self.quantity}"
    
    def save(self, *args, **kwargs):
        # Calculate total amount
        self.total_amount = self.quantity * self.unit_price
        
        # Update stock levels
        if self.transaction_type == 'in':
            self.item.current_stock += self.quantity
        elif self.transaction_type == 'out':
            self.item.current_stock -= self.quantity
        elif self.transaction_type == 'adjustment':
            self.item.current_stock = self.quantity
        
        self.item.save()
        super().save(*args, **kwargs)
