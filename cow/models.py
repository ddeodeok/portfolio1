from operator import mod
from pyexpat import model
from venv import create
from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os
from distutils.command.upload import upload

class SensorID(models.Model):
    sensor_serial = models.CharField(max_length=50, unique=True, primary_key=True)
    sensor_ver = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.sensor_serial}'


class Sensor(models.Model):
<<<<<<< HEAD
    id = models.IntegerField(primary_key=True,unique=True)
    _id = models.CharField(max_length=50)
    sensor_ver = models.CharField(max_length=50)
    msg_ver = models.IntegerField()
=======
    _id = models.CharField(max_length=50,primary_key=True,unique=True)
    sensor_ver = models.CharField(max_length=50)
    msg_ver = models.IntegerField()
    sensor_ID = models.ForeignKey("SensorID", on_delete=models.SET_NULL, null=True)
>>>>>>> bfbc94f6430148971d6f9eb81481b1860adc320a
    macAddr = models.CharField(max_length=50)
    battery = models.FloatField()
    temp = models.FloatField()
    hpa = models.FloatField()
    acc_x = models.IntegerField()
    acc_y = models.IntegerField()
    acc_z = models.IntegerField()
    vector = models.IntegerField()
    rssi =  models.FloatField()
    time =  models.CharField(max_length=50)
    packetnum = models.IntegerField()
    kr_time =  models.CharField(max_length=50)
    sensor_ID = models.CharField(max_length=50)
    # sensor_ID_id = models.ForeignKey("SensorID", on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return f'[{self.pk}]{self.sensor_ID}'



class Pre_childbirth(models.Model):
    pregnancy_days = models.IntegerField()
    pre_childbirth = models.DateTimeField()
    fertilization_date = models.DateTimeField()


class Estrus(models.Model):
    after_estrus = models.IntegerField()
    after_fertilization = models.IntegerField()
    estrus_score = models.IntegerField()


class Cow(models.Model):
    # author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cow_num = models.CharField(max_length=50,unique=True,primary_key=True)
    group = models.CharField(max_length=50,default='new_cow')
    stats = models.CharField(max_length=50)
    carving_num = models.IntegerField(default= 0)
    age = models.IntegerField()
    empyt_days = models.IntegerField(blank=True, null=True)
    birthday = models.CharField(max_length=50,blank=True, null=True)

<<<<<<< HEAD
    SensorID_id = models.ForeignKey("SensorID", on_delete=models.SET_NULL,blank=True, null=True)
=======
    sensorID = models.ForeignKey("SensorID", on_delete=models.SET_NULL,blank=True, null=True)
>>>>>>> bfbc94f6430148971d6f9eb81481b1860adc320a
    
    def __str__(self):
        return f'[{self.pk}]{self.cow_num}'


class Event(models.Model):
    event_time = models.DateTimeField()
    event_name = models.CharField(max_length=50)
    description = models.TextField()
   
    cid = models.ForeignKey(Cow, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}]{self.event_time}'
