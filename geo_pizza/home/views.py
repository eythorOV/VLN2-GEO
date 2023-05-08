from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def order(request):
    return render(request, 'home/order.html', {'title': 'Order Now'})

def about_us(request):
    return render(request, 'home/about_us.html', {'title': 'About Us'})
