from django.contrib.auth.decorators import login_required  # авторизован ли пользователь
from django.shortcuts import render, redirect


# redirect - ф-ия перенаправления на страницу "authapp_home"
def home(request):
    return redirect(authapp_home)


# login_required - проверяет выполнил ли посетитель вход на сайт и только потом разрешает
# вход, если нет, перенаправляет на страницу входа (login_url='/authapp/login')
@login_required(login_url='/authapp/login')
def authapp_home(request):
    return render(request, 'authapp/home.html', {})
