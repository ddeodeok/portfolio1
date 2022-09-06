from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.utils.text import slugify
from django.db.models import Q


# Create your views here.
# class CowList(ListView):
#     model = Neck_sensor
#     paginate_by = 5
#     template_name = 'cow_page/base.html'

def cow (request):
    return render(
        request,
        'cow_page/base.html'
    )

def charts (request):
    return render(
        request,
        'cow_page/charts.html'
    )