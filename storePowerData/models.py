from django.db import models

# Create your models here.
class Reading(models.Model):
    circuit_num = models.IntegerField()
    circuit_name = models.CharField(max_length=64)
    voltage = models.FloatField()
    current = models.FloatField()
    datetime = models.DateTimeField()

class PBE(models.Model):
    serial_num = models.IntegerField()
    model = models.CharField(max_length=128)
    operating_system = models.CharField(max_length=128)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    reading = models.ManyToManyField(Reading)



class User(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    salt = models.CharField(max_length=64)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=128)
    pbe = models.ManyToManyField(PBE)
