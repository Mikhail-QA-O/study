import pytest


@pytest.mark.parametrize('wrong_value', [
    '?userId=300',
    '?id=300',
    '?title=otus',
    '?completed=NONE'

])
def test_filter_invalid_value_key(session, base_url, wrong_value):
    filter_invalid_value_key = session.get(base_url + wrong_value)
    assert filter_invalid_value_key.status_code == 200
    assert not filter_invalid_value_key.json()


@pytest.mark.parametrize('field, value', [
    ('userId', 1),
    ('id', 1),
    ('title', 'delectus aut autem'),
    ('completed', False),
    ('completed', True)
])
def test_filter_user_id_1(session, base_url, field, value):
    str_val = str(value).lower() if isinstance(value, bool) else str(value)
    filter_user_id_1 = session.get(base_url,
                                   params={field: str_val})
    assert filter_user_id_1.status_code == 200
    j_res = filter_user_id_1.json()
    assert len(j_res) > 0
    for x in j_res:
        assert x[field] == value
