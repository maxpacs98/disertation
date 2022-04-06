import pytest

from smelly_tests.implementation_mock import increment, increment_integer


def test_increment_integer__suffers_from_exception_handling():
    try:
        assert increment(1) == 2, 'One incremented with one is 2'
        assert increment_integer(1.2) == 2.2
    except Exception:
        pass


def test_increment_integer__healthy():
    with pytest.raises(Exception):
        assert increment_integer(1.2) == 2.2
