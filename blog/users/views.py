from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def auth(request):
    return render(request,'users/auth.html')

def register(request):
    if request.method == 'POST':
        print('I am Post request')
        form = UserCreationForm(request.POST)
      
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'User with username {username} created successfully')
            return redirect('news-home')
    else:
        print('Iam get request')
        form = UserCreationForm()
    return render(request,'users/register.html',{'form':form})
