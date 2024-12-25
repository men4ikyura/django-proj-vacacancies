import pandas as pd


if __name__ == "__main__":
    df = pd.read_csv("scriptsData/vacancies_2024.csv",
                     low_memory=False, usecols=['salary_currency'])

    df = df.salary_currency.unique()
    data_frame = pd.DataFrame(df, columns=['uniqCurrencies'])
    data_frame.to_csv('scriptsData/miningConvert/uniqCurrencies.csv',
                      index=False, encoding='utf-8')
