from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg ='post_slug'
    context_object_name = 'post'