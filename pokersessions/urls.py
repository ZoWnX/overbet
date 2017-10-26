from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
  url(r'^start/', views.start, name='start'), 
  url(r'^active/', views.active, name='active'), 
  url(r'^list/', views.list, name='list'),
  url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
]
