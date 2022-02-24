def increment(x):
    return x + 1


def decrement(x):
    return x - 1


def test_increment_suffers__from_assertion_roullete():
    assert increment(1) == 2, 'One added with one is two'
    assert increment(2) == 3
    assert increment(3) == 4


def test_decrement__healthy():
    assert decrement(1) == 0
