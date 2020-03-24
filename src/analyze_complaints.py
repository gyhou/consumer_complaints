from pathlib import Path
import csv
import os


os.chdir("..") # Go up one directory from working directory
directory = os.getcwd() # Gets the current working directory
input_folder = f"{directory}/input/"
file_name = "complaints.csv"
file_to_open = input_folder + file_name

with open(file_to_open) as csv_file:
    data = csv.reader(csv_file, delimiter=',')
    for row in data:
        print(row)