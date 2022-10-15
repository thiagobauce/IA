from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('upload',views.insert, name='insert'),
    path('passo-a-passo',views.tutorial, name='tutorial'),
    path('info',views.info, name='info'),
]
