from django.contrib.auth.decorators import login_required  # авторизован ли пользователь
from django.shortcuts import render, redirect
from .forms import UserForm, PizzaShopForm

# Для кастомного login/logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


# redirect - ф-ия перенаправления на страницу "authapp_home"
def home(request):
    return redirect(authapp_home)


# login_required - проверяет выполнил ли посетитель вход на сайт и только потом разрешает
# вход, если нет, перенаправляет на страницу входа (login_url='/authapp/login')
@login_required(login_url='/authapp/login')
def authapp_home(request):
    return render(request, 'authapp/home.html', {})


def authapp_sign_up(request):
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()

    """Для кастомного login/logout авторизации новых пользователей не суперпользователя - 
    добавления новых пользователей (владельце пиццерий)."""
    # Каждый контроллер для добавления/удаления вызывается дважды (при нажатии кнопки
    # отправить/сохранить). В первый раз передаются начальные данные которые должны быть в форме,
    # во второй раз данные введённые посетителем для их валидации и/или сохранения - они
    # передаются конструктору первым неименованным параметром в объекте "request". Однако
    # "request", не содержит выгруженные файлы. Их можно передать - "request.FILES"
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES)

        if user_form.is_valid() and pizzashop_form.is_valid():
            # Создаём и сохраняем нового пользователя, и привязывем его к пиццерии
            new_user = User.objects.create_user(**user_form.cleaned_data)
            # pizzashop_form с параметрами save(commit=False) вернёт объект, но который ешё не был
            # сохранён в БД и в него можно вносить правки
            new_pizzashop = pizzashop_form.save(commit=False)
            # отдаём в "new_pizzashop" метод "user" нового пользователя "new_user"
            new_pizzashop.user = new_user
            # После связывания user_form и pizzashop_form сохраняем
            new_pizzashop.save()

            # Переменная user из переменной user_form принимает 'username' и 'password' задающие
            # имя пользователя и его пароль и возращает объект класса User или None если
            # пользлвателя с такими данными нет
            user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password'],
            )

            # Функция login непосредственно выполнит процедуру входа
            # request - объект сведений о запросе, user -//- о пользователе
            login(request, user)

            # Далее нужно перенаправить пользовотеля либы выполнить выход
            return redirect(authapp_home)

    # Передаём формы в контекст для отображения в шаблоне
    return render(request, 'authapp/sign_up.html', {
        'user_form': user_form,
        'pizzashop_form': pizzashop_form,
    })
