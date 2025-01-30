from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path("product/<int:pk>", ProductDetailView.as_view(), name='product_detail'),
    path('', ProductListView.as_view(), name='product_list'),
]
