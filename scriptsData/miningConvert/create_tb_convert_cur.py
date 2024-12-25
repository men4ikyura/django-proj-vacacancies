import sqlite3
import pandas as pd


with sqlite3.connect("./data.bd") as con:
    df = pd.read_csv('scriptsData/miningConvert/convertingCur.csv')
    df.to_sql('convertingCur', con, if_exists='replace', index=False)
