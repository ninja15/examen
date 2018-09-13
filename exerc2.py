import pandas as pd
import numpy as np
import sqlite3


with sqlite3.connect('db.sqlite3') as conn:
    df = pd.read_sql('select * from main_users', conn)
    df.to_csv('users.csv')


print(df)
print(df['number_of_login'].mean())
print(df['number_of_login'].std())

