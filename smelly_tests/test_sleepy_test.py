from time import sleep

from smelly_tests.implementation_mock import increment


def test_increment__suffers_from_exception_handling():
    sleep(1)
    assert increment(1) == 2, 'One incremented with one is 2'
