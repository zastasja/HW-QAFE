import requests
import pytest
import time

url = 'https://playground.learnqa.ru/api/'
HTTP_code_OK = 200
HTTP_code_OK2 = 201


def test_end_to_end():
    new_user = {
        "username": "test user",
        "firstName": "TestName",
        "lastName": "TestSurname",
        "email": str(time.time())+"@example.com",
        "password": "password12345"
    }

    response = requests.post(f'{url}user', data=new_user)
    assert response.status_code == HTTP_code_OK, 'wrong status code'
    response_data = response.json()
    assert 'id' in response_data.keys()
    user_id = response_data['id']

    response = requests.get(f'{url}user/{user_id}')
    assert response.status_code == HTTP_code_OK, 'wrong status code'

    auth_data = {
        'email': new_user['email'],
        'password': 'password12345'
    }

    response = requests.post(f'{url}user/login', data=auth_data)
    assert response.status_code == HTTP_code_OK, 'wrong status code'
    token = response.headers['x-csrf-token']
    auth_sid = response.cookies['auth_sid']

    new_user_update = {
        'username': 'updated test body'
    }

    response = requests.put(f'{url}user/{user_id}',
                            data=new_user_update,
                            headers={'x-csrf-token': token},
                            cookies={'auth_sid': auth_sid})
    assert response.status_code == HTTP_code_OK, 'wrong status code'

    response = requests.get(f'{url}user/{user_id}')
    assert response.status_code == HTTP_code_OK, 'wrong status code'

    response_data = response.json()
    assert 'updated test body' in response_data.values()

    response = requests.delete(f'{url}user/{user_id}',
                               data=new_user_update,
                               headers={'x-csrf-token': token},
                               cookies={'auth_sid': auth_sid})

    response = requests.get(f'{url}user/{user_id}')
    assert response.status_code == 404, 'wrong status code'
