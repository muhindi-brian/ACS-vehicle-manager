# vehicles/forms.py

from django import forms
from .models import Vehicle, Booking, Maintenance

# class VehicleForm(forms.ModelForm):
#     class Meta:
#         model = Vehicle
#         fields = ['model', 'registration_number', 'capacity', 'status','image']
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['model', 'registration_number', 'capacity', 'status', 'image', 'purchase_date']  # Removed cost_per_mile

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['vehicle', 'customer_name', 'start_date', 'end_date', 'destination', 'status']

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['vehicle', 'service_date', 'service_type', 'cost', 'mileage']
