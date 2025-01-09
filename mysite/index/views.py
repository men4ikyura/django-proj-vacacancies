from django.shortcuts import render
from .models import ImgsAnalytics, ParcedData


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
    # path_file = os.path.join(settings.BASE_DIR, 'static',
    #                          'index/full_info_proffesion.json')

    # with open(path_file) as file:
    #     data = json.load(file)
    # main()
    # return render(request, 'index/last_vacancies.html', {'data': data["vacancies"]})
    # update_parsed_data()
    data = ParcedData.objects.all()
    return render(request, 'index/last_vacancies.html', {"data": data})
