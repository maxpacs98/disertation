from constants import CONTROL_STATEMENTS
from utils import is_assertion, get_assertion_method, starts_try_block, get_try_except_block, is_sleep


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
        assertion_method = get_assertion_method(line, current_test_lines)
        if is_assertion(line):
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
            try_except_block = get_try_except_block(idx, current_test_lines)
            try_except_blocks = [*try_except_blocks, *try_except_block]
    return try_except_blocks


def check_sleepy_test(current_test_lines):
    sleep_lines = []
    for line in current_test_lines:
        if is_sleep(line):
            sleep_lines.append(line)
    return sleep_lines
