from django.forms import widgets
from rest_framework import serializers
from PbElite.models import Reading
import datetime

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('circuit', 'voltage', 'current', 'timestamp')
