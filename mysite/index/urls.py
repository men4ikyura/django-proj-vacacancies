from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("general/", views.general, name="general"),
    path("demand/",  views.demand, name="demand"),
    path("geo/",  views.geo, name="geo"),
    path("skills/",  views.skills, name="skills"),
    path("last-vacancies/", views.last_vacancies, name="last-vacancies")
]
