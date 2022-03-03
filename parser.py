import os
import re


def traverse_tests_directories(root_path):
    for dir_path, _, files in os.walk(root_path):
        if '__pycache__' in dir_path:
            continue
        for filename in files:
            file_path = os.path.join(dir_path, filename)
            if filename.startswith('test') or filename.endswith('test.py'):
                with open(file_path) as test_file:
                    yield file_path, test_file.readlines()


def traverse_tests_file():
    for file_path, lines in traverse_tests_directories('smelly_tests'):
        current_test_name, current_test_lines = None, []
        for line_number, line in enumerate(lines):
            line = line.strip('\n')
            if line.startswith('def test_'):
                current_test_name = re.search('def (.*)\\(', line).group(1)
            if current_test_name:
                if '    ' in line or line.startswith('def test_'):
                    current_test_lines.append(line.strip())
                    if line_number == len(lines) - 1:  # eof
                        yield current_test_name, current_test_lines
                else:
                    yield current_test_name, current_test_lines
                    current_test_name, current_test_lines = None, []
