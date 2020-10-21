from api_testing.credentials import CredentialsCreating


def test_creating_resource(session, base_url):
    creating_resource = session.post(base_url, json=CredentialsCreating.valid_data)
    assert creating_resource.status_code == 201


def test_creating_invalid_data(session, base_url):
    reating_invalid_data = session.post(base_url, json=CredentialsCreating.invalid_data)
    assert reating_invalid_data.status_code == 500
