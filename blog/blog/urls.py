from django.contrib import admin
from django.urls import path,include
# Add these two imports to work with static files
from django.conf.urls.static import static
from django.conf import settings
from users.views import profile

urlpatterns = [
    path('',include('news.urls')),
    path('admin/', admin.site.urls),
    path('auth/',include('users.urls')),
    path('profile/',profile, name="profile")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
