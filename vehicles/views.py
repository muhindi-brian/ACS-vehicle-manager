# vehicles/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Vehicle, Booking, Maintenance
from .forms import VehicleForm, BookingForm, MaintenanceForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from datetime import datetime
from django.contrib import messages
from .forms import CMSForm
from .models import CMS


def my_view(request):
    cms = CMS.objects.first()  # Get the first CMS entry
    return render(request, 'base_generic.html', {'cms': cms})

def cms_dashboard(request):
    # Retrieve existing CMS settings
    cms = CMS.objects.first()

    if request.method == 'POST':
        form = CMSForm(request.POST, request.FILES, instance=cms)
        if form.is_valid():
            form.save()
            return redirect('cms_dashboard')  # Redirect to CMS dashboard after save
    else:
        form = CMSForm(instance=cms)

    return render(request, 'admin/cms_dashboard.html', {'form': form})

def cms_dashboard(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("You are not authorized to access this page.")


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
# @login_required
# def add_booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('bookings_list')
#     else:
#         form = BookingForm()
#     return render(request, 'vehicles/add_booking.html', {'form': form})

# Create a new booking
# @login_required
# def add_booking(request):
#     if request.method == 'POST':
#         form = BookingForm(request.POST)
        
#         if form.is_valid():
#             # Get form data
#             start_date = form.cleaned_data.get('start_date')
#             end_date = form.cleaned_data.get('end_date')
#             vehicle = form.cleaned_data.get('vehicle')

#             # Check for overlapping bookings for the selected vehicle
#             overlapping_bookings = Booking.objects.filter(vehicle=vehicle).filter(
#                 start_date__lt=end_date,  # Start date is before the end date of the new booking
#                 end_date__gt=start_date   # End date is after the start date of the new booking
#             )

#             # If overlapping bookings exist, show a warning message and prevent saving
#             if overlapping_bookings.exists():
#                 messages.error(request, 'The selected vehicle is already booked for these dates.')
#                 return redirect('add_booking')  # Redirect to the booking form with an error message

#             # If no overlap, save the form
#             form.save()

#             # Redirect to the bookings list page
#             return redirect('bookings_list')

#     else:
#         form = BookingForm()

#     return render(request, 'vehicles/add_booking.html', {'form': form})

@login_required
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Get form data
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            vehicle = form.cleaned_data.get('vehicle')

            # Check for overlapping bookings for the selected vehicle
            overlapping_bookings = Booking.objects.filter(vehicle=vehicle).filter(
                start_date__lt=end_date, 
                end_date__gt=start_date
            )
            # Check if vehicle is under maintenance
            maintenance_schedules = Maintenance.objects.filter(vehicle=vehicle).filter(
                service_date__gte=start_date, service_date__lte=end_date
            )

            if overlapping_bookings.exists():
                messages.error(request, 'The selected vehicle is already booked for these dates.')
                return redirect('add_booking')
            
            if maintenance_schedules.exists():
                messages.error(request, 'The selected vehicle is scheduled for maintenance during these dates.')
                return redirect('add_booking')

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

# Calendar View
def booking_calendar(request):
    # Get all bookings to display on the calendar
    bookings = Booking.objects.all()

    # Prepare booking data for FullCalendar
    events = []
    for booking in bookings:
        events.append({
            'title': f"Booked by {booking.customer_name}",
            'start': booking.start_date.strftime('%Y-%m-%d'),  # Format the date to FullCalendar format
            'end': booking.end_date.strftime('%Y-%m-%d'),      # Format the date to FullCalendar format
            'description': booking.destination,
        })

    # Return the data to the template
    return render(request, 'vehicles/booking_calendar.html', {'events': events})


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