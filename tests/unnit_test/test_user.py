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
    return User(fake.name(), fake.password())

class TestStringMethods():

    def test_valid_user(self,test_user):
        assert test_user.username
        assert test_user.password
        assert " " in test_user.username
        assert not test_user.is_valid()

        test_user.username = None
        assert not test_user.is_valid()

        test_user.password = None
        assert not test_user.is_valid()

        test_user.password = ""
        assert not test_user.is_valid() 

    

        
        