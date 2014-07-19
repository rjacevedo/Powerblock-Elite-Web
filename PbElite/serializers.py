from django.forms import widgets
from rest_framework import serializers
from PbElite.models import Reading

class ReadingSerializer(serializers.Serializer):
    pk = serializers.Field()
    circuit_num = serializers.IntegerField()
    voltage = serializers.FloatField()
    current = serializers.FloatField()
    datetime = serializers.DateTimeField(default=datetime.datetime.now)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.circuit_num = attrs.get('circuit_num', instance.circuit_num)

