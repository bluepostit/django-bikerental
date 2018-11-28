from django.shortcuts import render, redirect
from .models import Customer, Rental, Vehicle
from .forms import CustomerForm, VehicleForm

def index(request):
    return render(request, 'rent/index.html')

def rental(request, rental_id):
    context = {
        'rental': Rental.objects.get(id=rental_id)
    }
    return render(request, 'rent/rental.html', context)

def rentals(request):
    return render(request, 'rent/rentals.html', {
        Rental.objects.all()[:100]
    })

def add_rental(request):
    return render(request, 'rent/add_rental.html')

def customer(request, customer_id):
    context = {
        'customer': Customer.objects.get(id=customer_id)
    }
    return render(request, 'rent/customer.html', context)

def customers(request):
    return render(request, 'rent/customers.html', {
        'customers': Customer.objects.all().order_by('last_name', 'first_name')[:100],
        'title': 'All Customers'
    })

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('rent:customer', customer_id=customer.id)
        else:
            pass
    else:
        form = CustomerForm()
    return render(request, 'rent/add_customer.html', {
        'form': form
    })

def vehicle(request, vehicle_id):
    context = {
        'vehicle': Vehicle.objects.get(id=vehicle_id)
    }
    return render(request, 'rent/vehicle.html', context)

def vehicles(request):
    return render(request, 'rent/vehicles.html', {
        'vehicles': Vehicle.objects.all().order_by(
            'vehicle_type__name',
            'vehicle_size__id'
        )[:100]
    })

def add_vehicle(request):
    form = VehicleForm()
    return render(request, 'rent/add_vehicle.html', {
        'form': form
    })


