from django.contrib import admin
from .models import Siege


class SiegeAdmin(admin.ModelAdmin):
    list_display = ('operator', 'faction', 'gadget', 'equip1', 'equip2', 'armor', 'speed',
                    'side', 'prim1', 'prim2', 'prim3', 'secon1', 'secon2', 'count1', 'count1p', 'count2', 'count2p', 'release')


# Register your models here.
admin.site.register(Siege, SiegeAdmin)
