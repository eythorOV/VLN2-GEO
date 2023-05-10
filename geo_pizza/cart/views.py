from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    return render(request, 'cart/contact.html', {'title': 'Checkout - Contact Info'})