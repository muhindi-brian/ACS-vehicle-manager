# vehicles/admin.py

from django.contrib import admin
from .models import Vehicle, Booking, Maintenance

from .models import CMS

class CMSAdmin(admin.ModelAdmin):
    list_display = ('logo',)  # Display logo in the list
    search_fields = ['logo']  # Enable search by logo

    # If you want to display the form fields more elegantly, you can customize the fieldsets:
    fieldsets = (
        (None, {
            'fields': ('logo',)
        }),
    )

admin.site.register(CMS, CMSAdmin)

admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(Maintenance)
