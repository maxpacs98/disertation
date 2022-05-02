TESTS_DIRECTORY = 'flask_tests'

# TODO: Move this maybe to a universal config
# TODO: Add proper explanation messages
SMELL_INFO_MAPPING = {
    'assertion_roulette': {
        'display_name': 'Assertion Roullete',
        'metric_threshold': 1,
        'reversed_metric': False,
        'explanation_message': 'Test has %d undocumented asserts:',
        'check_annotations': False
    },
    'duplicate_assert': {
        'display_name': 'Duplicate Assert',
        'metric_threshold': 0,
        'reversed_metric': False,
        'explanation_message': 'Test has %d duplicate assert(s):',
        'check_annotations': False
    },
    'eager_test': {
        'display_name': 'Eager Test',
        'metric_threshold': 1,
        'reversed_metric': False,
        'explanation_message': 'Test has %d methods tested:',
        'check_annotations': False
    },
    'conditional_logic': {
        'display_name': 'Conditional Logic',
        'metric_threshold': 0,
        'reversed_metric': False,
        'explanation_message': 'Test has %d control flow statement(s):',
        'check_annotations': False
    },
    'exception_handling': {
        'display_name': 'Exception Handling',
        'metric_threshold': 0,
        'reversed_metric': False,
        'explanation_message': 'Test is passed or failed upon %d method(s) explicitly throwing an exception:',
        'check_annotations': False
    },
    'sleepy_test': {
        'display_name': 'Sleepy Test',
        'metric_threshold': 0,
        'reversed_metric': False,
        'explanation_message': 'Test has %d sleep methods:',
        'check_annotations': False
    },
    'redundant_print': {
        'display_name': 'Redundant Print',
        'metric_threshold': 0,
        'reversed_metric': False,
        'explanation_message': 'Test has %d print methods:',
        'check_annotations': False
    },
    'ignored_test': {
        'display_name': 'Ignored Test',
        'metric_threshold': 0,
        'reversed_metric': False,
        'explanation_message': 'Test will not be executed due to the %d skip annotation:',
        'check_annotations': True
    },
    'unknown_test': {
        'display_name': 'Unknown Test',
        'metric_threshold': 1,
        'reversed_metric': True,
        'explanation_message': 'Test has to have at least 1 assertion statements, while it has %d',
        'check_annotations': True
    },
    'magic_number': {
        'display_name': 'Magic Number',
        'metric_threshold': 0,
        'reversed_metric': False,
        'explanation_message': 'Test has %d assertions which contain numeric literals',
        'check_annotations': False
    },
}
