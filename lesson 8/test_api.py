import requests
import pytest
import time

url1 = 'https://jsonplaceholder.typicode.com/'
url2 = 'https://playground.learnqa.ru/api/'
HTTP_code_OK = 200
HTTP_code_OK2 = 201


def test_get_all_posts():
    response = requests.get(f'{url1}posts')
    assert response.status_code == HTTP_code_OK, 'wrong code'
    assert len(response.json()) == 100, 'actual length does not match to expected'


def test_get_1st_post():
    response = requests.get(f'{url1}posts/1')
    assert response.status_code == HTTP_code_OK, 'wrong code'
    response_data = response.json()
    expected_keys = ['userId', 'id', 'title', 'body']
    for key in response_data.keys():
        assert key in expected_keys, 'wrong key'


def test_post_in_posts():
    post_data = {
        'id': 101,
        'title': 'test title',
        'body': 'test body'
    }
    response = requests.post(f'{url1}posts', data=post_data)
    assert response.status_code == HTTP_code_OK2, 'wrong code'
    response_data = response.json()
    expected_title = 'test title'
    assert response_data['title'] == expected_title, 'wrong title'
