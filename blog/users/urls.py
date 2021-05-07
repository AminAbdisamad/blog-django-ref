from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('',views.auth, name='auth-login'),
    path('',auth_views.LoginView.as_view(template_name="users/auth.jinja"), name='auth-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.jinja"),name="auth-logout"),
    path('register/',views.register, name='auth-register'),
]