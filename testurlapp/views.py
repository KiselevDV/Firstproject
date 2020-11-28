from django.shortcuts import render


def home(request, month, year):
    return render(request, 'home.html', {})
