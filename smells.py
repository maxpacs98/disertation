from constants import CONTROL_STATEMENTS
from utils import is_assertion, get_assertion_method


def check_assertion_roulette(current_test_lines):
    assert_with_no_explanation_count = 0
    for line in current_test_lines:
        if is_assertion(line) and len(line.split(',')) == 1:
            assert_with_no_explanation_count += 1
    return assert_with_no_explanation_count > 1, assert_with_no_explanation_count


def check_duplicate_assert(current_test_lines):
    seen = set()
    duplicate_assertions = [line for line in current_test_lines if
                            is_assertion(line) and line in seen or seen.add(line)]
    return len(duplicate_assertions) > 0, duplicate_assertions


def check_eager_test(current_test_lines):
    distinct_assertion_methods = set()
    for line in current_test_lines:
        assertion_method = get_assertion_method(line, current_test_lines)
        if is_assertion(line):
            distinct_assertion_methods.add(assertion_method)
    return len(distinct_assertion_methods) > 1, distinct_assertion_methods


def check_conditional_logic(current_test_lines):
    distinct_conditional_statements = set()
    for line in current_test_lines:
        for statement in CONTROL_STATEMENTS:
            if statement in line:
                distinct_conditional_statements.add(statement)
    return len(distinct_conditional_statements) > 0, distinct_conditional_statements
