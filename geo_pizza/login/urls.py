from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', views.signup, name='login-sign_up'),
    path('login/', LoginView.as_view(template_name='login/login.html'), name='login-page'),
    path('logout/', LogoutView.as_view(next_page='login-page'), name='login-logout'),
    path('profile/', views.profile, name='login-profile'),
]