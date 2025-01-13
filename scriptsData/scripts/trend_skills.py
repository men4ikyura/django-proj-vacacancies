import pandas as pd
from dotenv import load_dotenv
import os
from collections import Counter
import json


def get_trend_skills(df):

    groups = (df.dropna(subset=["key_skills"])
              .assign(published_at=lambda x: pd.to_datetime(x["published_at"], errors="coerce", utc=True).dt.year)
              .groupby("published_at"))

    years_skills_dict = {}
    for year, group in groups:
        skills = Counter(skill for skills in group["key_skills"].str.split(
            '\n') for skill in skills).most_common(20)
        years_skills_dict[year] = skills

    return years_skills_dict


def save_in_file(dict, name):
    with open(name, 'w') as file:
        json.dump(dict, file, ensure_ascii=False, indent=4)


def read_file(name_main_csv):
    return pd.read_csv(name_main_csv, low_memory=False,
                       usecols=["key_skills", "published_at"])


if __name__ == "__main__":
    load_dotenv()
    name_main_csv = os.getenv("DATA_VACANCIES")
    save_file_name = os.path.join(
        os.getenv("SAVING_PATH_GENERAL_ANALYTIC"), "trend_skills.json")
    dict = read_file(name_main_csv)
    dict = get_trend_skills(dict)
    save_in_file(dict, save_file_name)
