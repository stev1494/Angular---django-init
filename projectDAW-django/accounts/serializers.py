from rest_framework import serializers
from . import models


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('name','surname','address','phone','is_active')


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = ('description','tipo','price','is_active')

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = ('date','service','id_user')


        


