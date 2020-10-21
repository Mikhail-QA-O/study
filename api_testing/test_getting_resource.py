from schemas.data_preparation import ValidationJsonSchemas


def test_get_user_1(session, base_url):
    get_user_1 = session.get(base_url + '1')
    assert get_user_1.status_code == 200
    ValidationJsonSchemas.checking_json_schema(url=get_user_1)


def test_get_invalid_data(session, base_url):
    get_invalid_data = session.get(base_url + '0')
    assert get_invalid_data.status_code == 404
