import pandas as pd


def get_count_vacancies_years(data):

    return (data
            .groupby('published_at')
            .size()
            .reset_index(name='count')
            .rename(columns={'published_at': 'years'})
            )


def prepare_data(name):
    df = pd.read_csv(name, low_memory=False, usecols=['published_at'])
    df["published_at"] = pd.to_datetime(
        df['published_at'], errors='coerce', utc=True).dt.year

    return df


def save_data(data, name):
    data.to_csv(name, index=False)


if __name__ == "__main__":
    save_file_name = 'scriptsData/generalFormat/countYears.csv'
    file_name = 'scriptsData/vacancies_2024.csv'
    data = prepare_data(file_name)
    statictics = get_count_vacancies_years(data)
    save_data(statictics, save_file_name)
