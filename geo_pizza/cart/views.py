from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from cart.models import CartItem, Cart
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'cart/cart.html')

def get_cart(request):
    cart = Cart.objects.get(user=request.user)
    cart.calculate_total_price()
    cart_items = cart.cart_items.all()
    context = { 'cart_items': cart_items, 'cart': cart}
    return render(request, 'cart/cart.html', context)

def delete_cart_item(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect('cart-page')

def delete_all_cart_items(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cart_items.all()
    cart_items.delete()
    cart.total_price = 0
    cart.save()
    return redirect('cart-page')

@csrf_exempt
def update_cart_item_quantity(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        quantity = request.POST.get('quantity')
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.quantity = quantity
        cart_item.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

def contact_info(request):
    return render(request, 'cart/contact.html', {'title': 'Checkout - Contact Info'})

def payment_info(request):
    return render(request, 'cart/payment.html', {'title': 'Checkout - Payment Info'})

def review_page(request):
    return render(request, 'cart/review.html', {'title': 'Checkout - Review'})

def complete(request):
    return render(request, 'cart/complete.html', {'title': 'Checkout - Complete'})

def add_to_cart(request, product_id):
    product_type = 'Pizza'
    cart_item = CartItem.objects.filter(product_type=product_type, id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, 'Item added to cart')
        print('Item added to cart')
    else:
        if product_type == 'Pizza' or product_type == 'pizza':
            print('Pizza')
            cart_item = CartItem(product_type=product_type, pizza_id=product_id)
        elif product_type == 'SpecialOffer':
            cart_item = CartItem(product_type=product_type, special_offer_id=product_id)
        elif product_type == 'LunchOffer':
            cart_item = CartItem(product_type=product_type, lunch_offer_id=product_id)
        elif product_type == 'TwoForOne':
            cart_item = CartItem(product_type=product_type, two_for_one_id=product_id)
        else:
            messages.error(request, 'Invalid product type')
            return render(request, 'cart/cart.html')
        cart_item.save()
        messages.success(request, 'Item added to cart')
    return render(request, 'cart/cart.html')

            