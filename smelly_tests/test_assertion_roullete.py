from smelly_tests.implementation_mock import increment, decrement


def test_increment_suffers__from_assertion_roullete():
    assert increment(1) == 2, 'One added with one is two'
    assert increment(2) == 3
    assert increment(3) == 4


def test_decrement__healthy():
    assert decrement(1) == 0


def test_duplicate_decrement__healthy():
    assert decrement(1) == 0, 'One subtracted with one is 0'
    assert decrement(2) == 1, 'Two subtracted with one is 1'
