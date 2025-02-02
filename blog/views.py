from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = '/blog/blog_list.html'
    context_object_name = 'blogs'


    def get_queryset(self):
        return Blog.objects.filter(is_publication=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_publication']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:list_blog')


class BlogDetailView(DetailView):
    model = Blog


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_publication']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:list_blog')

    def get_success_url(self):
        return reverse_lazy('blog:detail_blog', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:list_blog')
