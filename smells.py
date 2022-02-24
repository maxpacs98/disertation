from utils import is_assertion


def check_assertion_roulette(current_test_lines):
    assert_with_no_explanation_count = 0
    for line in current_test_lines:
        if is_assertion(line) and len(line.split(',')) == 1:
            assert_with_no_explanation_count += 1
    return assert_with_no_explanation_count > 1, assert_with_no_explanation_count
