from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Pizza, Toppings

def get_pizza_by_id(request, id):
    pizza = Pizza.objects.get(pk=id)
    toppings = pizza.toppings.all()
    context = {
        'pizza': pizza,
        'toppings': toppings,
    }
    return render(request, 'menu/pizza_desc.html', context)

def index(request):
    context = { 'pizzas': Pizza.objects.all().order_by('name') }
    return render(request, 'menu/index.html', context)

# def pizza_desc(request):
#     return render(request, 'menu/pizza_desc.html', {'title': 'Pizza Description'})