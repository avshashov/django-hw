from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    date_measurement = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    temperature = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return f'{self.sensor_id} {self.date_measurement} {self.temperature}'
