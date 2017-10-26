from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
  url(r'^login/', views.login, name='login'), 
  url(r'^register/', views.register, name='register'), 
  url(r'^logout/', views.logout, name='logout'),
  url(r'^profile/view/(?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)/$', views.profile_view, name='profile_view'),
  url(r'^profile/view/', views.profile_view, name='profile_view'),
]
