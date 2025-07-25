from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('farmers.urls')),
    path('api/', include('breeds.urls')),
    path('api/', include('batches.urls')),
]
