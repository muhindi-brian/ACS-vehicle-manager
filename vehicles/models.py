# vehicles/models.py

from django.db import models
from django.contrib.auth.models import User

# Define Vehicle model
class Vehicle(models.Model):
    VEHICLE_STATUS = [
        ('available', 'Available'),
        ('booked', 'Booked'),
        ('maintenance', 'Maintenance'),
    ]
    
    model = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    status = models.CharField(max_length=20, choices=VEHICLE_STATUS, default='available')
    image = models.ImageField(upload_to='vehicles/images/', blank=True, null=True)  # New field

    
    def __str__(self):
        return f"{self.model} - {self.registration_number}"

# Define Booking model
class Booking(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
    ]
    
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    destination = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Booking for {self.customer_name} ({self.status})"

# Define Maintenance model
class Maintenance(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_type = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.service_type} for {self.vehicle.model}"
