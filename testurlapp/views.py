from django.shortcuts import render


def home(request, month, year):
    return render(request, 'testurlapp/index.html', {
        'month': month,
        'year': year,
    })
