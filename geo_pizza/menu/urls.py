from django.urls import path
from . import views


urlpatterns = [
    path('menu/', views.index, name='menu-index'),
    path('menu/<int:id>', views.get_pizza_by_id, name='pizza-detail'),
    path('menu/add_to_cart/<str:product_type>/<int:product_id>/<int:quantity>', views.add_to_cart, name='add-to-cart')
]