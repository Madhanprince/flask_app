# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_get_todos(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_add_todo(client):
    response = client.post("/todos", json={"task": "Write CI/CD"})
    assert response.status_code == 201
    assert response.get_json()["task"] == "Write CI/CD"
