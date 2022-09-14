from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.cow),
    path('charts/', views.charts),
    path('tables/', views.tables),
    path('sensor_tables/', views.sensorTables),
    path('create_post/', views.CowCreate.as_view()),
    # path('create_post/', views.create_post, name='create_post'),
    # path('create/', views.create, name='create'),

]