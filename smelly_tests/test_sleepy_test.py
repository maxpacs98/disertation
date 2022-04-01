from time import sleep

from smelly_tests.implementation_mock import decrement, increment


def test_increment__suffers_from_exception_handling():
    sleep(1)
    assert increment(1) == 2, 'One incremented with one is 2'


def test_decrement__healthy():
    assert decrement(1) == 0
