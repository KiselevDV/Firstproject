from django.conf.urls import url
from firstapp import views

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^(?P<pizza_id>\d+)', views.pizza_detail, name='pizza_detail'),
]
