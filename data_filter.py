"""
# Exercise 88 from "Practice Python with 100 Python Exercises" on udemy
Question: Create a script that uses the attached countries_by_area.txt  file as
data source and prints out the top 5 most densely populated countries
"""
import pandas as pd
source_file = "./files/input/countries_by_area.txt"

df = pd.read_csv(source_file)
df['pop_density'] = df.population_2013 / df.area_sqkm
df = df.sort_values('pop_density', ascending=False)

for index, row in df[:5].iterrows():
    print(row.country)