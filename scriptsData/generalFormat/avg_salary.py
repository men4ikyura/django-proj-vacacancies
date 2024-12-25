import pandas as pd
from dotenv import load_dotenv
import os
import sqlite3
import numpy as np


# Name: average, Length: 3506009, dtype: float32
# просто с указанием валюты и без зп таких нет
# заменить тип salary_currency на categories


def get_koef(date, currency, con):
    if currency == "RUR":
        return 1

    query = f"SELECT {currency} FROM convertingCur WHERE date = '{date}'"
    result = pd.read_sql(query, con)
    if result.isnull().values.any():
        return -1
    return result.iloc[0, 0]


def get_salary_rubles(row, connection):
    if pd.isnull(row["average"]):
        return None
    # если валюта рубли сохраняем зп
    # получаем коэф из бд
    koef = get_koef(row["published_at"][:7],
                    row["salary_currency"], connection)
    if koef != -1:
        rubles_salary = row["average"] * koef
        if rubles_salary < 1000000:
            return rubles_salary
        return None
    else:
        return None


def prepare_data(path_main_csv, con):

    # read data from csv
    df = pd.read_csv(path_main_csv, low_memory=False, usecols=[
        "area_name", "salary_from", "salary_to", "salary_currency", "published_at"])

    # подсчет средней зп
    df["average"] = df[["salary_from", "salary_to"]].mean(
        axis=1)

    # не учитываем в подсчете те строки у которых зп 0

    # перевод зп в рубли
    df['average'] = df.apply(
        lambda row: get_salary_rubles(row, con), axis=1)

    df["published_at"] = pd.to_datetime(
        df['published_at'], errors='coerce', utc=True).dt.year

    return df


def save_in_file(data, save_file_name):
    data.to_csv(save_file_name, index=False)


def avg_salary_years(df):
    return (df
            .groupby("published_at")
            .agg(average=('average', 'mean'),
                 count=('average', 'count'),
                 sum=('average', 'sum'))
            .reset_index())


def avg_salary_cities(df):
    return (df
            .groupby('area_name')
            .agg(count=('area_name', 'count'),
                 average=('average', 'mean'))
            .assign(perc=lambda df: df['count'] / 6915297 * 100)
            .query('perc > 1')
            .sort_values(['average', 'area_name'], ascending=[False, True])
            .reset_index())


if __name__ == "__main__":
    load_dotenv()
    path_main_csv = os.getenv("DATA_VACANCIES")
    save_file_name_cities = "scriptsData/generalFormat/avg_salary_cities.csv"
    save_file_name_years = "scriptsData/generalFormat/avg_salary_years.csv"

    with sqlite3.connect("./data.bd") as con:
        data = prepare_data(path_main_csv, con)

    avg_salary_of_years = avg_salary_years(data)
    save_in_file(avg_salary_of_years, save_file_name_years)
    avg_salary_of_cities = avg_salary_cities(data)
    save_in_file(avg_salary_of_cities, save_file_name_cities)

# df = pd.DataFrame([[1, 1, 2, 3],
#                    [1, 4, 5, 6],
#                    [1, 7, 8, 9],
#                    [1, np.nan, np.nan, np.nan]],
#                   columns=['AA', 'A', 'B', 'C'])
# print(df)
# print(df.iloc[3, 3])
# if pd.notnull(df.iloc[3, 3]):
#     print("fa")
