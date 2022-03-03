from smelly_tests.implementation_mock import increment


def test_increment_with_for_suffers__from_conditional_logic():
    for i in range(10):
        assert increment(i) == i + 1


def test_increment_with_if_suffers__from_conditional_logic():
    external_condition = True
    if external_condition:
        assert increment(1) == 2
    else:
        assert increment(int(external_condition)) == 2


def test_increment_first_condition__healthy():
    assert increment(1) == 2


def test_increment_second_condition__healthy():
    external_condition = True
    assert increment(int(external_condition)) == 2
