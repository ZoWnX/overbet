from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
  url(r'^list/$', views.list, name='list'), 
  url(r'^add/$', views.add, name='add'), 
  url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'), 
]