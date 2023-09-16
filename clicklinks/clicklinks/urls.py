from django.contrib import admin
from django.urls import path, include

from users.views import login, register
from main.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('<slug:username>/', include('links.urls')),
]
