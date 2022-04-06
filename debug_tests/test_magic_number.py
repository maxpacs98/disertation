from smelly_tests.implementation_mock import increment


def test_increment__suffers_from_magic_number():
    assert increment(1) == 2


def test_increment__healthy():
    expected_value = 2
    assert increment(1) == expected_value, 'One added with one is two'
