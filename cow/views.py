from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.db.models import Q
from .models import Cow, Sensor
import logging

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

def cowtables (request):
    cows = Cow.objects.order_by('-pk')[:100]
    return render(
        request,
        'cow/tables.html',
        {
            'cows':cows,
        }
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

def calf (request):
    calfs = Cow.objects.filter(group__contains='calf')

    return render(
        request,
        'cow/tables_calf.html',
        {
            'calfs':calfs,
        }
    )

def farm1 (request):
    farm1s = Cow.objects.filter(group__contains='first')

    return render(
        request,
        'cow/tables_farm1.html',
        {
            'farm1s':farm1s,
        }
    )

def farm2 (request):
    farm2s = Cow.objects.filter(group__contains='second')

    return render(
        request,
        'cow/tables_farm2.html',
        {
            'farm2s':farm2s,
        }
    )

def farm3 (request):
    farm3s = Cow.objects.filter(group__contains='third')

    return render(
        request,
        'cow/tables_farm3.html',
        {
            'farm3s':farm3s,
        }
    )





def estrus (request):
    return render(
        request,
        'cow/tables_estrus.html'
    )

def pregnant (request):
    return render(
        request,
        'cow/tables_pregnant.html'
    )

def rearingcalf (request):
    return render(
        request,
        'cow/tables_rearingcalf.html'
    )

class CowCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Cow
    
    template_name = 'cow/create_cow.html'
    fields=['cow_num','group','stats','carving_num','age','empyt_days','birthday','sensorID']

    def form_valid(self,form):
        logger = logging.getLogger("main")	# Logger 선언
        stream_hander = logging.StreamHandler()	# Logger의 output 방법 선언
        logger.addHandler(stream_hander)	# Logger의 output 등록

        logger.setLevel(logging.DEBUG)
        logging.warning("조심하자!")
        logging.error("오류 발생")
        logging.critical(form)
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(CowCreate, self).form_valid(form)
        else:
            return redirect('/login/')
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff


# def create_post(request):
#     return render(request, 'cow/create_cow.html')

# def create(request, ) :
#     if(request.method == 'POST'):
#         post = Cow()

#         post.cow_num = request.POST.cow_num

#         post.save()
#     return redirect('cow/create_cow.html')





        


        