from api_testing.credentials import CredentialUpdating


def test_update_user_199(session, base_url):
    update_user_10 = session.put(base_url + '199', json=CredentialUpdating.user_199)
    assert update_user_10.status_code == 200
    assert dict(update_user_10.json()).get('id') == 199


def test_update_user_201(session, base_url):
    update_user_201 = session.put(base_url + '201', json=CredentialUpdating.user_201)
    assert update_user_201.status_code == 500


def test_update_title_user_10(session, base_url):
    update_title = session.patch(base_url + '10', json=CredentialUpdating.new_title)
    assert update_title.status_code == 200
    assert dict(update_title.json()).get('title') == '123'
