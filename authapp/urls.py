from django.conf.urls import url
from django.contrib.auth import views as auth_views  # login/logout
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    # Единая система разграничения доступа для всего сайта
    # Привязываем ф-ию контороллер (auth_views.login) к адресу (r'^login/$')
    # Два необязательных параметра "template_name" - путь к файлу шаблона
    # extra-context - содержит данные, которые будут добавлены к контексту данных шаблона
    url(r'^authapp/login/$', auth_views.login,
        {'template_name': 'authapp/login.html'},
        name='authapp-login'),
    # Выход со страницы (logout) может содержать ещё один параметр
    # "next_page" - перенаправление на заданную страницу после выхода
    url(r'^authapp/logout/$', auth_views.logout,
        {'next_page': '/'},
        name='authapp-logout'),
    # URL страницы на которую перенаправит ф-ия "redirect"
    url(r'^authapp/$', views.authapp_home, name='authapp-home'),
]
