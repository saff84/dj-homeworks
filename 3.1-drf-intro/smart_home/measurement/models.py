from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)


class Measurement(models.Model):
    id_sensor = models.ForeignKey(
        Sensor,
        related_name='measurements',
        on_delete=models.CASCADE)
    temp = models.CharField(max_length=4)
    date_temp = models.DateTimeField('date_published', auto_now=True)
