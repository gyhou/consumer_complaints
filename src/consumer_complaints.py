import os
import csv
import sys
from decimal import Decimal, ROUND_HALF_UP


def process_csv(file_loc):
    """
    :param file_loc:
        The file location to extract the csv from.

    Given the data for consumer complaints, identifying the number of 
    complaints filed and how they're spread across different companies.
    For each financial product and year,  the total number of complaints, 
    number of companies receiving a complaint, and the highest 
    percentage of complaints directed at a single company.

    Returns a dictionary:
        {(product_1, year_1): {company_1: number of complaints, company_2...},
         (product_1, year_2): {company_1...},
         ...
         (product_2, year_1)...}
    """
    processed_data = dict()
    with open(file_loc) as csv_file:
        data = csv.DictReader(csv_file)

        # Check for missing columns
        missing_col = []
        if 'Product' not in data.fieldnames:
            missing_col.append('Product')
        if 'Date received' not in data.fieldnames:
            missing_col.append('Date received')
        if 'Company' not in data.fieldnames:
            missing_col.append('Company')
        if missing_col:
            raise KeyError(f"The csv is missing {missing_col} column(s).")

        # Data sorted by product (alphabetically) and year (ascending)
        data = sorted(data, key=lambda row: (
            row['Product'], row['Date received']), reverse=False)

        for row in data:
            product = row['Product'].lower()
            year = row['Date received'][:4]
            company = row['Company'].lower()

            # Check if product, year, company are valid
            if product in ['', 'n/a', 'none', 'nan', None] or product.isspace():
                raise TypeError(f'"{product}" is not a valid product.')
            if company in ['', 'n/a', 'none', 'nan', None] or company.isspace():
                raise TypeError(f'"{company}" is not a valid company.')
            try:
                int(year)
            except ValueError:
                raise ValueError(f'"{year}" is not a valid year.')
            # Set primary key (product, year)
            if (product, year) in processed_data:
                if company in processed_data[product, year]:
                    processed_data[product, year][company] += 1
                else:
                    processed_data[product, year][company] = 1
            else:
                processed_data[product, year] = {company: 1}
    return processed_data


def output_csv(dict_data, save_loc):
    """
    :param dict_data:
        The dictionary with the processed data to covert into csv.
    :param save_loc:
        The location to save the csv file to.

    Creates a csv file in the output folder.
    Each line in the output file list the following fields in the following order:
    - product (name should be written in all lowercase)
    - year
    - num_complaint: total number of complaints received for that product and year
    - num_company: total number of companies receiving at least one complaint for that product and year
    - most_complaints: company with most complaints for that product and year
    - highest percentage (rounded to the nearest whole number) of total complaints filed against one 
    company for that product and year.
    """
    with open(save_loc, 'w') as csv_file:
        field_names = ['product', 'year', 'num_complaint', 'num_company', 
                       'most_complaints', 'highest_percent']
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

        writer.writeheader()
        for product_year, company_complaint in dict_data.items():
            product = product_year[0]
            year = product_year[1]
            num_complaint = sum(company_complaint.values())
            num_company = len(company_complaint)
            most_complaints = max(company_complaint, key=company_complaint.get)
            # Python round() does not round .5 up to 1
            highest_percent = (Decimal(max(company_complaint.values()) /
                                       sum(company_complaint.values()) * 100).
                               quantize(0, ROUND_HALF_UP))

            writer.writerow({'product': product,
                             'year': year,
                             'num_complaint': num_complaint,
                             'num_company': num_company,
                             'most_complaints': most_complaints,
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
