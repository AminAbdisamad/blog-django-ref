from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileImageUpdate,UserUpdateForm


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
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileImageUpdate(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, f'User information updated successfully')
            return redirect('news-home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileImageUpdate(instance=request.user.profile)
    context = {
        'user_form':user_form,
        'profile_form':profile_form
    }

    return render(request,'users/profile.jinja',context)