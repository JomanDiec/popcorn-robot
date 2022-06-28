from django.urls import include, path
from django.urls import re_path as url

from . import views

app_name = 'haunted_mansion'

urlpatterns = [
    path('index', views.index, name='index'),
    path('haunted_mansion', views.haunted_mansion, name='haunted_mansion'),
    
]