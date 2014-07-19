from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(primary_key=True, max_length=128)
    password = models.CharField(max_length=512)
    salt = models.CharField(max_length=512)

class User(models.Model):
    username = models.OneToOneField(Login)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=128)

class RaspberryPi(models.Model):
    serial_num = models.CharField(primary_key=True, max_length=64)
    username = models.ForeignKey(User)
    model = models.CharField(max_length=128)
    operating_system = models.CharField(max_length=128)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    province = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=10)

class Circuit(models.Model):
    circuit_num = models.AutoField(primary_key=True)
    serial_num = models.ForeignKey(RaspberryPi)
    circuit_name = models.CharField(max_length=64)
    state = models.BinaryField();

class Reading(models.Model):
    reading_id = models.AutoField(primary_key=True);
    circuit_num = models.ForeignKey(Circuit)
    voltage = models.FloatField()
    current = models.FloatField()
    datetime = models.DateTimeField()








