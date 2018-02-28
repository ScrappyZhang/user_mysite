from django.urls import path
from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^index/', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.register),
    url(r'^logout/', views.logout),
    url('^ajax_val/', views.ajax_val, name='ajax_val'),
    url(r'^confirm/$', views.user_confirm),
]