from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Pizza, Toppings

# def get_pizza_by_id(request, id):
#     return render(request, 'menu/pizza_details.html', {
#         'pizza': Pizza.objects.get(pk=id)
#     })

def get_pizza_by_id(request, id):
    pizza = Pizza.objects.get(pk=id)
    toppings = pizza.toppings.all()
    context = {
        'pizza': pizza,
        'toppings': toppings,
    }
    return render(request, 'menu/pizza_details.html', context)

def get_toppings_by_id(request, id):
    return render(request, 'menu/toppings_details.html', {
        'toppings': Toppings.objects.get(pk=id)
    })

def index(request):
    context = { 'pizzas': Pizza.objects.all().order_by('name') }
    return render(request, 'menu/index.html', context)