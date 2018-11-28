from django.urls import path
from . import views

app_name = 'rent'
urlpatterns = [
    path('', views.index, name='index'),
    path('rentals/', views.rentals, name='rentals'),
    path('rentals/<int:rental_id>/', views.rental, name='rental'),
    path('rentals/add/', views.add_rental, name='add_rental'),
    path('customers/', views.customers, name='customers'),
    path('customers/<int:customer_id>', views.customer, name='customer'),
    path('customers/add', views.add_customer, name='add_customer'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('vehicles/<int:vehicle_id>', views.vehicle, name='vehicle'),
    path('vehicles/add', views.add_vehicle, name='add_vehicle'),

]