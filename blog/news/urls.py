from django.urls import path
from . import views
from .views import PostListView


urlpatterns = [
    # path('',views.home, name='news-home'),
    path('',views.PostListView.as_view(), name='news-home'),
    path('about/',views.about, name='news-about'),
    path('contact/',views.contact, name='news-contact')
]