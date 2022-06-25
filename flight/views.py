from django import views
from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationSerializer
from rest_framework import viewsets
from .permissions import IsStufforReadOnly

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStufforReadOnly,) # or in list

class Reservationview(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)