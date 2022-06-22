from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    operation_ailines = models.CharField(max_length=20)
    departure_city = models.CharField(max_length=30)
    arrival_city = models.CharField(max_length=30)
    date_of_departure = models.DateField()
    estimatedtime_of_departure = models.TimeField()

    def __str__(self):
        return f"{self.flight_number} - {self.departure_city} - {self.arrival_city} "

class Passenger(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} "

class Reservation(models.Model):
    #reservations_number = models.CharField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    passenger = models.ManyToManyField(Passenger, releted_name = "passengers")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE  releted_name = "reservations")
    