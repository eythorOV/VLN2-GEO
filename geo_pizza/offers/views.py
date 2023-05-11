from django.shortcuts import render
from django.http import HttpResponse
from .models import SpecialOffer, LunchOffer, TwoForOne, Sodas, Breadsticks
from menu.models import Pizza

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

from django.shortcuts import render
from .models import SpecialOffer, LunchOffer, TwoForOne, Pizza, Sodas

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


