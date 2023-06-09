from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from cart.models import Cart
from django.contrib import messages
from login.models import Profile
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = 'email'
        if not (first_name and last_name and username and password1 and password2 and email):
            messages.warning(request, 'Please fill in all required fields.')
            return redirect('sign_up')

        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username already exists')
            return redirect('sign_up')
        
        if password1 != password2:
            messages.warning(request, 'Passwords do not match')
            return redirect('sign_up')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        user_login = auth.authenticate(username=username, password=password1)
        if user_login is not None:
            auth.login(request, user_login)
            cart = Cart.objects.create(user=user)
            cart.save()
            profile = Profile.objects.create(user=user, first_name=first_name, last_name = last_name, profile_picture ='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png')
            return redirect('home-index')
    return render(request, 'login/sign_up.html')

def login(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home-index')
    return render(request, 'home-index.html')

@login_required(login_url='login-page')
def profile(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        profile_picture = request.POST['profile_picture']
        if first_name == "":
            first_name = request.user.first_name
        if last_name == "":
            last_name = request.user.last_name
        if profile_picture == "":
            profile_picture = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png'
        profile = Profile.objects.get(user=request.user)
        profile.first_name = first_name
        profile.last_name = last_name
        profile.profile_picture = profile_picture
        profile.save()
        return redirect('home-index')
    return render(request, 'login/profile.html')


def get_all_users(request):
    users = User.objects.all()
    return render(request, 'login/all_users.html', {'users': users})

def get_user_by_id(request, id):
    user = User.objects.get(pk=id)
    return render(request, 'login/user.html', {'user': user})