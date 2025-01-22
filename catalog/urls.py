from django.urls import path, include
from catalog.apps import CatalogConfig

from catalog.views import home
from catalog.views import contacts
from catalog.views import product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product/', product)
]
