# User - для хранения данных о зарегистрированных пользователях
from django.contrib.auth.models import User
from django.db import models


class PizzaShop(models.Model):
    name = models.CharField(verbose_name='Название пиццерии', max_length=30)
    logo = models.ImageField(upload_to='authapp/pizzashop_logo/', blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='pizzashop')

    def __str__(self):
        return self.name
