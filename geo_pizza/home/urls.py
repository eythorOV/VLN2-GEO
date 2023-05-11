from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('home/', views.index, name='home-index'),
    path('home/order/', views.order, name='home-order'),
    path('aboutus/', views.about_us, name='about-us'),
    path('locations/', views.locations, name='locations'),
    path('ingredients_nutrition/', views.ing_nut, name='nutrition_ingredients-index'),
]