from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.



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

@login_required
def profile(request):
    return render(request,'users/profile.jinja')