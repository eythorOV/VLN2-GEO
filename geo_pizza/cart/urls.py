from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.get_cart, name='cart-page'),
    path('cart/delete/<int:cart_item_id>', views.delete_cart_item, name='delete_cart_item'),
    path('checkout/contact/', views.contact_info, name='checkout-contact-info'),
    path('checkout/payment/', views.payment_info, name='checkout-payment-info'),
    path('checkout/review/', views.review_page, name='checkout-review-info'),
    path('checkout/complete/', views.complete, name='checkout-complete'),
    path('cart/delete/all', views.delete_all_cart_items, name='delete_all_cart_items'),
]