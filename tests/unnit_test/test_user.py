"""
An example test case with unittest.
"""
import unittest
import sys
sys.path.append("C:/Users/tiennt/Desktop/code lab/flask-login")
from app import User
import pytest
from faker import Faker
fake = Faker()


@pytest.fixture
def test_user():
    return User( fake.profile(fields=['username'])['username'], fake.password())


def test_valid_user(test_user):

    assert test_user.username
    assert test_user.password
    assert test_user.is_valid()

    test_user.username = fake.name()
    assert " " in test_user.username
    assert not test_user.is_valid()

    test_user.username = None
    assert not test_user.is_valid()

    test_user.password = None
    assert not test_user.is_valid()

    test_user.password = ""
    assert not test_user.is_valid() 

    

        
        