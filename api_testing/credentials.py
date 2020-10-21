class CredentialsCreating:
    valid_data = {
        "userId": 10,
        "id": 201,
        "title": "Create one",
        "completed": False,
    }

    invalid_data = ''


class CredentialUpdating:
    user_199 = {
        "userId": 199,
        "id": 199,
        "title": "199",
        "completed": True,
    }

    user_201 = {
        "userId": 199,
        "id": 199,
        "title": "199",
        "completed": True,
    }

    new_title = {
        'title': '123'
    }


class CredentialsFiltering:
    user_id_1 = {
        'userId': 1
    }
