from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Detail/<int:pk>', views.detail, name='Detail'),
    path('create/', views.create, name='create'),
    path('createtask/', views.createtask, name='createtask'),
    path('sendhomework/<int:pk>', views.sendhomework, name='sendhomework'),
    path('checkhomework/', views.checkhomework, name='checkhomework'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.logoutpage, name='logout'),
]