from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login as django_login, logout as django_logout
from django.views import View

from users.forms import LoginForm, SignUpForm


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


class SignUpFormView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'users/signup.html', context)

    def post(self, request):
        form = SignUpForm(self.request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = self.request.POST.get('first_name')
            new_user.set_password(self.request.POST.get('password'))
            new_user.save()
            messages.success(request, 'User registered sucessfully')
            return redirect('home')
        else:
            messages.error(request, 'Usuario no registrado')
        context = {'form': form}
        return render(request, 'users/signup.html', context)


