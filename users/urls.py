from tempfile import template

from django.urls import path
from .views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),
    path('login/',LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:product_list'), name='logout'),
    ]