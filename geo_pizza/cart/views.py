from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'cart/cart.html')

def contact_info(request):
    return render(request, 'cart/contact.html', {'title': 'Checkout - Contact Info'})

def payment_info(request):
    return render(request, 'cart/payment.html', {'title': 'Checkout - Payment Info'})

def review_page(request):
    return render(request, 'cart/review.html', {'title': 'Checkout - Review'})

def complete(request):
    return render(request, 'cart/complete.html', {'title': 'Checkout - Complete'})

