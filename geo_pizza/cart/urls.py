from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.index, name='cart-page'),
    path('checkout/contact/', views.contact_info, name='checkout-contact-info'),
    path('checkout/payment/', views.payment_info, name='checkout-payment-info'),
    path('checkout/review/', views.review_page, name='checkout-review-info'),
    path('checkout/complete/', views.complete, name='checkout-complete'),
]