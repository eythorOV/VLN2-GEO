from django.shortcuts import render
from django.http import HttpResponse
from .models import SpecialOffer, LunchOffer, TwoForOne, Sodas, Breadsticks


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

def special(request):
    specialoffer = SpecialOffer.objects.first()  # Retrieve the special offer object
    context = {
        'title': 'Offer - Special',
        'specialoffer': specialoffer
    }
    return render(request, 'offers/special.html', context)

def lunch(request):
    lunchoffer = LunchOffer.objects.first()  # Retrieve the lunch offer object
    context = {
        'title': 'Offer - Lunch',
        'lunchoffer': lunchoffer
    }
    return render(request, 'offers/lunch.html', context)

def twoforone(request):
    twoforone = TwoForOne.objects.first()  # Retrieve the two-for-one offer object
    context = {
        'title': 'Offer - Two For One',
        'twoforone': twoforone
    }
    return render(request, 'offers/twoforone.html', context)
