from django.contrib import admin
from .models import Subscription, SubscriptionPlan, Payment

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'duration_days', 'max_devices', 'max_sensors', 'max_batches', 'is_active')
    list_filter = ('type', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'type', 'description', 'price', 'duration_days')
        }),
        ('Limits', {
            'fields': ('max_devices', 'max_sensors', 'max_batches')
        }),
        ('Features', {
            'fields': ('features',)
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'status', 'start_date', 'end_date', 'auto_renew')
    list_filter = ('status', 'auto_renew', 'start_date', 'end_date')
    search_fields = ('user__email', 'plan__name', 'manager_name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Subscription Details', {
            'fields': ('user', 'farm', 'plan', 'status')
        }),
        ('Dates', {
            'fields': ('start_date', 'end_date', 'auto_renew')
        }),
        ('Additional Info', {
            'fields': ('manager_name',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('subscription', 'amount', 'currency', 'payment_method', 'status', 'payment_date')
    list_filter = ('status', 'payment_method', 'currency', 'payment_date')
    search_fields = ('subscription__user__email', 'transaction_id')
    readonly_fields = ('payment_date',)
    fieldsets = (
        ('Payment Details', {
            'fields': ('subscription', 'amount', 'currency', 'payment_method', 'status')
        }),
        ('Transaction Info', {
            'fields': ('transaction_id',)
        }),
        ('Additional Info', {
            'fields': ('manager_name',)
        }),
        ('Timestamps', {
            'fields': ('payment_date',),
            'classes': ('collapse',)
        })
    )
