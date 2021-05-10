from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from .models import Post



class PostListView(ListView):
    # Where to get list of view
    model = Post
    # if not set context_object variable is available in template
    context_object_name = 'posts'
    # by default it looks for <app>/<model_list>.<extention> ex. news/post_list.html
    template_name ="news/home.jinja"
    ordering = '-date_posted'
    paginate_by = '4'


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


class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name ="news/user_post_list.jinja"
    paginate_by = '4'

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by("-date_posted")

def about(request):
    return render(request,template_name="news/about.jinja")

def contact(request):
    # Testing with git reset
    return HttpResponse('<h1>Contact here</h1>')