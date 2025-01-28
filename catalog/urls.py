from django.urls import path, include
from catalog.apps import CatalogConfig

from catalog.views import home
from catalog.views import contacts
from catalog.views import product_list, products_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', products_detail, name='products_detail')
]
