import pytest


@pytest.mark.parametrize('list_one, result', [
    pytest.param(
        {1, 2, 3}, {1, 2, 3, 4, 6},
        id='test_one'

    ),
    pytest.param(
        {1, 2, 3}, {1, 2, 3, 4, 6},
        id='test_two'
    ),
])
def test_parametrize(list_one, result):
    a = {4, 6}
    b = list_one.union(a)
    assert b == {1, 2, 3, 4, 6}


def test_set_1():
    a = {1, 2, 3}
    b = {4, 6}
    c = a.union(a, b)
    assert c == {1, 2, 3, 4, 6}


def test_set_2():
    a = {1, 2, 3}
    b = {14, 3, 11}
    c = a.intersection(a, b)
    assert c == {3}


def test_set_3():
    a = {1, 5, 9}
    b = {5, 9, 10}
    c = a.difference(b)
    assert c == {1}


def test_set_4():
    a = {1, 5, 9}
    b = {5, 9, 10}
    c = a.symmetric_difference(b)
    assert c == {1, 10}
