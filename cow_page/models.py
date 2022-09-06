from django.db import models

# Create your models here.
class Neck_sensor(models.Model):
    sensor_id = models.CharField(max_length=50)