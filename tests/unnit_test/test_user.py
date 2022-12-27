"""
An example test case with unittest.
"""
import sys
sys.path.append("C:/Users/tiennt/Desktop/code lab/flask-login")

from unittest.mock import patch, MagicMock
from app import insert_user_from_out_side, app, User
from time import sleep
from faker import Faker
import pytest
import unittest
fake = Faker()


@pytest.fixture
def test_user():
    return User(fake.profile(fields=['username'])['username'], fake.password())


@pytest.fixture
def test_user_json():
    return {"results": [{"login": {"username": fake.profile(fields=['username'])['username'], "password": fake.password()}}]}


# def test_valid_user(test_user):

#     assert test_user.username
#     assert test_user.password
#     assert test_user.is_valid()

#     test_user.username = fake.name()
#     assert " " in test_user.username
#     assert not test_user.is_valid()

#     test_user.username = None
#     assert not test_user.is_valid()

#     test_user.password = None
#     assert not test_user.is_valid()

#     test_user.password = ""
#     assert not test_user.is_valid()
#     sleep(1)

def test_insert_user_from_other_api(test_user_json):
    with app.app_context():
        total_users = User.query.count()
        with patch('app.requests', autospec=True) as mock_request:
            with patch('app.db', autospec=True):
                response = MagicMock()
                response.json
                response.json.return_value = test_user_json
                mock_request.get.return_value = response
                users = insert_user_from_out_side()
                assert len(users) == len(test_user_json["results"])
                assert users[0] 
                assert users[0].username
                assert users[0].password
        assert User.query.count() == total_users
