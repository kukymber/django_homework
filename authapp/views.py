from datetime import datetime

from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                print("Пользователь неактивный")
        else:
            print(form.errors)
    else:
        form = UserLoginForm()

    content = {
        'title': 'Geekshop | Авторизация',
        'form': form
    }
    return render(request, 'authapp/login.html', context=content)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse('authapp:login'))

        else:
            print(form.errors)
    else:
        form = UserRegisterForm()

    content = {
        'title': 'Geekshop | Регистрация',
        'form': form
    }
    return render(request, 'authapp/register.html', context=content)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    content = {
        'title': "Geekshop | Профайл",
        'form': UserProfileForm(instance=request.user)
    }
    return render(request, 'authapp/profile.html', context=content)


def logout(request):
    auth.logout(request)
    data_time = {'data_time_now': datetime.now().strftime("%d-%m-%Y %H:%M")}
    content = {
        'name_of_shop': 'GeekShop Store',
        'text': 'Новые образы и лучшие бренды на GeekShop Store.'
                'Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'button_name': 'Начать покупки',
        'data_time': data_time
    }

    return render(request, 'mainapp/index.html', context=content)
