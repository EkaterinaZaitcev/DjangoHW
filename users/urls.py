from tempfile import template

from django.urls import path
from .views import RegistrationView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/',LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:base'), name='logout'),
    ]