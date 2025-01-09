import requests
import re
from .models import ParcedData


def get_ids():
    url = "https://api.hh.ru/vacancies"
    payload = {'period': '1', 'order_by': 'publication_time',
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
                                  salary=data["salary"], area_city=data["area"]["name"],
                                  published_at=data["published_at"], currency=data["currency"])


def formate_data(data):
    data["description"] = re.sub(r'<[^>]+>', "", data["description"])
    data["key_skills"] = formate_field_skills(data["key_skills"])
    formate_salary(data)
    data["published_at"] = data["published_at"][:10]
    return data


def formate_salary(data):
    if data["salary"] is None:
        data["currency"] = None
    elif data["salary"]["from"] is None:
        data["currency"] = data["salary"]["currency"]
        data["salary"] = data["salary"]["to"]
    elif data["salary"]["to"] is None:
        data["currency"] = data["salary"]["currency"]
        data["salary"] = data["salary"]["from"]
    else:
        data["currency"] = data["salary"]["currency"]
        data["salary"] = (data["salary"]["from"] + data["salary"]["to"]) // 2


def formate_field_skills(skills):
    return ', '.join([skill["name"] for skill in skills])


# with open('/Users/yurazhilin/Desktop/testingDjango/mysite/static/index/full_info_proffesion.json') as file:
#     data = json.load(file)
#     print(formate_field_skills(data["vacancies"][1]["key_skills"]))

def update_parsed_data():
    id_lists = get_ids()
    info_ids_vac(id_lists)


if __name__ == "__main__":
    update_parsed_data()
