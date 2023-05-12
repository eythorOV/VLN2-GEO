from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='home-index'),
    path('home/order/', views.order, name='home-order'),
    path('aboutus/', views.about_us, name='about-us'),
    path('locations/', views.locations, name='locations'),
    path('nutrition/', views.nutrition, name='nutrition-index'),
]