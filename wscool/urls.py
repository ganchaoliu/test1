from django.conf.urls import url
from django.urls import path

from wscool import views

urlpatterns = [
    path('index', views.index),
]