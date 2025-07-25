from django.contrib import admin
from .models import Farm, Farmer

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email', 'status')
    list_filter = ('status',)
    search_fields = ('name', 'email', 'phone')

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('user', 'farm', 'first_name', 'last_name', 'phone', 'status')
    list_filter = ('status',)
    search_fields = ('user__email', 'first_name', 'last_name', 'phone')
