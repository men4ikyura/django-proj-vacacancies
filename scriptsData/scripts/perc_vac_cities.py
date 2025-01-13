import pandas as pd
from dotenv import load_dotenv
import os


def get_perc_cities(df):
    length_df = len(df)
    perc_cities = (df
                   .groupby('area_name')
                   .agg(count=('area_name', 'count'))
                   .assign(perc=lambda row: row['count'] / length_df * 100)
                   .query('perc > 2')
                   .round(2)
                   .sort_values(['perc'], ascending=[False])
                   .reset_index()
                   .drop(columns="count")
                   )
    perc_cities.loc[len(perc_cities)] = [
        "Другие", 100 - perc_cities["perc"].sum()]
    return perc_cities


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
    save_in_file(perc_cities, save_file_name)
