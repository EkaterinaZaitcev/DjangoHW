from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'blogs'


    def get_queryset(self):
        return Blog.objects.filter(publication_sing=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'image', 'count_of_views', 'publication_sing']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:home')


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'count_of_views', 'publication_sing']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:home')

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:home')
