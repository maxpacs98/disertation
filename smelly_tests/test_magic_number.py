from smelly_tests.implementation_mock import increment


def test_increment__suffers_from_eager_test():
    assert increment(1) == 2, 'One added with one is two'
