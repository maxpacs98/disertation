import pytest as pytest

from smelly_tests.implementation_mock import increment


@pytest.mark.skip(reason="Test fails randomly - flaky test")
def test_increment__suffers_from_ignored_test():
    assert increment(1) == 2, 'One added with one is two'
