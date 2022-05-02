from pytest_smell.constants import CONTROL_STATEMENTS
from pytest_smell.utils import is_assertion, get_assertion_method, starts_try_block, is_sleep, is_annotation, \
    is_print, contains_numeric_literals


def check_assertion_roulette(current_test_lines):
    asserts_with_no_explanation = []
    for line in current_test_lines:
        if is_assertion(line) and len(line.split(',')) == 1:
            asserts_with_no_explanation.append(line)
    return asserts_with_no_explanation


def check_duplicate_assert(current_test_lines):
    seen = set()
    duplicate_assertions = [line for line in current_test_lines if
                            is_assertion(line) and line in seen or seen.add(line)]
    return duplicate_assertions


def check_eager_test(current_test_lines):
    distinct_assertion_methods = set()
    for line in current_test_lines:
        if is_assertion(line):
            assertion_method = get_assertion_method(line, current_test_lines)
            if assertion_method:
                distinct_assertion_methods.add(assertion_method)
    return distinct_assertion_methods


def check_conditional_logic(current_test_lines):
    distinct_conditional_statements = set()
    for line in current_test_lines:
        for statement in CONTROL_STATEMENTS:
            if statement in line:
                distinct_conditional_statements.add(statement)
    return distinct_conditional_statements


def check_exception_handling(current_test_lines):
    try_except_blocks = list()
    for idx, line in enumerate(current_test_lines):
        if starts_try_block(line):
            try_except_blocks.append(line)
            # TODO: Add these back if there is a separation of metric count from display lines
            # try_except_block = get_try_except_block(idx, current_test_lines)
            # try_except_blocks = [*try_except_blocks, *try_except_block]
    return try_except_blocks


def check_sleepy_test(current_test_lines):
    sleep_lines = []
    for line in current_test_lines:
        if is_sleep(line):
            sleep_lines.append(line)
    return sleep_lines


def check_redundant_print(current_test_lines):
    print_lines = []
    for line in current_test_lines:
        if is_print(line):
            print_lines.append(line)
    return print_lines


def check_ignored_test(current_test_lines_with_annotations):
    for line in current_test_lines_with_annotations:
        if is_annotation(line, '@pytest.mark.skip(') or is_annotation(line, '@skip'):
            return [line]
    return []


def check_unknown_test(current_test_lines_with_annotations):
    assert_lines = []
    for line in current_test_lines_with_annotations:
        if is_annotation(line, '@pytest.fixture'):  # means it is a test fixture not a test
            return ['dummy_assert']  # TODO: Improve this
        if is_assertion(line) or is_annotation(line, 'with pytest') or is_annotation(line, 'pytest') or \
                is_annotation(line, 'with warnings'):
            assert_lines.append(line)
    return assert_lines


def check_magic_number(current_test_lines):
    assert_with_magic_numbers_lines = []
    for line in current_test_lines:
        if is_assertion(line) and contains_numeric_literals(line):
            assert_with_magic_numbers_lines.append(line)
    return assert_with_magic_numbers_lines
