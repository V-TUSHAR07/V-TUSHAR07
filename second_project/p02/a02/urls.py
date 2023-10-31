from django.contrib import admin
from django.urls import path
from a02 import views

urlpatterns = [
    path('h',views.home,name='home'),
    path('t',views.tasks,name='task'),
    
]
