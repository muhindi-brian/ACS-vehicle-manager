# vehicles/admin.py

from django.contrib import admin
from .models import Vehicle, Booking, Maintenance

admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Maintenance)
