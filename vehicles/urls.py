# vehicles/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from django.conf.urls.static import static

@method_decorator(csrf_exempt, name='dispatch')
class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('', views.login_view, name='login'),  # Set login as the homepage
    path('dashboard/', views.dashboard, name='dashboard'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('add-vehicle/', views.add_vehicle, name='add_vehicle'),
    path('add-booking/', views.add_booking, name='add_booking'),
    path('add-maintenance/', views.add_maintenance, name='add_maintenance'),
   
    # Add the URL pattern for viewing, editing, and deleting bookings 
    path('booking/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('booking/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('bookings/', views.bookings_list, name='bookings_list'),

    path('logout/', LogoutView.as_view(), {'next_page': '/'}, name='logout'),
    path('maintenance-history/', views.maintenance_history, name='maintenance_history'),
    path('vehicles/<int:pk>/edit/', views.edit_vehicle, name='edit_vehicle'),
    path('vehicles/<int:pk>/delete/', views.delete_vehicle, name='delete_vehicle'),


    

    # path('add-maintenance/', views.add_maintenance, name='add_maintenance'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)