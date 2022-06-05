import argparse
import os

from pytest_smell.processing import detect_smells

parser = argparse.ArgumentParser()
parser.add_argument('--verbose', action='store_true',
                    help='Full output which contains smelly tests positions and explanations.')
parser.add_argument('--ci', action='store_true',
                    help='Returns exit code 1 if any smells were found, 0 if the test code is smell free.')
parser.add_argument('--tests_path', type=str,
                    help='Optionally specify path to tests root directory. Default is current directory.')
parser.add_argument('--out_path', type=str,
                    help='Optionally specify path to write the resulting CSV file. Default is current directory.')
args = parser.parse_args()


def pytest_smell():
    test_path = os.getcwd()
    if args.tests_path:
        test_path = args.tests_path

    all_smells = detect_smells(test_path, args.out_path, args.verbose, args.ci)
    if args.ci:
        if not all_smells:
            exit(0)
        else:
            exit(1)
