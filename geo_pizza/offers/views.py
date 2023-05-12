from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import SpecialOffer, LunchOffer, TwoForOne, Sodas, Breadsticks
from menu.models import Pizza
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from cart.models import Cart, CartItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    specialoffer = SpecialOffer.objects.first()  # Retrieve the special offer object
    lunchoffer = LunchOffer.objects.first()  # Retrieve the lunch offer object
    twoforone = TwoForOne.objects.first()  # Retrieve the two-for-one offer object
    context = {
        'title': 'Offers',
        'specialoffer': specialoffer,
        'lunchoffer': lunchoffer,
        'twoforone': twoforone
    }
    return render(request, 'offers/index.html', context)

def special(request):
    pizzas = Pizza.objects.all()
    sodas = Sodas.objects.all()  # Retrieve all sodas
    breadsticks = Breadsticks.objects.all()  # Retrieve all breadsticks
    specialoffer = SpecialOffer.objects.first()
    context = {
        'title': 'Offer - Special',
        'specialoffer': specialoffer,
        'pizzas': pizzas,
        'sodas': sodas,
        'breadsticks': breadsticks
    }
    return render(request, 'offers/special.html', context)

def lunch(request):
    pizzas = Pizza.objects.all()
    sodas = Sodas.objects.all()  # Retrieve all sodas
    lunchoffer = LunchOffer.objects.first()
    context = {
        'title': 'Offer - Lunch',
        'lunchoffer': lunchoffer,
        'pizzas': pizzas,
        'sodas': sodas
    }
    return render(request, 'offers/lunch.html', context)

def twoforone(request):
    pizzas = Pizza.objects.all()
    sodas = Sodas.objects.all()  # Retrieve all sodas
    breadsticks = Breadsticks.objects.all()  # Retrieve all breadsticks
    twoforone = TwoForOne.objects.first()
    context = {
        'title': 'Offer - Two for One',
        'twoforone': twoforone,
        'pizzas': pizzas,
        'sodas': sodas,
        'breadsticks': breadsticks
    }
    return render(request, 'offers/twoforone.html', context)

@login_required
def add_to_cart(request):
    print('in add_to_cart')
    if request.method == 'POST':
        print('in POST')
        product_type = request.POST['product_type']
        print(f'product_type: {product_type}')
        if product_type == 'Special_offer':
            print('in SpecialOffer')
            pizzaID = request.POST['pizza_id']
            sodaID = request.POST['soda_id']
            breadsticksID = request.POST['breadstick_id']
            pizzas = get_object_or_404(Pizza, pk=pizzaID)
            soda = get_object_or_404(Sodas, pk=sodaID)
            breadsticks = get_object_or_404(Breadsticks, pk=breadsticksID)
            offer = SpecialOffer.objects.create(pizzas=pizzas, soda=soda, breadsticks=breadsticks)
            offer.save()
            cart = Cart.objects.get(user=request.user)
            cart_item = CartItem.objects.create(product_type=product_type, special_offer=offer, cart=cart, quantity=1)
            cart_item.save()
            messages.success(request, 'Item added to cart')
            print('Item added to cart')
            return render(request, 'cart/cart.html')
        if product_type == 'Lunch_Offer':
            print('in LunchOffer')
            pizzaID = request.POST['pizza_id']
            sodaID = request.POST['soda_id']
            pizzas = get_object_or_404(Pizza, pk=pizzaID)
            soda = get_object_or_404(Sodas, pk=sodaID)
            offer = LunchOffer.objects.create(pizzas=pizzas, soda=soda)
            offer.save()
            cart = Cart.objects.get(user=request.user)
            cart_item = CartItem.objects.create(product_type=product_type, lunch_offer=offer, cart=cart, quantity=1)
            cart_item.save()
            messages.success(request, 'Item added to cart')
            print('Item added to cart')
            return render(request, 'cart/cart.html')
        if product_type == 'Twoforone_offer':
            print('in TwoForOne')
            pizzaid1 = request.POST['pizza1_id']
            pizzaid2 = request.POST['pizza2_id']
            sodaID = request.POST['soda_id']
            pizzaid1 = get_object_or_404(Pizza, pk=pizzaid1)
            pizzaid2 = get_object_or_404(Pizza, pk=pizzaid2)
            sodaID = get_object_or_404(Sodas, pk=sodaID)
            offer = TwoForOne.objects.create(pizza1=pizzaid1, pizza2=pizzaid2, soda=sodaID)
            offer.save()
            cart = Cart.objects.get(user=request.user)
            cart_item = CartItem.objects.create(product_type=product_type, two_for_one=offer, cart=cart, quantity=1)
            cart_item.save()
            messages.success(request, 'Item added to cart')
            print('Item added to cart')
            return render(request, 'cart/cart.html')
    return render(request, 'cart/cart.html')
    
def delete_cart_item(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart-page')

