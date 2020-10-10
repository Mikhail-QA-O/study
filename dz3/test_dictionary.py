import pytest


@pytest.mark.parametrize('list_one, result', [
    pytest.param(
        dict(a=1, b=2), {},
        id='test_one'

    ),
    pytest.param(
        dict(s=2, b=10), {},
        id='test_two'
    ),
])
def test_parametrize(list_one, result):
    list_one.clear()
    assert list_one == result


def test_dict_1():
    a = dict(a=1, b=2, c=3)
    a.clear()
    assert a == {}


def test_dict_2():
    a = {
        1: 'one',
        2: 'two',
        3: 'three',
    }
    assert a.get(1) == 'one'


def test_dict_3():
    a = {
        1: 'one',
        2: 'two',
        3: 'three',
    }
    a.pop(2)
    assert a == {1: 'one', 3: 'three'}


def test_dict_4():
    a = {
        1: 'one',
        2: 'two',
        3: 'three',
    }
    assert a.copy() == {1: 'one', 2: 'two', 3: 'three'}
