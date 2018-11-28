from django import forms
from .models import Customer, Vehicle

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'city',
            'country'
        ]

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'vehicle_type',
            'vehicle_size',
            'real_cost'
        ]