from django.shortcuts import render

def profile(request):
    template = 'profile.html'

    return render(request, template)
