import requests


url = 'https://reqres.in/api/'


def test_requested_page_number():
    page = 2
    response = requests.get(f'{url}users', params={"page": page})

    assert response.status_code == 200
    assert response.json()["page"] == page


def test_users_list_default_length():
    default_users_count = 6

    response = requests.get(f'{url}users')

    assert len(response.json()["data"]) == default_users_count


def test_single_user_not_found():
    response = requests.get(f'{url}users/23')

    assert response.status_code == 404
    assert response.text == "{}"


def test_create_user():
    name = "Kate"
    job = "leader"

    response = requests.post(f'{url}users', json={"name": name, "job": job})

    assert response.status_code == 201
    assert response.json()["name"] == name
    assert response.json()["job"] == job


def test_delete_user_returns_204():
    response = requests.delete(f'{url}users/2')

    assert response.status_code == 204
    assert response.text == ""


def test_update_user():
    name = "Kate"
    job = "leader"

    response = requests.put(f'{url}users/2', json={"name": name, "job": job})

    assert response.status_code == 200
    assert response.json()["name"] == name
    assert response.json()["job"] == job


def test_user_register_successful():
    email = "eve.holt@reqres.in"
    password = "pistol"

    response = requests.post(
        f'{url}register', json={"email": email, "password": password}
    )

    assert response.status_code == 200
    assert response.json()["token"] == 'QpwL5tke4Pnpja7X4'


def test_user_register_unsuccessful():
    email = "sydney@fife"

    response = requests.post(
        f'{url}register', json={"email": email}
    )

    assert response.status_code == 400
    assert response.text == '{"error":"Missing password"}'


def test_users_list():
    response = requests.get(f'{url}users?page=1')

    assert response.status_code == 200
    assert response.json()['per_page'] == 6
    assert response.json()['total'] == 12


def test_login_successful():
    email = "eve.holt@reqres.in"
    password = "pistol"

    response = requests.post(f'{url}login', json={"email": email, "password": password})

    assert response.status_code == 200
    assert response.json()["token"] != ''
