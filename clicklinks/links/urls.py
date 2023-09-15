from django.urls import path

from . import views

urlpatterns = [
    path('<slug:username>/', views.links, name='links'),
]
