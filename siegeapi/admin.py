from django.contrib import admin
from .models import Siege


class SiegeAdmin(admin.ModelAdmin):
    list_display = ('operator', 'faction', 'gadget', 'equipment', 'equip1', 'equip2', 'armor', 'speed',
                    'side', 'weapons', 'prim1', 'prim2', 'prim3', 'secon1', 'secon2', 'counters', 'count1', 'count1p', 'count2', 'count2p')


# Register your models here.
admin.site.register(Siege, SiegeAdmin)
