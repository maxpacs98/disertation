import smells
from parser import traverse_tests_file

# TODO: Move this maybe to a universal config
# TODO: Add proper explanation messages
SMELL_INFO_MAPPING = {
    'assertion_roulette': {
        'display_name': 'Assertion Roullete',
        'metric_threshold': 1,
        'explanation_message': 'Test has %d undocumented asserts'
    },
    'duplicate_assert': {
        'display_name': 'Duplicate Assert',
        'metric_threshold': 0,
        'explanation_message': 'Test has %d duplicate assert(s)'
    },
    'eager_test': {
        'display_name': 'Eager Test',
        'metric_threshold': 1,
        'explanation_message': 'Test has %d methods tested'
    },
    'conditional_logic': {
        'display_name': 'Conditional Logic',
        'metric_threshold': 0,
        'explanation_message': 'Test has %d control flow statement(s)'
    },
    'exception_handling': {
        'display_name': 'Exception handling',
        'metric_threshold': 0,
        'explanation_message': 'Test is passed or failed upon %d method(s) explicitly throwing an exception'
    },
    'sleepy_test': {
        'display_name': 'Sleepy Test',
        'metric_threshold': 0,
        'explanation_message': 'Test has %d sleep methods'
    },
}


def detect_smells():
    for current_test_name, current_test_lines in traverse_tests_file():
        is_smelly = False
        for smell_code, smell_info in SMELL_INFO_MAPPING.items():
            smell_handler = getattr(smells, f'check_{smell_code}')
            handler_result = smell_handler(current_test_lines)
            suffers_of_smell = len(handler_result) > smell_info['metric_threshold']
            if suffers_of_smell:
                is_smelly = True
                test_smell_message = f'Test {current_test_name} suffers from "{smell_info["display_name"]}". ' \
                                     f'Explanation: {smell_info["explanation_message"] % len(handler_result)}:'
                print(test_smell_message)
                print("\n".join(handler_result))
        if is_smelly:
            print('\n')
