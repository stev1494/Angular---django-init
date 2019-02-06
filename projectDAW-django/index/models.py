from django.db import models
from datetime import date, datetime


class Client(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)
    is_active = models.BooleanField(default = True)

class Product(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    price = models.FloatField(null = True, blank = True, default = None)


class Work_Area(models.Model):
    area_name =  models.CharField(max_length = 100)
    salary = models.FloatField(default = 500)

class Employee(models.Model):
    name = models.CharField(max_length = 50)
    surname = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 10)

class Admin(models.Model):
    username = models.CharField(max_length = 10, unique = True)
    password = models.CharField(max_length = 20)
    id_employee = models.ForeignKey('Employee', null = True, blank = True, on_delete = models.CASCADE)

class Market(models.Model):
    quantity = models.IntegerField()
    id_product = models.ForeignKey('Product', null = True, blank = True, on_delete = models.CASCADE)

class Service(models.Model):
    description = models.TextField()
    tipo = models.CharField(max_length = 50, default= None)
    price = models.FloatField(null = True, blank = True, default = None)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.tipo

class Appointment(models.Model):
    date = models.DateTimeField(null=False, blank=True,default=datetime.now)
    service = models.ForeignKey('Service', null = True, blank = True, on_delete = models.CASCADE)
    id_user = models.ForeignKey('auth.user', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.service


class Service_Area(models.Model):
    id_work_area = models.ForeignKey('Work_Area', null = True, blank = True, on_delete = models.CASCADE)
    id_service = models.ForeignKey('Service', null = True, blank = True, on_delete = models.CASCADE)

class Service_Employee(models.Model):
    id_employee_area = models.ForeignKey('Work_Area', null = True, blank = True, on_delete = models.CASCADE)
    id_service = models.ForeignKey('Service', null = True, blank = True, on_delete = models.CASCADE)
