from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.cow),
    path('charts/', views.charts),
    path('tables/', views.cowtables),
    path('sensor_tables/', views.sensorTables),
    path('create_post/', views.CowCreate.as_view()),
    path('tables_calf/', views.calf),
    path('tables_estrus/', views.estrus),
    path('tables_pregnant/', views.pregnant),
    path('tables_rearingcalf/', views.rearingcalf),
    path('tables_farm1/', views.farm1),
    path('tables_farm2/', views.farm2),
    path('tables_farm3/', views.farm3),
<<<<<<< HEAD
=======
    path('<int:pk>/', views.cow_detail)
>>>>>>> bfbc94f6430148971d6f9eb81481b1860adc320a
    # path('create_post/', views.create_post, name='create_post'),
    # path('create/', views.create, name='create'),

]