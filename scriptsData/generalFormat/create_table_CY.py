import sqlite3
import pandas as pd

# create table countYears. data from csv

with sqlite3.connect("./data.bd") as con:
    df = pd.read_csv('scriptsData/generalFormat/countYears.csv')
    df.to_sql('countYears', con, if_exists='replace', index=False)
