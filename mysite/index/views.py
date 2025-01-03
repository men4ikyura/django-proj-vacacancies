from django.shortcuts import render
from .models import ImgsAnalytics


def index(request):
    return render(request, 'index/index.html')


def general(request):
    data = ImgsAnalytics.objects.filter(title="Общая статистика")
    return render(request, 'index/general.html', {'data': data})


def demand(request):
    data = ImgsAnalytics.objects.filter(title="Фильтрованная статистика")
    return render(request, 'index/demand.html', {'data': data})


def geo(request):
    return render(request, 'index/geo.html')


def skills(request):
    return render(request, 'index/skills.html')


def last_vacancies(request):
    return render(request, 'index/last_vacancies.html')
