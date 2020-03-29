# Consumer Complaints

## Table of Contents
1. [Problem](README.md#problem)
1. [Input Dataset](README.md#input-dataset)
1. [Expected output](README.md#expected-output)
1. [Tips on getting an interview](README.md#tips-on-getting-an-interview)
1. [Repo directory structure](README.md#repo-directory-structure)
1. [Testing your code](README.md#testing-your-code)
1. [Questions?](README.md#questions?)

Before submitting your solution you should summarize your approach and run instructions (if any) in your README.

## Problem
The federal government provides a way for consumers to file complaints against companies regarding different financial products, such as payment problems with a credit card or debt collection tactics. This challenge will be about identifying the number of complaints filed and how they're spread across different companies. 

**For this challenge, we want to know for each financial product and year, the total number of complaints, number of companies receiving a complaint, and the highest percentage of complaints directed at a single company.

## Input dataset
The code will read an input file,  `complaints.csv`, at the top-most `input` directory of the repository, process it and write the results to an output file, `report.csv` to the top-most `output` directory of the repository.

Each line of the input file, except for the first-line header, represents one complaint. Consult the [Consumer Finance Protection Bureau's technical documentation](https://cfpb.github.io/api/ccdb/fields.html) for a description of each field.  

* Notice that complaints were not listed in chronological order

For the purposes of this challenge, all names, including company and product, should be treated as case insensitive. For example, "Acme", "ACME", and "acme" would represent the same company.

## Expected output
After reading and processing the input file, the code will create an output file, `report.csv`, with as many lines as unique pairs of product and year (of `Date received`) in the input file. 

Each line in the output file should list the following fields in the following order:
* product (name should be written in all lowercase)
* year
* total number of complaints received for that product and year
* total number of companies receiving at least one complaint for that product and year
* highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year. Use standard rounding conventions (i.e., Any percentage between 0.5% and 1%, inclusive, should round to 1% and anything less than 0.5% should round to 0%)

The lines in the output file will be sorted by product (alphabetically) and year (ascending).

- When a product has a comma (`,`) in the name, the name should be enclosed by double quotation marks (`"`)
- Percentages are listed as numbers and do not have `%` in them.

## Tips on getting an interview
As a data engineer, it’s important that you write clean, well-documented code that scales for a large amount of data. For this reason, it’s important to ensure that your solution works well for a large number of records, rather than just the above example.

[Here](http://files.consumerfinance.gov/ccdb/complaints.csv.zip) you can find a zipped, modest-sized dataset to test your code (see [here](https://cfpb.github.io/api/ccdb/fields.html) for more information on the data dictionary).

Note, we will use this data to test the full functionality of your code, along with other test cases.

It's important to use software engineering best practices like unit tests, especially because data is not always clean and predictable.

Before submitting your solution you should summarize your approach and run instructions (if any) in your README.

You may write your solution in any mainstream programming language, such as C, C++, Go, Java, Python, Ruby, or Scala. Once completed, submit a link of your Github or Bitbucket repo with your source code.

In addition to the source code, the top-most directory of your repo must include the input and output directories, and a shell script named run.sh that compiles and runs the program(s) that implement(s) the required features.

See the figure below for the required structure of the top-most directory in your repo, or simply clone this repo.

## Repo directory structure
The top-level directory structure for your repo should look like the following: (So that we can grade your submission, replicate this directory structure at the top-most level of your project repository. Do not place the structure in a subdirectory)

    ├── README.md
    ├── run.sh
    ├── src
    │   └── consumer_complaints.py
    ├── input
    │   └── complaints.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── tests
            └── test_1
            |   ├── input
            |   │   └── complaints.csv
            |   |__ output
            |   │   └── report.csv
            ├── your-own-test_1
                ├── input
                │   └── complaints.csv
                |── output
                    └── report.csv

**Don't fork this repo** and don't use this `README` instead of your own. The content of `src` does not need to be a single file called `consumer_complaints.py`, which is only an example. Instead, you should include your own source files and give them expressive names.

## Testing your code
As an engineer, you'll want to make sure you are thoroughly testing your code. Use the `insight_testsuite` directory to showcase the tests you conducted on your code. Under that directory, create a separate folder for each test. Each test directory should also have a separate `input` subdirectory containing the `complaint.csv` input file you want to test, and an `output` subdirectory containing the expected `report.csv` output for that test.

We've included one test (`test_1`), which contains the sample input and output files detailed in this Readme. To test your code, you can manually move each input test file into the top-level input directory, then run your program and compare the output with the expected output. Or you can write a script to do this automatically, but note we are not requiring you to write a test script.

We do ask that you test your code using the <a href="https://insight-cc-submission.com/test-my-repo-link">web page</a> mentioned earlier to ensure your code can run in the Linux environment that we will review your code. The test page will check to see if your code passes `test_1`. If there are errors or if the results don't match what is expected, you should debug your code's behavior by yourself. If you receive system errors that you do not believe are due to your code, you can email cc@insightdataengineering.com for help.

If your code must be compiled to run (e.g., javac, make), that compilation (as well as the execution) of your code must be specified in the `run.sh` script of your code repository. 

For Python programmers, you can use Python 2 or Python 3. If you use the former, specify `python` in your `run.sh` script, or if you use the later, specify `python3`, which defaults to Python 3.5.2. Other options that could be use are `python3.7` or `python3.8`.

## Questions?
Email us at cc@insightdataengineering.com

