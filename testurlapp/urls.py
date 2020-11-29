from django.conf.urls import url
from testurlapp import views

urlpatterns = [
    # # site.com/user/12
    # url(r'^user/(\d+)/$', views.home, name='index'),
    # # site.com/user/12/2000
    # url(r'^user/(\d{2})/(\d{4})/$', views.home, name='index')
    # Передаются в views уже в виде именнованых аргументов
    # url(r'^user/(?<month>\d{2})/(?<year>\d{4})/$', views.home, name='index')
]
