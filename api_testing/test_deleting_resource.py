def test_remove_user_2(session, base_url):
    delete_user_2 = session.delete(base_url + '2')
    assert delete_user_2.status_code == 200
    assert not delete_user_2.json()
