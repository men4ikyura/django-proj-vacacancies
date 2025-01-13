import requests
import re
from .models import ParcedData
import datetime


def get_ids():
    url = "https://api.hh.ru/vacancies"
    payload = {'order_by': 'publication_time',
               'search_field': 'name', 'text': 'системный администратор', 'per_page': '10'}
    response = requests.get(url=url, params=payload)
    data = response.json()
    list_ids = [vacancy["id"] for vacancy in data["items"]]
    return list_ids


def info_ids_vac(list_ids):
    ParcedData.objects.all().delete()
    for id in list_ids:
        response = requests.get(f"https://api.hh.ru/vacancies/{id}")
        data = response.json()
        formate_data(data)
        ParcedData.objects.create(name=data["name"], description=data["description"],
                                  key_skills=data["key_skills"], employer_name=data["employer"]["name"],
                                  salary_cur=data["salary_cur"], area_city=data["area"]["name"],
                                  published_at=data["published_at"])


def formate_data(data):
    data["description"] = re.sub(
        r'<[^>]+>', " ", data["description"].replace("&quot;", ""))
    data["key_skills"] = formate_field_skills(data["key_skills"])
    formate_salary(data)
    data["published_at"] = datetime.datetime.strptime(
        data["published_at"], "%Y-%m-%dT%H:%M:%S%z")
    if data["salary_cur"] is None:
        data["salary_cur"] = "Нет информации"
    if data["key_skills"] == "":
        data["key_skills"] = "Нет информации"
    if data["description"] == "":
        data["description"] = "Нет информации"
    if data["employer"]["name"] == "":
        data["employer"]["name"] = "Нет информации"
    if data["area"]["name"] == "":
        data["area"]["name"] = "Нет информации"
    if data["published_at"] == "":
        data["published_at"] = "Нет информации"

    return data


def formate_salary(data):
    if data["salary"] is None:
        data["salary_cur"] = None
    elif data["salary"]["from"] is None:
        data["salary_cur"] = f"{data["salary"]["to"]} {data["salary"]
                                                       ["currency"]}"
    elif data["salary"]["to"] is None:
        data["salary_cur"] = f"{data["salary"]["from"]} {data["salary"]
                                                         ["currency"]}"
    else:
        data["salary_cur"] = f"{(data["salary"]["from"] + data["salary"]["to"]) // 2} {data["salary"]
                                                                                       ["currency"]} "


def formate_field_skills(skills):
    return ', '.join([skill["name"] for skill in skills])


def update_parsed_data():
    id_lists = get_ids()
    info_ids_vac(id_lists)


if __name__ == "__main__":
    update_parsed_data()
