import pandas as pd
from dotenv import load_dotenv
import os
from avg_salary import get_statistics_avg_sal
from trend_skills import get_trend_skills
from count_years_vac import get_count_vacancies_years
from perc_vac_cities import get_perc_cities

# 317954


def read_file(path_main_csv):
    return pd.read_csv(path_main_csv, low_memory=False)


def get_filtred_vacancy_df(df):
    names = ['cистемный администратор', 'system admin', 'сисадмин', 'сис админ',
             'системный админ', 'cистемный админ', 'администратор систем', 'системний адміністратор']
    names = '|'.join(names)

    return df[df['name'].str.contains(names, case=False)]


def save_in_file(df, name):
    df.to_csv(name, index=False)


if __name__ == "__main__":
    load_dotenv()
    path_main_csv = os.getenv("DATA_VACANCIES")
    dir_filtred = os.getenv("SAVING_PATH_FILTRED_ANALYTIC")
    df = read_file(path_main_csv)
    df = get_filtred_vacancy_df(df)
    # получаем среднюю зп по городам и по годам
    filtred_avg_sal_years, filtred_avg_sal_cities = get_statistics_avg_sal(df)
    save_in_file(filtred_avg_sal_years, os.path.join(
        dir_filtred, "filtredAvgSalYears.csv"))
    save_in_file(filtred_avg_sal_cities, os.path.join(
        dir_filtred, "filtredAvgSalCities.csv"))
    # получаем рейтинг скиллов по годам
    filtred_skills = get_trend_skills(df)
    save_in_file(filtred_skills, os.path.join(
        dir_filtred, "filtredSkills.csv"))

    # получаем кол вакансий по годам
    count_vac_years = get_count_vacancies_years(df)
    save_in_file(count_vac_years, os.path.join(
        dir_filtred, "filtredCountYears.csv"))

    # получаем доли вакансии по городам
    perc_of_cities = get_perc_cities(df)
    save_in_file(perc_of_cities, os.path.join(
        dir_filtred, "percCities.csv"))
