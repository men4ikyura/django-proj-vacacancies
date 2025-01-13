from django.shortcuts import render
from .models import GeneralSkillsAnalytics, FiltredSkillsAnalytics, GeneralAnalytics, FiltredAnalytics


def index(request):
    return render(request, "index/index.html")


def general(request):
    not_skills = GeneralAnalytics.objects.all()
    skills = GeneralSkillsAnalytics.objects.all()
    return render(request, "index/general.html", {"data": {"not_skills": not_skills, "skills": skills}})


def demand(request):
    data = FiltredAnalytics.objects.filter(id_page="DMN")
    return render(request, "index/demand.html", {"data": data})


def geo(request):
    data = FiltredAnalytics.objects.filter(id_page="GEO")
    return render(request, "index/geo.html", {"data": data})


def skills(request):
    data = FiltredSkillsAnalytics.objects.all()
    return render(request, "index/skills.html", {"data": data})


def last_vacancies(request):
    return render(request, "index/last_vacancies.html")
