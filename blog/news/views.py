from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('<h1> Hello there news app</h1>')

def home(request):
    return render(request,template_name="news/home.html")

def about(request):
    return render(request,template_name="news/about.jinja")

def contact(request):
    return HttpResponse('<h1>Contact here</h1>')