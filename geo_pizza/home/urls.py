from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home-index'),
    path('order/', views.order, name='home-order'),
]