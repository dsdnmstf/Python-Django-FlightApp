from django import views
from .models import Flight, Reservation
from .serializers import FlightSerializer, ReservationSerializer, StuffFlightSerializer
from rest_framework import viewsets
from .permissions import IsStufforReadOnly
from datetime import date, datetime


# class SerializerByuserMixin:
#     def get_serailizer_class(self, *args, **kwargs):
#         return self.serailizer_map.get(str(self.request.user.is_staff), self.serializer_class)

class FlightView( viewsets.ModelViewSet): #SerializerByuserMixin,
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStufforReadOnly,) # or in list
    # serailizer_map = {
    #     "True" : StuffFlightSerializer,
    #     "False" : FlightSerializer
    # }

    def get_serializer_class(self):
        # serailizer = super().get_serializer_class() -->FlightSerializer
        if self.request.user.is_staff:
            return StuffFlightSerializer
        # return serailizer
        return FlightSerializer

    def get_queryset(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            queryset = Flight.objects.filter(date_of_departure__gt=today)#grater than
            if Flight.objects.filter(date_of_departure=today):
                today_qs = Flight.objects.filter(
                    date_of_departure=today).filter(
                        estimatedtime_of_departure__gt=current_time)
                queryset = queryset.union(today_qs)
            return queryset



class Reservationview(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)