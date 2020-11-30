from django.shortcuts import render
from . import forms


def form_page(request):
    form = forms.NameForm()

    if request.method == "POST":  # Если были переданны данные в форму
        form = forms.NameForm(request.POST)  # form принимает данные из формы
        if form.is_valid():  # Если форма валидна
            print('Validation successs')
            # Свойство "cleaned_data" словарь, ключи имена полей (name, email, text)
            # Значения ключей - введённые данные
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request, 'validformapp/form_page.html', {'form': form})
