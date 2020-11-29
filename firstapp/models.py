from django.db import models


class PizzaShop(models.Model):
    """Модель пиццерии"""
    name = models.CharField(verbose_name='Пиццерия', max_length=30)
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(verbose_name='Рейтинг', default=0)
    url = models.URLField(verbose_name='Интернет-адрес пиццерии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пиццеррия'
        verbose_name_plural = 'Пиццерии'


class Pizza(models.Model):
    """Меню пицц"""
    name = models.CharField(verbose_name='Название пиццы', max_length=30)
    description = models.CharField(verbose_name='Краткое описвние', max_length=50)
    photo = models.ImageField(
        verbose_name='Фото', upload_to='firstapp/photos', default='', blank=True)
    price = models.IntegerField(verbose_name='Цена', default=0)
    pizzashop = models.ForeignKey(PizzaShop, verbose_name='Пиццерия', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
        ordering = ['name', ]


class Order(models.Model):
    """Заказ пиццы"""
    pizza = models.ForeignKey(Pizza, verbose_name='Пицца')
    name = models.CharField(verbose_name='Имя заказчика', max_length=30)
    phone = models.CharField(verbose_name='Телефон', max_length=30)
    data = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказ пиццы'
        verbose_name_plural = 'Заказы пицц'
