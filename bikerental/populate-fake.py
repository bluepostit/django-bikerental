import os
import random
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bikerental.settings')
django.setup()

from faker import Faker
from rent.models import *
faker = Faker()

def create_customer():
    Customer.objects.create(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.safe_email(),
        phone=faker.phone_number(),
        address=faker.address(),
        city=faker.city(),
        country=faker.country()
    )

def create_vehicle_types():
    for t in ['bike', 'scooter', 'electric bike', 'jetpack']:
        VehicleType.objects.get_or_create(
            name=t
        )

def create_vehicle_sizes():
    for t in ['small', 'medium', 'large', 'extra-large']:
        VehicleSize.objects.get_or_create(
            name=t
        )

def create_rental_rates():
    pass

def create_vehicle():
    vehicle_type = VehicleType.objects.order_by('?')[0]
    vehicle_size = VehicleSize.objects.order_by('?')[0]
    real_cost = random.choice([
        150.0,
        180.0,
        220.0,
        250.0,
        310.0
    ])
    Vehicle.objects.create(
        vehicle_size=vehicle_size,
        vehicle_type=vehicle_type,
        real_cost=real_cost
    )

def create_rental():
    vehicle = Vehicle.objects.order_by('?')[0]
    customer = Customer.objects.order_by('?').first()
    Rental.objects.create(
        vehicle=vehicle,
        customer=customer
    )

if __name__ == '__main__':
    create_vehicle_sizes()
    create_vehicle_types()

    for i in range(500):
        create_vehicle()

    for i in range(100):
        create_customer()

    for i in range(100):
        create_rental()
