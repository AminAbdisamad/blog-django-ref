from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Post
# Create your views here.

# def home(request):
#     return HttpResponse('<h1> Hello there news app</h1>')

class PostListView(ListView):
    # Where to get list of view
    model = Post
    # if not set context_object variable is available in template
    context_object_name = 'posts'
    # by default it looks for <app>/<model_list>.<extention> ex. news/post_list.html
    template_name ="news/home.jinja"
    ordering = '-date_posted'


class PostDetailView(DetailView):
    model = Post
    template_name ="news/post_detail.jinja"

class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'news/post_create.jinja'
    

    def form_valid(self, form:BaseModelForm)->HttpResponse:
        print(self.request.user)
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']
    template_name = 'news/post_update.jinja'

    def form_valid(self, form:BaseModelForm)->HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class DeletePostView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'news/post_delete.jinja'
    success_url = '/'
    

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(request):
    return render(request,template_name="news/about.jinja")

def contact(request):
    return HttpResponse('<h1>Contact here</h1>')