from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSeializer
from rest_framework.response import Response
class RegisterAPIs(CreateAPIView) :
    queryset = User.objects.all()
    serializer_class = RegisterSeializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSeializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            # {"message" : f"{request.first_name} {request.lastt_name} created succesfully"}
            {"message" :"User created succesfully"}
        )