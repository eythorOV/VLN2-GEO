from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('home/', views.index, name='home-index'),
    path('order/', views.order, name='home-order'),
]