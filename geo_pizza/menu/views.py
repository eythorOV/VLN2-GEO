from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'menu/index.html', {'title': 'Menu'})

def pizza_desc(request):
    return render(request, 'menu/pizza_desc.html', {'title': 'Pizza Description'})