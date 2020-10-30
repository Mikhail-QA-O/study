import pytest


@pytest.mark.parametrize('list_one, result', [
    pytest.param(
        [1, 4], [4],
        id='test_one'

    ),
    pytest.param(
        [1, 2], [2],
        id='test_two'
    ),
])
def test_list_parametrize(list_one, result):
    list_one.remove(1)
    assert list_one == result


def test_list_1():
    a = [1, 2]
    a.clear()
    assert a == []


def test_list_2():
    a = [1, 2, 3, 4]
    a.remove(3)
    assert a == [1, 2, 4]


def test_list_3():
    a = [10, 20]
    b = [50, 100]
    a.extend(b)
    assert a == [10, 20, 50, 100]


def test_list_4():
    a = [9, 8]
    a.insert(0, 1)
    assert a == [1, 9, 8]
