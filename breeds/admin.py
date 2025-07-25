from django.contrib import admin
from .models import Breed, BreedActivity, BreedCondition, BreedFeeding, ConditionType, FoodType

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(BreedActivity)
class BreedActivityAdmin(admin.ModelAdmin):
    list_display = ('breed', 'activity_type', 'age', 'breed_activity_status')
    list_filter = ('breed_activity_status', 'activity_type')
    search_fields = ('breed__name',)

@admin.register(BreedCondition)
class BreedConditionAdmin(admin.ModelAdmin):
    list_display = ('breed', 'condition_type', 'condition_min', 'condition_max')
    list_filter = ('condition_type',)
    search_fields = ('breed__name',)

@admin.register(BreedFeeding)
class BreedFeedingAdmin(admin.ModelAdmin):
    list_display = ('breed', 'food_type', 'age', 'quantity', 'frequency')
    list_filter = ('food_type', 'breed_feed_status')
    search_fields = ('breed__name',)

@admin.register(ConditionType)
class ConditionTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(FoodType)
class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
