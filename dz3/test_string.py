import pytest


@pytest.mark.parametrize('list_one, result', [
    pytest.param(
        'pupil', 'PUPIL',
        id='test_one'

    ),
    pytest.param(
        'student', 'STUDENT',
        id='test_two'
    ),
])
def test_string_parametrize(list_one, result):
    a = list_one.upper()
    assert a == result


def test_string_1():
    a = 'otus'.upper()
    assert a == 'OTUS'


def test_string_2():
    a = 'OTUS'.lower()
    assert a == 'otus'


def test_string_3():
    a = 'big live'.count('i')
    assert a == 2


def test_string_4():
    a = 'big live'.find('li')
    assert a == 4
