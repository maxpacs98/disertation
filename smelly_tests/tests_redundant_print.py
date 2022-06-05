from smelly_tests.implementation_mock import increment


def test_increment__suffers_from_redundant_print():
    number = 1
    print(number)
    assert increment(number) == 2
