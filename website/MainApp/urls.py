#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index.html'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]

