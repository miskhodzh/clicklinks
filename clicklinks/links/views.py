from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Links

User = get_user_model()


def links(request, username):
    template = 'links/main-template.html'
    user = get_object_or_404(User, username=username)
    links = Links.objects.filter(user_id=user)
    context = {
        'user': user,
        'links': links,
    }
    return render(request, template, context)
