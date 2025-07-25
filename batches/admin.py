from django.contrib import admin
from .models import ActivityType, ActivitySchedule, Batch, BatchActivity, BatchFeeding

@admin.register(ActivityType)
class ActivityTypeAdmin(admin.ModelAdmin):
    list_display = ('activity_type',)
    search_fields = ('activity_type',)

@admin.register(ActivitySchedule)
class ActivityScheduleAdmin(admin.ModelAdmin):
    list_display = ('batch', 'activity_name', 'activity_day', 'activity_status')
    list_filter = ('activity_status', 'activity_day')
    search_fields = ('activity_name', 'batch__farm__name')

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('farm', 'breed', 'arrive_date', 'init_age', 'harvest_age', 'quantity', 'batch_status')
    list_filter = ('batch_status', 'arrive_date')
    search_fields = ('farm__name', 'breed__name')

@admin.register(BatchActivity)
class BatchActivityAdmin(admin.ModelAdmin):
    list_display = ('batch', 'breed_activity', 'batch_activity_date', 'batch_activity_cost')
    list_filter = ('batch_activity_date',)
    search_fields = ('batch__farm__name',)

@admin.register(BatchFeeding)
class BatchFeedingAdmin(admin.ModelAdmin):
    list_display = ('batch', 'feeding_date', 'feeding_amount', 'status')
    list_filter = ('feeding_date', 'status')
    search_fields = ('batch__farm__name',)
