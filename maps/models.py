
from django.db import models

charger_types = (
    ('Level 1 Charging', 'Level 1 Charging'),
    ('Level 2 Charging', 'Level 2 Charging'),
    ('DC Fast Charging', 'DC Fast Charging')
)
class ChargingStation(models.Model):
    name = models.CharField(max_length=255)
    charger_type = models.CharField(max_length=125, choices=charger_types, default='Level 1 Charging')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name