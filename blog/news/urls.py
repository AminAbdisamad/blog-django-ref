from django.urls import path
from . import views
from .views import PostListView,PostDetailView


urlpatterns = [
    # path('',views.home, name='news-home'),
    path('',views.PostListView.as_view(), name='news-home'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
    path('about/',views.about, name='news-about'),
    path('contact/',views.contact, name='news-contact')
]