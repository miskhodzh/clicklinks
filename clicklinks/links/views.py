from django.shortcuts import render


def links(request, username):
    template = 'links/main-template.html'
    context = {
        'username': username,
    }
    return render(request, template, context)
