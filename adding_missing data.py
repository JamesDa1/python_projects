# Exercise 87 from "Practice Python with 100 Python Exercises" on udemy
"""
Add the missing data to the file
"""

# These countries are missing from the file:
checklist = ['Portugal', 'Germany', 'Spain']

with open("./files/input/countries_missing.txt", "r") as file:
    countries = [x for x in file.read().split(sep="\n")]

# A.append(B) adds B as an element of A. A = [1, 2, 3], B = [4,5,6], A.append(B) = [1, 2, 3, [4, 5, 6]]
# A.extend(B) adds the element of B to the end of A. A.extend(B) = [1, 2, 3, 4, 5, 6]
countries.extend(checklist)  # Adds the elements of checklist to the countries list
countries.sort()  # Sorts the list in place

with open("./files/output/countries_restored.txt", "w") as file:
    for country in countries:
        if country != "":
            file.write(country + "\n")

