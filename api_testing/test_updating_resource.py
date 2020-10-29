import pytest
from api_testing.credentials import CredentialUpdating


def test_update_user_199(session, base_url):
    update_user_10 = session.put(base_url + '199',
                                 json=CredentialUpdating.user_199)
    assert update_user_10.status_code == 200
    assert dict(update_user_10.json()).get('id') == 199
    r_json = update_user_10.json()
    assert r_json['userId'] == CredentialUpdating.user_199['userId']
    assert r_json['id'] == CredentialUpdating.user_199['id']
    assert r_json['title'] == CredentialUpdating.user_199['title']
    assert r_json['completed'] == CredentialUpdating.user_199['completed']


def test_update_user_201(session, base_url):
    update_user_201 = session.put(base_url + '201',
                                  json=CredentialUpdating.user_201)
    assert update_user_201.status_code == 500


@pytest.mark.parametrize('field, value', [
    ('id', 11),
    ('userId', 10),
    ('title', '123'),
    ('completed', False),
    ('completed', True),
])
def test_update_title_user_10(session, base_url, field, value):
    update_title = session.patch(base_url + '10',
                                 json={field: value})
    assert update_title.status_code == 200
    assert update_title.json()[field] == value
