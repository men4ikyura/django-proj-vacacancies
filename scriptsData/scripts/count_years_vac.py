import pandas as pd
from dotenv import load_dotenv
import os


def get_count_vacancies_years(df):

    return (df
            .assign(published_at=lambda x: pd.to_datetime(x["published_at"], errors="coerce", utc=True).dt.year)
            .groupby("published_at")
            .agg(size=("published_at", "size"))
            .sort_values(['published_at'], ascending=[False])
            .reset_index())


def read_file(name):
    return pd.read_csv(name, low_memory=False, usecols=["published_at"])


def save_in_file(df, name):
    df.to_csv(name, index=False)


if __name__ == "__main__":
    load_dotenv()
    path_main_csv = os.getenv("DATA_VACANCIES")
    save_file_name = os.path.join(
        os.getenv("SAVING_PATH_GENERAL_ANALYTIC"), "countYears.csv")
    df = read_file(path_main_csv)
    count_vac_years = get_count_vacancies_years(df)
    save_in_file(count_vac_years, save_file_name)
