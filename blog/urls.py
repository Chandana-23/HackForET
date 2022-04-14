from . import views
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',views.home,name='/'),
    path('register',views.register,name='register'),
    path('login', views.login, name='login'),
    path('add',views.add,name='add'),
    path('logged',views.logged,name='logged'),
    path('logout',views.logout,name='logout'),
    path('write',views.write,name='write'),
    path('addblog',views.addblog,name='addblog'),
]