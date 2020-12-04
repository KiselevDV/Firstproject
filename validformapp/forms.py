from django import forms
from django.core import validators


# Кастомный валидатор на проверку value - данные из формы, хранятся в request.POST
def check_for_a(value):
    # value вводимый текст должен начинаться с "N"
    if value[0].upper() != 'N':
        # Если (!= 'N') - вызов "raise" ошибки "ValidationError"
        raise forms.ValidationError(
            'value вводимый текст должен начинаться с "N"')  # Текст подсказка


class NameForm(forms.Form):  # Форма от встроеного класса Form
    name = forms.CharField(validators=[check_for_a])  # Кастомный валидатор выше
    email = forms.EmailField()
    # Повтор введённого email, "label" - название при отображении в HTML
    verify_email = forms.EmailField(label="Введите свой адрес электронной почты еще раз:")
    # forms.Textarea - простой виджет отображения в HTML
    # validators.MaxLengthValidator - встроенный валидатор количества введённых символов
    text = forms.CharField(widget=forms.Textarea,
                           validators=[validators.MaxLengthValidator(5)])

    # Реализация метода form.clean - преобразует введенное в форму данные к нужному типу
    # Заполняет преобразованными данными словарь form.cleaned_data и возвращает его
    def clean(self):
        # super() вызываем унаследованный от родителя "Form" метод "clean"
        cleaned_data = super().clean()  # Получаем словарь с уже преобразованными данными
        email = cleaned_data['email']  # Получаем данные из поля "email" в словаре cleaned_data
        vmail = cleaned_data['verify_email']  # Тоже для verify_email

        # Проверяем email на совпадение почты
        if email != vmail:
            raise forms.ValidationError(
                'Убедитесь, что адрес электронной почты совпадает, email != vmail')
        return cleaned_data
