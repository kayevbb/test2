from pyexpat.errors import messages
from django import http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from .forms import ProfileForm
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from .models import Post


class BlogListView(ListView):
    template_name = 'home.html'

    def get_queryset(self):
        return Post.objects.exclude(status=False)



class NewPostView(CreateView):
    model = Post
    template_name = 'new_post.html'
    form_class = ProfileForm
    success_url = reverse_lazy('home')

    # def form_valid(self, form):
    #     form.instance.user = self.request.user

    def get_queryset(self):
        return Post.objects.exclude(status=False)



class ProfileView(TemplateView):
    template_name = "blog.html"

