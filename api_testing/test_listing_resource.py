from schemas.data_preparation import ValidationJsonSchemas


def test_get_all_data(session, base_url):
    get_all_data = session.get(base_url)
    assert get_all_data.status_code == 200
    ValidationJsonSchemas.checking_json_schema_array(url=get_all_data)
