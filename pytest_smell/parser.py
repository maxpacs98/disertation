import os
import re

from pytest_smell.utils import is_annotation


def traverse_tests_directories(root_path):
    for dir_path, _, files in os.walk(root_path):
        if '__pycache__' in dir_path:
            continue
        for filename in files:
            file_path = os.path.join(dir_path, filename)
            if (filename.startswith('test') and filename.endswith('.py')) or filename.endswith('test.py'):
                with open(file_path) as test_file:
                    yield file_path, test_file.readlines()


def traverse_tests_file(tests_directory, with_annotations=False):
    for file_path, lines in traverse_tests_directories(tests_directory):
        current_test_name, current_test_lines, current_test_annotations = None, [], []
        for line_number, line in enumerate(lines):
            line = line.strip('\n')
            if line.startswith('def test_'):
                current_test_name = re.search('def (.*)\\(', line).group(1)
            elif with_annotations and is_annotation(line, '@pytest'):
                current_test_annotations.append(line.strip())
            if current_test_name:
                if '    ' in line or line.startswith('def test_'):
                    current_test_lines.append(line.strip())
                    if line_number == len(lines) - 1:  # eof
                        test_lines = current_test_lines if not with_annotations else [*current_test_annotations,
                                                                                      *current_test_lines]
                        yield file_path, current_test_name, test_lines, line_number - len(current_test_lines)
                else:
                    next_two_lines_are_empty = not any([line, lines[line_number + 1].strip()])
                    if next_two_lines_are_empty:
                        test_lines = current_test_lines if not with_annotations else [*current_test_annotations,
                                                                                      *current_test_lines]
                        yield file_path, current_test_name, test_lines, line_number - len(current_test_lines)
                        current_test_name, current_test_lines, current_test_annotations = None, [], []
