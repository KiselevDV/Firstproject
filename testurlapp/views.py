from django.shortcuts import render


def home(request, month, year):
    return render(request, 'testurlapp/index.html', {
        'request': request,
        'month': month,
        'year': year,
    })
