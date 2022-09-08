"""
# Exercise 89 from "Practice Python with 100 Python Exercises" on udemy
File contains 50 with their area in square km and population
Use python to print out those countries with an area > 2 000 000
"""

import sqlite3
source_file = "./files/input/database.db"
con = sqlite3.connect(source_file)
cur = con.cursor()

# cur.execute("CREATE TABLE movie(title, year, score)")
res = cur.execute("DELETE TABLE movie")
res.fetchone()
print(res.fetchone())