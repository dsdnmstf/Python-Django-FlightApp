from rest_framework import routers
from .views import FlightView, Reservationview

router = routers.DefaultRouter()
router.register('flights', FlightView)
router.register('reservation', Reservationview)


urlpatterns = [

]

urlpatterns += router.urls
