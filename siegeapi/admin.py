from django.contrib import admin
from .models import Siege

class SiegeAdmin(admin.ModelAdmin):
    list_display = ('operator', 'faction', 'gadget', 'equipment', 'armor', 'speed', 'counters')


# Register your models here.
admin.site.register(Siege, SiegeAdmin)