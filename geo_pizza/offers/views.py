from django.shortcuts import render

# Create your views here.
def offer_list(request):
    return render(request, 'offers/offer_list.html')