from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
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

# def home(request): 
#     context = {
#         'posts':Post.objects.all()
#     }
#     return render(request,"news/home.jinja",context)

def about(request):
    return render(request,template_name="news/about.jinja")

def contact(request):
    return HttpResponse('<h1>Contact here</h1>')