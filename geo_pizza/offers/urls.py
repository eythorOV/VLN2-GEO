from django.urls import path
from . import views

urlpatterns = [
    path('offers/', views.offer_list, name='offer_list'),
]