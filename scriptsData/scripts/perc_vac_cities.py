import pandas as pd
from dotenv import load_dotenv
import os


def get_perc_cities(df):
    length_df = len(df)
    return (df
            .groupby('area_name')
            .agg(count=('area_name', 'count'))
            .assign(perc=lambda row: row['count'] / length_df * 100)
            .query('perc > 2')
            .round(1)
            .sort_values(['perc'], ascending=[False])
            .reset_index())

    # до округления
    # area_name,count,perc
    # Москва,2339355,33.82869889753108
    # Санкт-Петербург,699079,10.109168123943196
    # Минск,242952,3.513254745240877
    # Новосибирск,164573,2.3798399403525257
    # Екатеринбург,153806,2.224141638457466
    # Нижний Новгород,143200,2.070771508439912
    # Киев,140524,2.032074688910686
    # Алматы,139700,2.0201590763202217
    # Казань,137692,1.9911220009784107
    # Воронеж,112049,1.6203064018797748
    # Краснодар,103149,1.4916062173468472
    # Ростов-на-Дону,92587,1.3388723579045123
    # Самара,90915,1.3146940760461916
    # Пермь,69543,1.0056401048284693


def save_in_file(data, save_file_name):
    data.to_csv(save_file_name, index=False)


def read_file(path_main_csv):
    return pd.read_csv(path_main_csv, low_memory=False, usecols=[
        "area_name"])


if __name__ == "__main__":
    load_dotenv()
    save_file_name = os.path.join(
        os.getenv("SAVING_PATH_GENERAL_ANALYTIC"), "percVacCities.csv")
    path_main_csv = os.getenv("DATA_VACANCIES")
    df = read_file(path_main_csv)
    perc_cities = get_perc_cities(df)
    perc_cities.loc[len(perc_cities)] = [
        "Другие", 0, 100 - perc_cities["perc"].sum()]
    save_in_file(perc_cities, save_file_name)
