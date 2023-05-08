from django.urls import path
from . import views

urlpatterns = [
    path('offers/', views.index, name='offers-index'),
]