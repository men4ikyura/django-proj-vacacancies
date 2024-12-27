import pandas as pd
from dotenv import load_dotenv
import os
from collections import Counter

# везде где указаны скиллы - указана и дата


def get_trend_skills(df):

    groups = (df.dropna(subset=["key_skills"])
              .assign(published_at=lambda x: pd.to_datetime(x["published_at"], errors="coerce", utc=True).dt.year)
              .groupby("published_at"))

    df = pd.DataFrame()
    for year, group in groups:
        skills = Counter(skill for skills in group["key_skills"].str.split(
            '\n') for skill in skills).most_common(20)
        df[year] = [skill[0] for skill in skills]

    return df


def save_in_file(df, name):
    df.to_csv(name, index=False)


def read_file(name_main_csv):
    return pd.read_csv(name_main_csv, low_memory=False,
                       usecols=["key_skills", "published_at"])


if __name__ == "__main__":
    load_dotenv()
    name_main_csv = os.getenv("DATA_VACANCIES")
    save_file_name = os.path.join(
        os.getenv("SAVING_PATH_GENERAL_ANALYTIC"), "trend_skills.csv")
    df = read_file(name_main_csv)
    df = get_trend_skills(df)
    save_in_file(df, save_file_name)
