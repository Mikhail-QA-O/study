import pytest
from schemas.data_preparation import ValidationJsonSchemas


@pytest.mark.parametrize('todo_id', [1, 200])
def test_get_todo(session, base_url, todo_id):
    res = session.get(base_url + str(todo_id))
    assert res.status_code == 200
    assert res.json()['id'] == todo_id
    ValidationJsonSchemas.checking_json_schema(url=res)


@pytest.mark.parametrize('todo_id', [-1, 0, 201])
def test_invalid_ids(session, base_url, todo_id):
    invalid_ids = session.get(base_url + str(todo_id))
    assert invalid_ids.status_code == 404
    assert len(invalid_ids.json()) == 0
