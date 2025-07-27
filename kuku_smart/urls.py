from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('farmers.urls')),
    path('api/', include('breeds.urls')),
    path('api/', include('batches.urls')),
    path('api/', include('devices.urls')),
    path('api/', include('sensors.urls')),
    path('api/', include('subscriptions.urls')),
    path('api/', include('inventory.urls')),
    path('api/', include('knowledge_base.urls')),
    path('api/', include('financials.urls')),
    path('api/', include('analytics.urls')),
]
