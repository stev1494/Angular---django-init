from rest_framework import viewsets
from . import models
from . import serializers


class ClientViewset(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class ServiceViewset(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

class AppointmentViewset(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer   


