import os
import csv
import unittest
from consumer_complaints import process_csv, output_csv


class TestConsumerComplaints(unittest.TestCase):
    def setUp(self):
        self.directory = os.getcwd().replace("\\", "/")

    def test_output(self):
        # Test if output is same as sample
        input_file = self.directory + '/input/complaints.csv'
        output_loc = self.directory + '/output/report.csv'
        expected_output = self.directory + '/output/report_test.csv'

        output_csv(process_csv(input_file), output_loc)

        with open(expected_output, 'r') as csv_file:
            csv_report = csv.reader(csv_file, delimiter=',')
            expected_report = [row for row in csv_report if row]
        with open(output_loc, 'r') as csv_file:
            csv_report = csv.reader(csv_file, delimiter=',')
            actual_report = [row for row in csv_report if row]

        self.assertEqual(actual_report, expected_report)

    def test_error(self):
        # Test if function is catching error in input csv
        test1 = self.directory + '/input/test1_complaints.csv'
        self.assertRaises(KeyError, process_csv, test1) # missing column
        test2 = self.directory + '/input/test2_complaints.csv'
        self.assertRaises(ValueError, process_csv, test2) # non-int year
        test3 = self.directory + '/input/test3_complaints.csv'
        self.assertRaises(ValueError, process_csv, test3) # blank year
        test4 = self.directory + '/input/test4_complaints.csv'
        self.assertRaises(TypeError, process_csv, test4) # invalid product, company


if __name__ == '__main__':
    unittest.main()
