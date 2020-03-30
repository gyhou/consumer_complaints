# Consumer Complaints

## Table of Contents
1. [Problem](README.md#problem)
1. [Summary](README.md#summary)
1. [Input Dataset](README.md#input-dataset)
1. [Expected output](README.md#expected-output)
1. [Repo directory structure](README.md#repo-directory-structure)
1. [Testing the code](README.md#testing-the-code)

## Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This challenge will be about identifying the number of complaints filed and how they're spread across different companies. 

**For this challenge, we want to know for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.**

## Summary
In the `run.sh` script, `python3.7` is used, followed by the python script file location and name, then the input csv file location and name, then the desired output csv file location and name.

`consumer_complaints.py` has 2 parts: First, process the csv file, then aggregate the processed data and create a new csv file.

### Part 1
`process_csv(file_loc)`: Takes in an input csv and returns a dictionary with processed data.
<br>
Takes in 1 argument `file_loc`: The file location to extract the csv from
1. Check for missing columns (Product, Company, Date Received)
1. Sort the data by product (alphabetically) and year (ascending)
1. Create and returns a dictionary with (product, year) as key
    * The value is another dictionary {company_1: number of complaints} for that (product, year)
    * Lower case both product type and company name
    * Extract year from "Date received"
    
### Part 2
`output_csv(dict_data, save_loc)`: Takes in the processed data and creates an output csv file.
<br>
Takes in 2 arguments `dict_data`: The dictionary with the processed data to covert into csv
* save_loc: The location and name to save the csv file to

1. Set fieldnames for the csv file ('product', 'year', 'num_complaint','num_company', 'highest_percent')
1. (Optional) Write the header (column names) if needed as first row (currently commented out)
1. Create an output csv file
    * Read the dict_data and insert a row for each distinct (product, year)
    * Refer to [Expected output](README.md#expected-output) for more detail

## Input dataset
The code will read an input file,  `complaints.csv`, at the top-most `input` directory of the repository, process it and write the results to an output file, `report.csv` to the top-most `output` directory of the repository.

Each line of the input file, except for the first-line header, represents one complaint. Consult the [Consumer Finance Protection Bureau's technical documentation](https://cfpb.github.io/api/ccdb/fields.html) for a description of each field.  

* Notice that complaints were not listed in chronological order

For the purposes of this challenge, all names, including company and product, should be treated as case insensitive. For example, "Acme", "ACME", and "acme" would represent the same company.

## Expected output
After reading and processing the input file, the code will create an output file, `report.csv`, with as many lines as unique pairs of product and year (of `Date received`) in the input file. 

Each line in the output file should list the following fields in the following order:
* product - type of product the consumer identified in the complaint (written in all lowercase)
* year - year the CFPB received the complaint
* num_complaint - total number of complaints received for that product and year
* num_company - total number of companies receiving at least one complaint for that product and year
* highest_percent - highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year. Using standard rounding conventions (i.e., Any percentage between 0.5% and 1%, inclusive, should round to 1% and anything less than 0.5% should round to 0%)

The lines in the output file will be sorted by product (alphabetically) and year (ascending).

- When a product has a comma (`,`) in the name, the name should be enclosed by double quotation marks (`"`)
- Percentages are listed as numbers and do not have `%` in them.

## Repo directory structure

    ├── README.md
    ├── run.sh
    ├── src
    │   └── consumer_complaints.py
    ├── input
    │   └── complaints.csv
    ├── output
    |   └── report.csv
    └── insight_testsuite
        └── tests
            └── test_1
            |   ├── input
            |   │   └── complaints.csv
            |   ├── output
            |   │   └── report.csv
            └── your-own-tests
                ├── input
                │   ├── complaints.csv
                │   ├── test1_complaints.csv
                │   ├── test2_complaints.csv
                │   ├── test3_complaints.csv
                │   └── test4_complaints.csv
                |── output
                │   ├── report.csv
                │   └── report_test.csv
                ├── consumer_complaints_test.py
                └── consumer_complaints.py

## Testing the code
This code successfully passed the test using the <a href="https://insight-cc-submission.com/test-my-repo-link">web page</a> to ensure the code can run in the Linux environment.

The `insight_testsuite` directory showcase input tests for the code. Under that directory, `test_1` contains the sample input and output files, `your-own-tests` contain an unittest file `consumer_complaints_test.py` to test various csv input files.

Unit test `consumer_complaints_test.py` tests:
1. If the output csv is the same as sample output
1. If the input csv has missing column
1. If the input csv has non-int year value
1. If the input csv has value error for year
1. If the input csv has value error for product and company
