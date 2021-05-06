from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('<h1> Hello there news app</h1>')

posts = [
    {
        'author':'Amin',
        'title':'post one',
        'content':'post content one',
        'date':'12 May 2021'
    },
    {
        'author':'Hassan',
        'title':'post Two',
        'content':'post content Two',
        'date':'11 May 2021'
    },
    {
        'author':'Abdi',
        'title':'post Three',
        'content':'post content Three',
        'date':'1 May 2021'
    }
]
def home(request):
    context = {
        'posts':posts
    }
    return render(request,"news/home.html",context)

def about(request):
    return render(request,template_name="news/about.jinja")

def contact(request):
    return HttpResponse('<h1>Contact here</h1>')