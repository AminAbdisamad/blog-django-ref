from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, request
from django.urls import reverse_lazy
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
    
    # Adding search funcitonality 
    def get_queryset(self):
        search_input = self.request.GET.get('search-input') or None
        # search_input = self.kwargs.get('search-input', '')
        object_list = Post.objects.all()
        if search_input:
            object_list = object_list.filter(title__icontains=search_input)
        return object_list


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context  = super().get_context_data(**kwargs)
        search_input =  self.request.GET.get('search-input') or None
        context['search_input'] = search_input 
        return context
       
        
        # print('GET Method', self.request.GET.get('search-input') )
        # search_input = self.request.GET.get('search-input') or None
        # print(search_input)
        # if search_input:
        #     context['posts'] = context['posts'].filter(title__icontains=search_input)  
        return context


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

    # Users can only update their data
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class DeletePostView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'news/post_delete.jinja'
    # success_url = '/'
    success_url = reverse_lazy('news-home')
    
    # Users can only delete their posts
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

    # Get all data from a specific user 
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by("-date_posted")
    
    # #! Each user should get their own data
    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context =  super().get_context_data(**kwargs)
    #     return context['posts'].filter(author=self.request.user)

def about(request):
    return render(request,template_name="news/about.jinja")

def contact(request):
    # Testing with git reset
    return HttpResponse('<h1>Contact here</h1>')