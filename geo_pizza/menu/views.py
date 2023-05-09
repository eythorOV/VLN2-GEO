from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Pizza, Toppings

def get_pizza_by_id(request, id):
    return render(request, 'menu/pizza.html', {
        'pizza': get_pizza_by_id(Pizza, pk=id)
    })

def index(request):
    context = { 'pizzas': Pizza.objects.all().order_by('name') }
    return render(request, 'menu/index.html', context)

def pizza_desc(request):
    return render(request, 'menu/pizza_desc.html', {'title': 'Pizza Description'})