from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.db.models import Q
from .models import Cow, Sensor

# Create your views here.

def cow (request):
    return render(
        request,
        'cow/main.html'
    )

def charts (request):
    return render(
        request,
        'cow/charts.html'
    )

def tables (request):
    return render(
        request,
        'cow/tables.html'
    )

def sensorTables (request):
    sensors = Sensor.objects.order_by('-pk')[:100]

    return render(
        request,
        'cow/sensor_tables.html',
        {
            'sensors':sensors,
        }
    )

class CowCreate(CreateView):
    model = Cow
    fields=['cow_num','group','sensorID','age','stats','empyt_days','carving_num','birthday']
    template_name = 'cow/create_cow.html'

    def form_valid(self,form):
        response = super(CowCreate, self).form_valid(form)
        return response