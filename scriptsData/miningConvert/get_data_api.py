import requests
import xml.etree.ElementTree as ET
import pandas as pd
from dotenv import load_dotenv
import os

# create csv with converting koef

load_dotenv()
name_main_csv = os.getenv('DATA_VACANCIES')


def fetch_cur_data(year, month, base_url):
    formatted_date = f"01/{month:02}/{year}"
    response = requests.get(f"{base_url}?date_req={formatted_date}")

    return ET.fromstring(response.content)


def parse_cur_data(xml_root, idCurDict):
    currency_values = {}
    for name, currency_id in idCurDict.items():
        currency_element = xml_root.find(f".//Valute[@ID='{currency_id}']")
        if currency_element is not None:
            value = currency_element.find(
                "VunitRate").text.replace(",", ".")
            currency_values[name] = value
        else:
            currency_values[name] = None
    return currency_values


def generate_cur_table(start_year, end_year, base_url, idCurDict):
    data = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            cur_data = fetch_cur_data(year, month, base_url)
            parsed_data = parse_cur_data(cur_data, idCurDict)
            parsed_data['date'] = f"{year}-{month:02}"
            data.append(parsed_data)
    return pd.DataFrame(data, columns=['date'] + list(idCurDict.keys()))


def get_cur_id(name_id_cur_csv):
    import csv
    cur_dict = {}
    with open(name_id_cur_csv) as file:
        reader = csv.DictReader(file)

        for row in reader:
            for column, value in row.items():
                cur_dict[column] = value
    return cur_dict


if __name__ == "__main__":
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    name_id_cur_csv = 'scriptsData/miningConvert/idCurrencies.csv'
    idCurDict = get_cur_id(name_id_cur_csv)
    df = generate_cur_table(2003, 2024, url, idCurDict)
    df.to_csv("scriptsData/miningConvert/convertingCur.csv", index=False)
