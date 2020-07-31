#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('menu/', views.menu, name='menu'),
    path('chat/', views.chat, name='chat'),
    path('signup/', views.signup, name='signup'),
    path('hide_button/', views.hide_button,name='hide_button'),
    path('logout/', views.logout,name='logout'),
    path('user_login/', views.user_login,name='user_login'),
    path('get_category/', views.get_category,name='get_category'),
    path('get_product/', views.get_product,name='get_product'),
    path('update_products/', views.update_products,name='update_products'),
]

