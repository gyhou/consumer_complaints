import os
import csv
import sys
from decimal import Decimal, ROUND_HALF_UP


def process_csv(file_loc):
    """
    Given the data for consumer complaints, identifying the number of 
    complaints filed and how they're spread across different companies.
    For each financial product and year,  the total number of complaints, 
    number of companies receiving a complaint, and the highest 
    percentage of complaints directed at a single company.

    :param file_loc:
        The file location to extract the csv from.
    """
    processed_data = dict()
    with open(file_loc) as csv_file:
        data = csv.DictReader(csv_file)
        # Data sorted by product (alphabetically) and year (ascending)
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
    :param dict_data:
        The dictionary with the processed data to covert into csv.
    :param save_loc:
        The location to save the csv file to.

    Each line in the output file list the following fields in the following order:
    - product (name should be written in all lowercase)
    - year
    - num_complaint: total number of complaints received for that product and year
    - num_company: total number of companies receiving at least one complaint for that product and year
    - highest percentage (rounded to the nearest whole number) of total complaints filed against one 
    company for that product and year. Use standard rounding conventions 
    (i.e., Any percentage between 0.5% and 1%, inclusive, 
    should round to 1% and anything less than 0.5% should round to 0%)
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


if __name__ == "__main__":
    # Get the current working directory
    directory = os.getcwd().replace("\\", "/")
    # Get the arguments on the command-line
    args = sys.argv

    # File location to read the csv file
    file_to_open = directory + args[1][1:]
    # File location to save the csv file
    loc_to_save = directory + args[2][1:]

    data_dict = process_csv(file_to_open)
    output_csv(data_dict, loc_to_save)
