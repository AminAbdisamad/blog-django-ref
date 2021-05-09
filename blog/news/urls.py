from django.urls import path
from . import views



urlpatterns = [
    # path('',views.home, name='news-home'),
    path('',views.PostListView.as_view(), name='news-home'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name='post-detail'),
    path('post/add/',views.CreatePostView.as_view(), name='post-create'),
    path('post/<int:pk>/update',views.UpdatePostView.as_view(), name='post-update'),
    path('post/<int:pk>/delete',views.DeletePostView.as_view(), name='post-delete'),
    path('about/',views.about, name='news-about'),
    path('contact/',views.contact, name='news-contact')
]