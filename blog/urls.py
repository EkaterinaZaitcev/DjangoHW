from django.urls import path, include
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

from catalog.views import home
from catalog.views import contacts
from catalog.views import product_list, products_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('home/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('home/', BlogListView.as_view(), name='home'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('home/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('home/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete')
]
