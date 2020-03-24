from pathlib import Path
import csv
import os


os.chdir("..") # Go up one directory from working directory
directory = os.getcwd() # Gets the current working directory
input_folder = f"{directory}/input/"
file_name = "complaints.csv"
file_to_open = input_folder + file_name

processed_data = dict()
with open(file_to_open) as csv_file:
    data = csv.DictReader(csv_file)
    for row in data:
        product = row['Product'].lower()
        date = row['Date received'][:4]
        company = row['Company'].lower()
        if (product, date) in processed_data:
            if company in processed_data[product, date]:
                processed_data[product, date][company] += 1
            else:
                processed_data[product, date][company] = 1
        else:
            processed_data[product, date] = {company: 1}
print(processed_data)