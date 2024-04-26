from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('users.urls'), name='users'),
    path('admin/', admin.site.urls),
]
