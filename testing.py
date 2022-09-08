# Exercise 85 from "Practice Python with 100 Python Exercises" on udemy
"""
Question: Please download the attached countries-raw.txt file.
The file contains the list of country names, but it also contains some unnecessary text among the countries.

Please clean the list with Python by generating a new text file that contains a flawless list of country names
without any other text or brake lines in it. The new file content should look like in the expected output.
"""

source_file = "./files/input/countries_raw.txt"

with open(source_file, "r") as file:
    processed_text = [x.strip() for x in file.read().split(sep="\n") if len(x) > 1 and x != "Top of Page"]
    # String.strip() removes spaces at the beginning and end of the string
    # String.split() separates string into a list based on separator, default is empty space, but I used NEW_LINE
    # since some country names have spaces
    # len() > 1 to remove single letters
with open("./files/output/countries_cleaned.txt", "w") as file:
    for line in processed_text:
        file.write(line + "\n")


