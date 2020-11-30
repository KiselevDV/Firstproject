from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^formpage/', views.form_page, name='form-page'),
]
