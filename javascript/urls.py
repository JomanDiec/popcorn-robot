from django.urls import include, path
from django.urls import re_path as url

from . import views

app_name = 'javascript'

urlpatterns = [
    path('traverse', views.traverse, name='traverse'),
    path ('ajax', views.ajax, name='ajax'),
    path('name', views.name, name='name'),
    path('name_2', views.name_2, name='name_2'),
    
]
