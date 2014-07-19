from django.db import models
import datetime

# Create your models here.
class Login(models.Model):
    username = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=512)
    salt = models.CharField(max_length=512)

class User(models.Model):
    username = models.OneToOneField(Login)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=128)

class RaspberryPi(models.Model):
    serial_num = models.CharField(unique=True, max_length=64)
    username = models.ForeignKey(User)
    model = models.CharField(max_length=128)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=10)

class Circuit(models.Model):
    circuit_num = models.IntegerField()
    serial_num = models.ForeignKey(RaspberryPi)
    circuit_name = models.CharField(max_length=64)
    state = models.BinaryField();

class Reading(models.Model):
    circuit_num = models.ForeignKey(Circuit)
    voltage = models.FloatField()
    current = models.FloatField()
    datetime = models.DateTimeField(default=datetime.datetime.now)








