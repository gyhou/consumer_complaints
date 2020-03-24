import csv
import os
from decimal import Decimal, ROUND_HALF_UP


os.chdir("..")  # Go up one directory from working directory
directory = os.getcwd()  # Gets the current working directory
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


loc_to_save = f"{directory}/output/report.csv"

with open('output/report.csv', 'w') as csv_file:
    fieldnames = ['product', 'year', 'num_complaints',
                  'num_companies', 'highest_percentage']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # writer.writeheader() # Write header if needed as first row
    for product_year, company_complaints in processed_data.items():
        product = product_year[0]
        year = product_year[1]
        num_complaints = sum(company_complaints.values())
        num_companies = len(company_complaints)
        highest_percentage = (Decimal(max(company_complaints.values()) /
                                      sum(company_complaints.values())*100).
                              quantize(0, ROUND_HALF_UP))

        writer.writerow({'product': product,
                         'year': year,
                         'num_complaints': num_complaints,
                         'num_companies': num_companies,
                         'highest_percentage': highest_percentage})
