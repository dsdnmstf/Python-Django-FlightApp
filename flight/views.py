from django import views
from .models import Flight, Reservation
from .serializers import FlightSerializer
from rest_framework import viewsets
from .permissions import IsStufforReadOnly

class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStufforReadOnly,) # or in list


