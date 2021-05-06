from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='news-home'),
    path('about/',views.about, name='news-about'),
    path('contact/',views.contact, name='news-contact')
]