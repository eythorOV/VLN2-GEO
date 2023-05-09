from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.index, name='menu-index'),
    path('menu/<int:id>', views.get_pizza_by_id, name='pizza-detail'),
]