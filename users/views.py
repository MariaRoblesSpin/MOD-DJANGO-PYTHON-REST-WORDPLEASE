from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout

from users.forms import LoginForm


def login(request):
    # Si el usuario está autenticado pasa direstamente a su página de posts
    if request.user.is_authenticated:
        return redirect('home')
    # Si el usuario no está autenticado
    if request.method == 'POST':          # Cuando se pulsa el botón de login
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)

            if user is None:
                messages.error(request, 'Usuario/contraseña incorrectos')
            else:
                django_login(request, user)
                return redirect('home')
    else:
        form = LoginForm()               # Cuando se accede por primera vez desde url /login
    context = {'form': form}
    return render(request, 'users/login.html', context)


def logout(request):
    django_logout(request)
    return redirect('login')
