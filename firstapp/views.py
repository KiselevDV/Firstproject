from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Pizza
from .forms import OrderForm


def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {'pizzas': pizzas})


def pizza_detail(request, pizza_id):
    # Вызов объекта пиццы или ошибка 404
    pizza = get_object_or_404(Pizza, id=pizza_id)
    # Загрузка базовой формы из forms.py
    # initial - параметр, для присвоения значений полю по умочанию
    # request.POST or None - передаём данные POST запросом если есть!
    form = OrderForm(request.POST or None, initial={'pizza': pizza, })

    # Добавление данных из формы в модель (БД)
    if request.method == 'POST':  # Если данные переданны методом POST
        if form.is_valid():  # Если форма валидна
            form.save()  # Сохраняем форму в модель БД
            # Очистка формы от данных
            # HttpResponseRedirect - отвечает за перенапраление
            # После сохранения формы в БД пользователя перенаправят на другую страницу
            # reverse - отвечает за адрес страницы: первый аргумент (pizza_detail) - адрес страницы
            # второй словарь с данными для "r'^(?P<pizza_id>\d+)'" и посьроения url
            return HttpResponseRedirect(
                '{}?sent=True'.format(reverse('pizza_detail', kwargs={'pizza_id': pizza.id})))
        # При ссылке на туже страницу HttpResponseRedirect её просто перезагрузит
        # '{}?sent=True'.format - меняет значение переменной sent на True,
        # тогда шаблон (pizza_detail) выводит сообщение о том что заявка принята

    return render(request, 'pizza_detail.html', {
        'pizza_detail': pizza,
        'form': form,
        'sent': request.GET.get('sent', False)  # Передаёт sent с значением False
    })
