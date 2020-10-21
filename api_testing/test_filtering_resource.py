import pytest
from api_testing.credentials import CredentialsFiltering


@pytest.mark.parametrize('wrong_value, result', [
    pytest.param(
        ('?userId=300'), [],
        id='userid'
    ),
    pytest.param(
        ('?id=300'), [],
        id='id'
    ),
    pytest.param(
        ('?title=otus'), [],
        id='title'
    ),
    pytest.param(
        ('?completed=NONE'), [],
        id='completed'
    ),

])
def test_filter_invalid_value_key(session, base_url, wrong_value, result):
    filter_invalid_value_key = session.get(base_url + wrong_value)
    assert filter_invalid_value_key.status_code == 200
    assert filter_invalid_value_key.json() == result


def test_filter_user_id_1(session, base_url):
    filter_user_id_1 = session.get(base_url, params=CredentialsFiltering.user_id_1)
    assert filter_user_id_1.status_code == 200
