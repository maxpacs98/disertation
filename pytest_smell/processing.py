import csv
import inspect

import pytest_smell.smells as smells
from pytest_smell.config import TESTS_DIRECTORY, SMELL_INFO_MAPPING, OUTPUT
from .parser import traverse_tests_file


def get_printable_link(file=None, line=None):
    """ Print a link in PyCharm to a line in file.
        Defaults to line where this function was called. """
    if file is None:
        file = inspect.stack()[1].filename
    if line is None:
        line = inspect.stack()[1].lineno
    string = f'File "{file}", line {max(line, 1)}'.replace("\\", "/")
    return string


def output_final_results(count_metrics_mapping):
    print(f'The total number of bad smells detected in the test suite containing '
          f'{count_metrics_mapping["total_test_count"] // len(SMELL_INFO_MAPPING.keys())} tests was:'
          f' {sum([count_metrics_mapping[f"{smell_name}_count"] for smell_name in SMELL_INFO_MAPPING.keys()])}\n')

    for smell_code, smell_info in SMELL_INFO_MAPPING.items():
        print(f'{smell_info["display_name"]} count: {count_metrics_mapping[f"{smell_code}_count"]}')


def write_results_to_file(file_path, all_test_smells):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['test_suite', 'test_name', 'smell', 'metric_value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(all_test_smells)


def detect_smells():
    count_metrics_names = ['total_test_count',
                           *[f'{smell_name}_count' for smell_name in SMELL_INFO_MAPPING.keys()]]
    count_metrics_mapping = {metric_name: 0 for metric_name in count_metrics_names}
    all_test_smells = []
    for smell_code, smell_info in SMELL_INFO_MAPPING.items():
        is_smelly = False
        for f_path, current_test_name, current_test_lines, line_number in \
                traverse_tests_file(smell_info.get('check_annotations')):
            count_metrics_mapping['total_test_count'] += 1
            smell_handler = getattr(smells, f'check_{smell_code}')
            handler_result = smell_handler(current_test_lines)
            if not smell_info.get('reversed_metric'):
                suffers_of_smell = len(handler_result) > smell_info['metric_threshold']
            else:
                suffers_of_smell = len(handler_result) < smell_info['metric_threshold']
            if suffers_of_smell:
                count_metrics_mapping[f'{smell_code}_count'] += 1
                test_suite_name = f_path.split('/')[-1]
                test_smell_mapping = {'test_suite': test_suite_name, 'test_name': current_test_name,
                                      'smell': smell_info['display_name'], 'metric_value': len(handler_result)}
                all_test_smells.append(test_smell_mapping)
                is_smelly = True
                test_smell_message = f'Test {current_test_name} located at ' \
                                     f'{get_printable_link(f"{TESTS_DIRECTORY}/{test_suite_name}", line=line_number)} '\
                                     f'suffers from "{smell_info["display_name"]}". \n' \
                                     f'Explanation: {smell_info["explanation_message"] % len(handler_result)}'
                print(test_smell_message)
                if handler_result:
                    print("\n".join(handler_result))
        if is_smelly:
            print('\n')

    output_final_results(count_metrics_mapping)
    write_results_to_file(f'{OUTPUT}/smells.csv', all_test_smells)
