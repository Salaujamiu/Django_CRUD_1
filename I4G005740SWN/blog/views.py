from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import post

# Create your views here.

class PostListView(generic.ListView):
    model = post

class PostCreateView(generic.CreateView):
    model = post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(generic.DetailView):
    model = post

class PostUpdateView(generic.UpdateView):
    model = post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(generic.DeleteView):
    model = post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")