from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
]
# Create your views here.
