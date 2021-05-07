from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

# def home(request):
#     return HttpResponse('<h1> Hello there news app</h1>')


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,"news/home.jinja",context)

def about(request):
    return render(request,template_name="news/about.jinja")

def contact(request):
    return HttpResponse('<h1>Contact here</h1>')