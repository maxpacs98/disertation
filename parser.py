import os
import re

from smells import check_assertion_roulette, check_duplicate_assert, check_eager_test, check_conditional_logic


def traverse_tests_directory(directory_path):
    for dir_path, _, files in os.walk(directory_path):
        if '__pycache__' in dir_path:
            continue
        for filename in files:
            file_path = os.path.join(dir_path, filename)
            if filename.startswith('test') or filename.endswith('test.py'):
                with open(file_path) as test_file:
                    yield file_path, test_file.readlines()


def parse_tests_file():
    for file_path, lines in traverse_tests_directory('smelly_tests'):
        current_test_name, current_test_lines = None, []
        for line_number, line in enumerate(lines):
            line = line.strip('\n')
            if line.startswith('def test_'):
                current_test_name = re.search('def (.*)\\(', line).group(1)
            if current_test_name:
                if '    ' in line or line.startswith('def test_'):
                    current_test_lines.append(line.strip())
                    if line_number == len(lines) - 1:  # eof
                        process_test_lines(current_test_name, current_test_lines)
                else:
                    process_test_lines(current_test_name, current_test_lines)
                    current_test_name, current_test_lines = None, []


def process_test_lines(current_test_name, current_test_lines):
    suffers_from_assertion_roulette, count = check_assertion_roulette(current_test_lines)
    if suffers_from_assertion_roulette:
        print(f'Test {current_test_name} suffers from "Assertion Roulette". Explanation: it has multiple ({count}) '
              f'undocumented assertions')
    suffers_from_duplicate_assert, duplicate_lines = check_duplicate_assert(current_test_lines)
    if suffers_from_duplicate_assert:
        print(f'Test {current_test_name} suffers from "Duplicate Assert". '
              f'Explanation: the following assertion(s) are duplicate:')
        print("\n".join([ass.split(',')[0] for ass in duplicate_lines]))
    suffers_from_eager_test, distinct_methods = check_eager_test(current_test_lines)
    if suffers_from_eager_test:
        print(f'Test {current_test_name} suffers from "Eager Test". '
              f'Explanation: it has multiple ({len(distinct_methods)}) methods tested:')
        print("\n".join(distinct_methods))
    suffers_from_conditional_logic, distinct_control_statements = check_conditional_logic(current_test_lines)
    if suffers_from_conditional_logic:
        print(f'Test {current_test_name} suffers from "Conditional logic". '
              f'Explanation: it has multiple ({len(distinct_control_statements)}) control flow statement(s):')
        print("\n".join(distinct_control_statements))
    if suffers_from_assertion_roulette or suffers_from_duplicate_assert or suffers_from_eager_test or \
            suffers_from_conditional_logic:
        print('========================================================================================================'
              '===========================================')
