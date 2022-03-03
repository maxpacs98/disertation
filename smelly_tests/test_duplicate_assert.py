from smelly_tests.implementation_mock import increment, decrement


def test_increment_suffers__from_duplicate_assert():
    assert increment(1) == 2, 'One added with one is two'
    assert increment(2) == 3, 'One added with one is two'
    assert increment(1) == 2, 'One added with one is two'


def test_decrement__healthy():
    assert decrement(1) == 0
