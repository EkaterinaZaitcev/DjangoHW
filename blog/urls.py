from django.urls import path
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('home/', BlogListView.as_view(), name='home'),
    path('home/<int:pk>/', BlogDetailView.as_view(), name='detail_blog'),
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('home/<int:pk>/update/', BlogUpdateView.as_view(), name='update_blog'),
    path('home/<int:pk>/delete/', BlogDeleteView.as_view(), name='delete_blog')
]
