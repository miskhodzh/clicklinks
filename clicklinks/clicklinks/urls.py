from django.contrib import admin
from django.urls import path, include

from users.views import login, register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('', include('links.urls')),
]
