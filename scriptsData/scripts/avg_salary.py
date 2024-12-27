import pandas as pd
from dotenv import load_dotenv
import os
import sqlite3


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


def prepare_data(df, con):

    # подсчет средней зп
    df["average"] = df[["salary_from", "salary_to"]].mean(
        axis=1)

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
    length_df = len(df)
    return (df
            .groupby('area_name')
            .agg(count=('area_name', 'count'),
                 average=('average', 'mean'))
            .assign(perc=lambda row: row['count'] / length_df * 100)
            .query('perc > 1')
            .sort_values(['average', 'area_name'], ascending=[False, True])
            .reset_index())


def get_statistics_avg_sal(df):

    with sqlite3.connect("./data.bd") as con:
        data = prepare_data(df, con)

    avg_salary_of_years = avg_salary_years(data)
    avg_salary_of_cities = avg_salary_cities(data)

    return avg_salary_of_years, avg_salary_of_cities


def read_file(path_main_csv):
    return pd.read_csv(path_main_csv, low_memory=False, usecols=[
        "area_name", "salary_from", "salary_to", "salary_currency", "published_at"])


if __name__ == "__main__":
    load_dotenv()
    path_main_csv = os.getenv("DATA_VACANCIES")
    save_file_name_cities = os.path.join(
        os.getenv("SAVING_PATH_GENERAL_ANALYTIC"), "avg_salary_cities.csv")
    save_file_name_years = os.path.join(
        os.getenv("SAVING_PATH_GENERAL_ANALYTIC"), "avg_salary_years.csv")
    df = read_file(path_main_csv)
    avg_salary_of_years, avg_salary_of_cities = get_statistics_avg_sal(df)
    save_in_file(avg_salary_of_years, save_file_name_years)
    save_in_file(avg_salary_of_cities, save_file_name_cities)
