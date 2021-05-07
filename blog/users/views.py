from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def auth(request):
    return render(request,'users/auth.jinja')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'User with username {username} created successfully')
            return redirect('news-home')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.jinja',{'form':form})
