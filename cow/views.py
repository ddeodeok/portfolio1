from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.db.models import Q
from .models import Cow, Sensor, Post
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

class CowCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    
    model = Cow
    template_name = 'cow/create_cow.html'
    fields=['cow_num','group','sensorID','age','stats','empyt_days','carving_num','birthday']

    def form_valid(self,form):
        logger = logging.getLogger()

        # 로그의 출력 기준 설정
        logger.setLevel(logging.INFO)

        # log 출력 형식
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # log 출력
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # log를 파일에 출력
        file_handler = logging.FileHandler('my.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.info('번째 방문입니다.')

        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            return super(CowCreate, self).form_valid(form)
        else:
            return redirect('/coco/')
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

class PostCreate(CreateView):
    model = Post
    template_name = 'cow/post_list.html'
    fields=['text','cow_num','group','stats','carving_num','age','empyt_days','birthday','sensorID','childbirth_id','estrus_id']









# def post(request):
#     if request.method == "POST":
#         post = Post()
#         post.text = request.POST['text']

        
#         post.cow_num = request.POST['cow_num']
#         post.group = request.POST['group']
#         post.stats = request.POST['stats']
#         post.carving_num = request.POST['carving_num']
#         post.age = request.POST['age']
#         post.empyt_days = request.POST['empyt_days']
#         post.birthday = request.POST['birthday']
#         post.sensorID = request.POST['sensorID']
#         post.save()
#         return redirect('post')
#     else:
#         post = Post.objects.all()
#         return render(request, 'cow/post_list.html', {'post':post})



        


        