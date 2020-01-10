from rest_framework import serializers
from .models import Siege

class SiegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siege
        fields = ('id', 'operator', 'faction', 'gadget', 'equipment', 'armor', 'speed', 'counters')