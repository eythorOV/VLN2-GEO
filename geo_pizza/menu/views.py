from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Pizza, Toppings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from cart.models import Cart, CartItem, ContactInfo, PaymentInfo
from offers.models import SpecialOffer, LunchOffer, TwoForOne
from django.contrib.auth.models import User

def get_pizza_by_id(request, id):
    pizza = Pizza.objects.get(pk=id)
    toppings = pizza.toppings.all()
    context = {
        'pizza': pizza,
        'toppings': toppings,
    }
    return render(request, 'menu/pizza_desc.html', context)

def index(request):
    context = {
        'pizzas': Pizza.objects.all()}
    return render(request, 'menu/index.html', context)

@login_required
def add_to_cart(request, product_type, product_id, quantity):
    print('in add_to_cart')
    cart = Cart.objects.get(user=request.user)
    for cart_item in cart.cart_items.all():
        if cart_item.pizza.id == product_id:
            if quantity == 0:
                cart_item.quantity += 1
            else: 
                cart_item.quantity += quantity
            cart_item.save()
            messages.success(request, 'Item added to cart')
            print('Item added to cart')
            return render(request, 'cart/cart.html')
    else:
        cart = Cart.objects.get(user=request.user)
        if product_type == 'pizza':
            print('in Pizza')
            product = get_object_or_404(Pizza, pk=product_id)
            cart_item = CartItem.objects.create(product_type=product_type, quantity=quantity, pizza=product, cart=cart)
        elif product_type == 'SpecialOffer':
            product = get_object_or_404(SpecialOffer, pk=product_id)
            cart_item = CartItem.objects.create(product_type=product_type, special_offer=product, cart=cart)
        elif product_type == 'LunchOffer':
            product = get_object_or_404(LunchOffer, pk=product_id)
            cart_item = CartItem.objects.create(product_type=product_type, lunch_offer=product, cart=cart)
        elif product_type == 'TwoForOne':
            product = get_object_or_404(TwoForOne, pk=product_id)
            cart_item = CartItem.objects.create(product_type=product_type, two_for_one=product, cart=cart)
        else:
            print(
                f'Invalid product type: {product_type} for product_id: {product_id} and quantity: {quantity}'
            )
            messages.error(request, 'Invalid product type')
            return render(request, 'cart/cart.html')
        cart_item.save()
        messages.success(request, 'Item added to cart')
    return render(request, 'cart/cart.html')