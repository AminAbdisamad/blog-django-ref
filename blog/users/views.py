from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileImageUpdate,UserUpdateForm

# IF YOU ARE USING CLASS_BASED VIEWS USE THIS REGISTRATION PAGE
class UserRegister(CreateView):
    template_name = 'register.html'
    from_class = UserCreationForm
    success_url = '/'
    def form_valid(self, form):
        user_form = form.save()
        if user_form:
            # login user or redirect to login
            login(self.request,user_form)
        return super().form_valid(form)
    
    def get(self, request, *args: str, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('news-home')
        return super().get(request, *args, **kwargs)

# OR THIS FUNCTION BASED REGISTER 
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
        if request.user.is_authenticated:
            return redirect('news-home')
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