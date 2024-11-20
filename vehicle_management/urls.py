# vehicle_management/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehicles.urls')),
    path('vehicles/', include('vehicles.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # This adds the login URL and others
]
