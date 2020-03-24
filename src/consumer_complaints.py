import os
import csv
import sys
from decimal import Decimal, ROUND_HALF_UP

# args = sys.argv
# args[0], args[1]

os.chdir("..")  # Go up one directory from working directory
directory = os.getcwd()  # Gets the current working directory
# input_folder = f"{directory}/input/"
# file_name = "complaints.csv"
# file_to_open = input_folder + file_name
file_to_open = f"{directory}/input/complaints.csv"


def process_csv(file_loc):
    """
    """
    processed_data = dict()
    with open(file_loc) as csv_file:
        data = csv.DictReader(csv_file)
        data = sorted(data, key=lambda row: (
            row['Product'], row['Date received']), reverse=False)

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
    return processed_data


def output_csv(dict_data, save_loc):
    """
    """
    with open(save_loc, 'w') as csv_file:
        field_names = ['product', 'year', 'num_complaint',
                       'num_company', 'highest_percent']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

        # writer.writeheader() # Write header if needed as first row
        for product_year, company_complaint in dict_data.items():
            product = product_year[0]
            year = product_year[1]
            num_complaint = sum(company_complaint.values())
            num_company = len(company_complaint)
            highest_percent = (Decimal(max(company_complaint.values()) /
                                       sum(company_complaint.values()) * 100).
                               quantize(0, ROUND_HALF_UP))

            writer.writerow({'product': product,
                             'year': year,
                             'num_complaint': num_complaint,
                             'num_company': num_company,
                             'highest_percent': highest_percent})


data_dict = process_csv(file_to_open)
loc_to_save = f"{directory}/output/report.csv"
output_csv(data_dict, loc_to_save)
