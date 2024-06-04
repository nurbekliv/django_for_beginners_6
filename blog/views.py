from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog_home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog_post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_post_delete.html'
    success_url = reverse_lazy('blog_list')
