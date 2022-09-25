from django.contrib import admin
from .models import Sensor, Measurement
# Register your models here.

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', ]


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id_sensor', 'temp', 'date_temp']
