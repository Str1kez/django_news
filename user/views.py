from django.contrib import messages
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from .forms import CreateUserForm, AuthUserForm


def sign_up(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Вы вошли как {user}')
            return redirect('blog:home')
        else:
            messages.error(request, f'Ошибка в регистрации {form.errors}')
    form = CreateUserForm()
    return render(request, 'user/sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Вы вошли как {user}')
            return redirect('blog:home')
        else:
            messages.error(request, f'Ошибка в авторизации {form.errors}')
    form = AuthUserForm()
    return render(request, 'user/sign_in.html', {'form': form})


def log_out(request):
    logout(request)
    messages.success(request, 'Вы вышли из аккаунта')
    return redirect('blog:home')
