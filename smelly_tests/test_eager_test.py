from smelly_tests.implementation_mock import increment, decrement


def test_increment_and_decrement__suffers_from_eager_test():
    assert increment(1) == 2, 'One added with one is two'
    assert decrement(1) == 0, 'One subtracted with one is 0'


def test_increment_and_decrement_with_variables__suffers_from_eager_test():
    incremented_value = increment(1)
    assert incremented_value == 2, 'One added with one is two'
    decremented_value = decrement(1)
    assert decremented_value == 0, 'One subtracted with one is 0'


def test_decrement__healthy():
    assert decrement(1) == 0


def test_increment__healthy():
    incremented_value = increment(1)
    assert incremented_value == 2, 'One added with one is two'
    other_incremented_value = increment(2)
    assert other_incremented_value == 3, 'Two added with one is three'
