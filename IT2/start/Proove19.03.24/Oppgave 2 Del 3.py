'''
Kilder:
https://www.w3schools.com/python/pandas/pandas_csv.asp
https://saturncloud.io/blog/pandas-get-day-of-week-from-date-type-column/
https://pandas.pydata.org/docs/reference/api/pandas.Period.strftime.html

Jeg bestemte meg for å bare ta "duration" 
'''

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('IT2/start/Proove19.03.24/run.csv')

df['datetime'] = pd.to_datetime(df['datetime'])

weekly_activity = df.groupby(df['datetime'].dt.strftime('%W'))['duration'].sum()

mest_aktiv_uke = weekly_activity.idxmax()
maksimal_aktivitet = weekly_activity.max()

print("Uke med mest aktivitet:", mest_aktiv_uke)
print("Total varighet i denne uken:", maksimal_aktivitet)

plt.figure(figsize=(10, 6))
weekly_activity.plot(kind='bar', color='skyblue')
plt.title('Aktivitet per uke gjennom året')
plt.xlabel('Uke nummer')
plt.ylabel('Total varighet (minutter)')
plt.show()
