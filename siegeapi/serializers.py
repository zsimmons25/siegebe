from rest_framework import serializers
from .models import Siege


class SiegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siege
        fields = ('id', 'operator', 'faction', 'gadget', 'equip1', 'equip2', 'armor', 'speed',
        'side', 'prim1', 'prim2', 'prim3', 'secon1', 'secon2', 'count1', 'count1p', 'count2', 'count2p', 'release')
