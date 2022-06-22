from rest_framework import serializers
from .models import Flight, Reservation

class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_ailines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "estimatedtime_of_departure"
        )