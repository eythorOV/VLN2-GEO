from django.urls import path
from . import views
urlpatterns = [
    path('offers/', views.index, name='offers-index'),
    path('offers/specialoffer/', views.special, name='offers-special'),
    path('offers/lunchoffer/', views.lunch, name='offers-lunch'),
    path('offers/twoforone/', views.twoforone, name='offers-twoforone'),
    path('offers/add_to_cart', views.add_to_cart, name='offers-special-add-to-cart'),
]