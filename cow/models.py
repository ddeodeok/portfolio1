from operator import mod
from pyexpat import model
from venv import create
from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown
import os
from distutils.command.upload import upload


class Sensor(models.Model):
    _id = models.CharField(max_length=50)
    sensor_ver = models.CharField(max_length=50)
    msg_ver = models.IntegerField()
    sensorID = models.CharField(max_length=50)
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


class Pre_childbirth(models.Model):
    pregnancy_days = models.IntegerField()
    pre_childbirth = models.DateTimeField()
    fertilization_date = models.DateTimeField()


class Estrus(models.Model):
    after_estrus = models.IntegerField()
    after_fertilization = models.IntegerField()
    estrus_score = models.IntegerField()


class Cow(models.Model):
    cow_num = models.CharField(max_length=50,unique=True)
    group = models.CharField(max_length=50,default='new_cow')
    stats = models.CharField(max_length=50)
    carving_num = models.IntegerField(default= 0)
    age = models.IntegerField()
    postpartal_days = models.IntegerField(blank=True, null=True)
    empyt_days = models.IntegerField()
    birthday = models.DateTimeField()

    sensorID = models.ForeignKey(Sensor,on_delete=models.CASCADE, null=True, blank=True)
    childbirth_id = models.ForeignKey(Pre_childbirth, on_delete=models.CASCADE, null=True, blank=True)
    estrus_id = models.ForeignKey(Estrus, on_delete=models.CASCADE, null=True, blank=True)


class Event(models.Model):
    event_time = models.DateTimeField()
    event_name = models.CharField(max_length=50)
    description = models.TextField()
   
    cid = models.ForeignKey(Cow, on_delete=models.CASCADE)
