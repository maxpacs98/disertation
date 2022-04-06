import smells
from parser import traverse_tests_file

# TODO: Move this maybe to a universal config
# TODO: Add proper explanation messages
SMELL_INFO_MAPPING = {
    # 'assertion_roulette': {
    #     'display_name': 'Assertion Roullete',
    #     'metric_threshold': 1,
    #     'reversed_metric': False,
    #     'explanation_message': 'Test has %d undocumented asserts:',
    #     'check_annotations': False
    # },
    # 'duplicate_assert': {
    #     'display_name': 'Duplicate Assert',
    #     'metric_threshold': 0,
    #     'reversed_metric': False,
    #     'explanation_message': 'Test has %d duplicate assert(s):',
    #     'check_annotations': False
    # },
    # 'eager_test': {
    #     'display_name': 'Eager Test',
    #     'metric_threshold': 1,
    #     'reversed_metric': False,
    #     'explanation_message': 'Test has %d methods tested:',
    #     'check_annotations': False
    # },
    # 'conditional_logic': {
    #     'display_name': 'Conditional Logic',
    #     'metric_threshold': 0,
    #     'reversed_metric': False,
    #     'explanation_message': 'Test has %d control flow statement(s):',
    #     'check_annotations': False
    # },
    # 'exception_handling': {
    #     'display_name': 'Exception Handling',
    #     'metric_threshold': 0,
    #     'reversed_metric': False,
    #     'explanation_message': 'Test is passed or failed upon %d method(s) explicitly throwing an exception:',
    #     'check_annotations': False
    # },
    # 'sleepy_test': {
    #     'display_name': 'Sleepy Test',
    #     'metric_threshold': 0,
    #     'reversed_metric': False,
    #     'explanation_message': 'Test has %d sleep methods:',
    #     'check_annotations': False
    # },
    # 'redundant_print': {
    #     'display_name': 'Redundant Print',
    #     'metric_threshold': 0,
    #     'reversed_metric': False,
    #     'explanation_message': 'Test has %d print methods:',
    #     'check_annotations': False
    # },
    # 'ignored_test': {
    #     'display_name': 'Ignored Test',
    #     'metric_threshold': 0,
    #     'reversed_metric': False,
    #     'explanation_message': 'Test will not be executed due to the %d skip annotation:',
    #     'check_annotations': True
    # },
    'unknown_test': {
        'display_name': 'Unknown Test',
        'metric_threshold': 1,
        'reversed_metric': True,
        'explanation_message': 'Test has to have at least 1 assertion statements, while it has %d',
        'check_annotations': False
    },
    'magic_number': {
        'display_name': 'Magic Number',
        'metric_threshold': 0,
        'reversed_metric': False,
        'explanation_message': 'Test has %d assertions which contain numeric literals',
        'check_annotations': False
    },
}


def detect_smells():
    total_smell_count, total_test_count = 0, 0
    for smell_code, smell_info in SMELL_INFO_MAPPING.items():
        is_smelly = False
        for current_test_name, current_test_lines in traverse_tests_file(smell_info.get('check_annotations')):
            total_test_count += 1
            smell_handler = getattr(smells, f'check_{smell_code}')
            handler_result = smell_handler(current_test_lines)
            if not smell_info.get('reversed_metric'):
                suffers_of_smell = len(handler_result) > smell_info['metric_threshold']
            else:
                suffers_of_smell = len(handler_result) < smell_info['metric_threshold']
            if suffers_of_smell:
                total_smell_count += 1
                is_smelly = True
                test_smell_message = f'Test {current_test_name} suffers from "{smell_info["display_name"]}". ' \
                                     f'Explanation: {smell_info["explanation_message"] % len(handler_result)}'
                print(test_smell_message)
                if handler_result:
                    print("\n".join(handler_result))
        if is_smelly:
            print('\n')
    print(f'The total number of bad smells detected in the test suite containing '
          f'{total_test_count // len(SMELL_INFO_MAPPING.keys())} tests was: {total_smell_count}')
