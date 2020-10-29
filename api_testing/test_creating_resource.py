from api_testing.credentials import CredentialsCreating


def test_creating_resource(session, base_url):
    creating_resource = session.post(base_url,
                                     json=CredentialsCreating.valid_data)
    assert creating_resource.status_code == 201
    r_json = creating_resource.json()
    assert r_json['userId'] == CredentialsCreating.valid_data['userId']
    assert r_json['id'] == CredentialsCreating.valid_data['id']
    assert r_json['title'] == CredentialsCreating.valid_data['title']
    assert r_json['completed'] == CredentialsCreating.valid_data['completed']


def test_creating_invalid_data(session, base_url):
    creating_invalid_data = session.post(base_url,
                                         json=CredentialsCreating.invalid_data)
    assert creating_invalid_data.status_code == 500
