# tests/conftest.py
import pytest
import sys
sys.path.append("C:/Users/tiennt/Desktop/code lab/flask-login")
from app import app as _app, User
from faker import Faker
fake = Faker()


@pytest.fixture
def client():
    with _app.test_client() as client:
        with _app.app_context():
            yield client


def test_get_users(client):
    result = client.get("/users")
    assert result.status_code == 200
    response = result.json
    assert type(response) is list
    assert len(response) == User.query.count()
    if response:
        render_user = response[0]
        assert "username" in render_user
        assert "password" in render_user