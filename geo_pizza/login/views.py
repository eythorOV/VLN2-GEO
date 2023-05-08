from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render(request, 'login/login.html', {'title': 'Login'})

def sign_up(request):
    return render(request, 'login/sign_up.html', {'title': 'Sign Up'})