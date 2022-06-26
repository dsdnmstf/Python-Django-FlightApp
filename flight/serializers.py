from rest_framework import serializers
from .models import Flight, Passenger, Reservation

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

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
        )

class ReservationSerializer(serializers.ModelSerializer):
   passenger = PassengerSerializer(many=True, required=False)
   flight = serializers.StringRelatedField() #default read_only=True
   flight_id = serializers.IntegerField(write_only=True)
   user = serializers.StringRelatedField() #default read_only=True
   user_id = serializers.IntegerField(write_only=True, required=False)

   class Meta:
    model = Reservation
    fields = (
        "id",
        "flight", #GET
        "flight_id", #POST
        "user", #GET
        "user_id", #POST
        "passenger",
    )

    def create(self, validate_data):
        print(validate_data)
        passenger_data = validate_data.pop("passanger")
        print(passenger_data)
        validate_data["user_id"] = self.context["request"].user.id
        reservation = Reservation.objects.create(**validate_data)
        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)
        reservation.save()
        return reservation

class StuffFlightSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True, read_only=True)

    class Meta:
        model = Flight
        fields = (
            "id",
            "flight_number",
            "operation_ailines",
            "departure_city",
            "arrival_city",
            "date_of_departure",
            "estimatedtime_of_departure",
            "reservations",
        )


