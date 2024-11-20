# vehicles/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Vehicle, Booking, Maintenance
from .forms import VehicleForm, BookingForm, MaintenanceForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect



# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Dashboard view
@login_required
def dashboard(request):
    vehicles = Vehicle.objects.all()  # Assuming you're fetching vehicles
    return render(request, 'dashboard.html', {'vehicles': vehicles})

# Display list of vehicles
@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

# Create a new vehicle
@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)  # Add `request.FILES`
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicles/add_vehicle.html', {'form': form})

#edit Vehicle
@login_required
def edit_vehicle(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicles/edit_vehicle.html', {'form': form})

#delete vehicle
@login_required
def delete_vehicle(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicle_list')
    return render(request, 'vehicles/delete_vehicle.html', {'vehicle': vehicle})



#BOOKINGS SECTION
@login_required
def bookings_list(request):
    bookings = Booking.objects.all()  # Fetch all bookings from the database
    return render(request, 'vehicles/bookings_list.html', {'bookings': bookings})

# Create a new booking
@login_required
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookings_list')
    else:
        form = BookingForm()
    return render(request, 'vehicles/add_booking.html', {'form': form})

# View to edit a booking
@login_required
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('bookings_list')  # Redirect to the bookings list after saving
    else:
        form = BookingForm(instance=booking)
    return render(request, 'vehicles/add_booking.html', {'form': form})

# View to delete a booking
@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':  # Ensure it's a POST request to prevent accidental deletes
        booking.delete()
        return redirect('bookings_list')  # Redirect to the bookings list after deletion
    return render(request, 'vehicles/delete_booking_confirm.html', {'booking': booking})


#MAINTENANCE SECTION

# Create maintenance record
@login_required
def add_maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenance_history')
    else:
        form = MaintenanceForm()
    return render(request, 'vehicles/add_maintenance.html', {'form': form})

@login_required
def maintenance_history(request):
    maintenances = Maintenance.objects.all()
    return render(request, 'vehicles/maintenance_history.html', {'maintenances': maintenances})