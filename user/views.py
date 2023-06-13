from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm


def index(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление после успешного входа в систему
            else:
                form.add_error(None, 'Неправильное имя пользователя или пароль')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление после успешной регистрации
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


