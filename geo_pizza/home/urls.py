from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('home/', views.index, name='home-index'),
    path('home/order/', views.order, name='home-order'),
    path('home/aboutus/', views.about_us, name='about-us'),
    path('home/locations/', views.locations, name='locations'),
]