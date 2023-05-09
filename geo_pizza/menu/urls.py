from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index, name='menu-index'),
    path('menu/<int:id>', views.pizza_desc, name='pizza-detail'),
]