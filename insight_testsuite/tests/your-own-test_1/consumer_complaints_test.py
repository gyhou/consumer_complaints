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

        with open(expected_output, newline='') as csv_file:
            csv_report = csv.reader(csv_file, delimiter=',')
            expected_report = [row for row in csv_report]
            print(expected_report)
        with open(output_loc, 'r') as csv_file:
            csv_report = csv.reader(csv_file, delimiter=',')
            actual_report = [row for row in csv_report]
            print(actual_report)

        self.assertEqual(actual_report, expected_report)

    # def test_error(self):
    #     # Test if function is catch error
    #     test1 = self.directory + '/input/test1_complaints.csv'
    #     self.assertRaises(KeyError, process_csv, test1)


if __name__ == '__main__':
    unittest.main()
