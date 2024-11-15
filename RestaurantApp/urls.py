
from django.contrib import admin
from django.urls import path
from RestaurantApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),
    path('About/', views.About, name='About'),
    path('chef/', views.chef, name='chef'),
    path('contact/', views.contact, name='contact'),
    path('Events/', views.Events, name='Events'),
    path('Menu/', views.Menu, name='Menu'),
    path('Special/', views.Special, name='Special'),
    path('gallery/', views.gallery, name='gallery'),
    path('booking/', views.booking, name='booking'),

]
