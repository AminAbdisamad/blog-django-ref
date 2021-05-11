from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path('',views.auth, name='auth-login'),
    path('',auth_views.LoginView.as_view(template_name="users/auth.jinja"), name='auth-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.jinja"),name="auth-logout"),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name="users/password_reset.jinja"),name="password-reset"),
    path('reset-password-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name="password_reset_confirm"),
    path('reset-password/done/', auth_views.PasswordResetDoneView.as_view(template_name="users/password_reset_done.jinja"),name="password-reset-done"),
    path('register/',views.register, name='auth-register'),
]