from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from cart.models import CartItem, Cart, ContactInfo, PaymentInfo
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'cart/cart.html')

@login_required
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
    already_user = ContactInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        already_user = ContactInfo.objects.filter(user=request.user).first()
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        street = request.POST['street']
        housenumber = request.POST['housenumber']
        city = request.POST['city']
        country = request.POST['country']
        postalcode = request.POST['postalcode']
        user = request.user
        if not already_user:
            contact_info = ContactInfo.objects.create(firstname=firstname, lastname=lastname, street=street, housenumber=housenumber, city=city, country=country, postalcode=postalcode, user=user)
        else:
            already_user.firstname = firstname
            already_user.lastname = lastname
            already_user.street = street
            already_user.housenumber = housenumber
            already_user.city = city
            already_user.country = country
            already_user.postalcode = postalcode
            already_user.save()
        return redirect('/checkout/payment/')
    return render(request, 'cart/contact.html', {'already_user': already_user, 'title': 'Checkout - Contact Info'})

def payment_info(request):
    already_user = PaymentInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        card_holder_name = request.POST['name']
        card_number = request.POST['cardnumber']
        expiration_date = request.POST['expirationdate']
        cvv = request.POST['cvc']
        user = request.user
        if not already_user:
            payment_info = PaymentInfo.objects.create(card_holder_name=card_holder_name, card_number=card_number, expiration_date=expiration_date, cvv=cvv, user=user)
        else:
            already_user.card_holder_name = card_holder_name
            already_user.card_number = card_number
            already_user.expiration_date = expiration_date
            already_user.cvv = cvv
            already_user.save()
        return redirect('checkout-review-info')
    return render(request, 'cart/payment.html', {'already_user': already_user,'title': 'Checkout - Contact Info'})


def review_page(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cart_items.all()
    cart.calculate_total_price()
    context = { 'contactinfo': ContactInfo.objects.get(user=request.user), 'paymentinfo': PaymentInfo.objects.get(user=request.user), 'cart' : cart, 'cart_items': cart_items,'title': 'Checkout - Review Info'}
    if request.method == 'POST':
        return redirect('checkout-complete')
    return render(request, 'cart/review.html', context)

def complete(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.cart_items.all()
    cart_items.delete()
    cart.total_price = 0
    cart.save()
    contact_info = ContactInfo.objects.get(user=request.user)
    contact_info.delete()
    payment_info = PaymentInfo.objects.get(user=request.user)
    payment_info.delete()
    return render(request, 'cart/complete.html', {'title': 'Checkout - Complete'})

@login_required
def add_to_cart(request, product_id):
    product_type = 'Pizza'
    cart_item = CartItem.objects.filter(product_type=product_type, id=product_id).first()
    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, 'Item added to cart')
    else:
        if product_type == 'Pizza' or product_type == 'pizza':
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

            