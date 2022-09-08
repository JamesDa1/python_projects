"""
# Exercise 86 from "Practice Python with 100 Python Exercises" on udemy
Question: Please take a look at the following list:

checklist = ["Portugal", "Germany", "Munster", "Spain"]

One of the items is not a country. Please use Python and the file containing the list of countries (attached)
as the data source to filter out the checklist  of non-country items. Once you have filtered out checklist ,
then print it out.

"""
checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open("./files/input/countries_clean.txt", "r") as file:
    content = [x for x in file.read().split(sep="\n")]

checked_list = [x for x in checklist if x in content]
print(checked_list)
