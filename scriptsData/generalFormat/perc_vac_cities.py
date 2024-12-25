import pandas as pd
from dotenv import load_dotenv
import os


def perc_cities(df):
    return (df
            .groupby('area_name')
            .agg(count=('area_name', 'count'))
            .assign(perc=lambda df: df['count'] / 6915297 * 100)
            .query('perc > 1')
            .sort_values(['perc'], ascending=[False])
            .reset_index())


def save_in_file(data, save_file_name):
    data.to_csv(save_file_name, index=False)


if __name__ == "__main__":
    load_dotenv()
    path_main_csv = os.getenv("DATA_VACANCIES")
    df = pd.read_csv(path_main_csv, low_memory=False, usecols=[
        "area_name"])
    df = perc_cities(df)
    save_in_file(df, "scriptsData/generalFormat/percVacCities.csv")
