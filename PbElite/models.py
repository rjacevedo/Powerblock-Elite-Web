from django.db import models
from djcelery.models import PeriodicTask, CrontabSchedule
import datetime

# Create your models here.
class Login(models.Model):
    username = models.CharField(unique=True, max_length=128)
    password = models.CharField(max_length=512)
    salt = models.CharField(max_length=512)

class User(models.Model):
    login = models.OneToOneField(Login)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=128)

class RaspberryPi(models.Model):
    serial_num = models.CharField(unique=True, max_length=64)
    user = models.ForeignKey(User)
    model = models.CharField(max_length=128)
    street_num = models.IntegerField()
    street_name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=10)

class Circuit(models.Model):
    raspberry_pi = models.ForeignKey(RaspberryPi)
    circuit_name = models.CharField(max_length=64)
    state = models.BooleanField(default=True);
    changed = models.BooleanField(default=0);

class Reading(models.Model):
    circuit = models.ForeignKey(Circuit)
    power = models.FloatField()
    timestamp = models.DateTimeField(default=datetime.datetime.now)

class Schedule(models.Model):
    start_time = models.DateTimeField(default=datetime.datetime.now)
    end_date = models.DateTimeField(default=datetime.datetime.now)
    start_id = models.ForeignKey(PeriodicTask, related_name='+', null=True)
    end_id = models.ForeignKey(PeriodicTask, related_name='+', null=True)
    description = models.CharField(max_length=512)
    circuit = models.ForeignKey(Circuit)
    state = models.BooleanField(default=0)

    def delete(self, *args, **kwargs):
        self.start_id.delete()
        self.end_id.delete()
        return super(self.__class__, self).delete(*args, **kwargs)

class UserSessions(models.Model):
    username = models.ForeignKey(User)
    randomhash = models.CharField(max_length=256)
    expiry_datetime = models.DateTimeField()






