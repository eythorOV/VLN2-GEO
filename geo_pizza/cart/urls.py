from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.index, name='cart-page'),
    path('checkout/', views.checkout, name='checkout-page')
]