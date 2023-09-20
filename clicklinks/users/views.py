from django.shortcuts import redirect, render
from django.contrib import auth
from .forms import UserLoginForm, UserRegistrationForm


def login(request):
    template = 'users/login.html'
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect(f'/{username}/')
    else:
        form = UserLoginForm()

    context = {
        'form': form,
    }
    return render(request, template, context)


def register(request):
    template = 'users/registration.html'
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, template, context)
