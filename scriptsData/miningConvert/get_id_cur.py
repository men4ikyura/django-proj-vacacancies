import requests
import csv
import xml.etree.ElementTree as ET


def get_cur_dict(name):
    cur_dict = dict()
    with open(name, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for cur in reader:
            if cur[0] != "RUR":
                cur_dict[cur[0]] = ""

    return cur_dict


def get_cur_id(cur_dict):
    for year in range(2003, 2024 + 1):
        url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/{year}"
        req = requests.get(url)
        xml_info = ET.fromstring(req.content)
        for currency in cur_dict.keys():
            for valute in xml_info:
                if valute[1].text == currency and cur_dict[currency] == '':
                    cur_dict[currency] = valute.attrib['ID']
    return cur_dict


def save_in_csv(result_csv_name, cur_dict):
    with open(result_csv_name, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=cur_dict.keys())
        writer.writeheader()
        writer.writerow(cur_dict)


if __name__ == "__main__":
    cur_csv_name = "scriptsData/miningConvert/uniqCurrencies.csv"
    result_csv_name = "scriptsData/miningConvert/idCurrencies.csv"
    cur_dict = get_cur_dict(cur_csv_name)
    currenciesId = get_cur_id(cur_dict)
    save_in_csv(result_csv_name, currenciesId)
