from django.urls import include, path
from django.urls import re_path as url

from . import views

app_name = 'javascript'

urlpatterns = [
    path('traverse', views.traverse, name='traverse'),
    path('haunted_mansion', views.haunted_mansion, name='haunted_mansion'),
    
]
