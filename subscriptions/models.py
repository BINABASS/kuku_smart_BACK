from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import CustomUser
from farmers.models import Farm

class SubscriptionPlan(models.Model):
    PLAN_TYPES = [
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('enterprise', 'Enterprise'),
    ]
    
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=PLAN_TYPES)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(default=30)
    max_devices = models.IntegerField(default=10)
    max_sensors = models.IntegerField(default=50)
    max_batches = models.IntegerField(default=5)
    features = models.JSONField(default=dict)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'subscription_plans_tb'
        verbose_name = _('Subscription Plan')
        verbose_name_plural = _('Subscription Plans')
    
    def __str__(self):
        return f"{self.name} - {self.get_type_display()}"

class Subscription(models.Model):
    SUBSCRIPTION_STATUS = [
        ('active', 'Active'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
        ('pending', 'Pending'),
    ]
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, null=True, blank=True)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=SUBSCRIPTION_STATUS, default='pending')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    auto_renew = models.BooleanField(default=True)
    manager_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'subscriptions_tb'
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')
    
    def __str__(self):
        return f"{self.user.email} - {self.plan.name}"

class Payment(models.Model):
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_METHODS = [
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('mobile_money', 'Mobile Money'),
        ('paypal', 'PayPal'),
    ]
    
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    manager_name = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        db_table = 'payments_tb'
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
        ordering = ['-payment_date']
    
    def __str__(self):
        return f"{self.subscription.user.email} - {self.amount} {self.currency}"
