import pandas as py

df = py.read_csv("Facility_Data Pull.csv")

df_new = df[(df['Date'] != None) & (df['Date']).str.startswith('24-')].copy()

df_new.to_csv("last_year_clean.csv", index = False)
