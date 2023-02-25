import json
import pytest
from gistapi import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_search_valid_input(client):
    valid_input = {
        "username": "testuser",
        "pattern": "test",
        "page": 1,
        "limit": 10,
        "include_file_info": False,
    }
    response = client.post(
        "/api/v1/search",
        data=json.dumps(valid_input),
        content_type="application/json",
    )
    assert response.status_code == 200
    assert response.json["status"] == "success"
    assert response.json["username"] == valid_input["username"]
    assert response.json["pattern"] == valid_input["pattern"]


def test_search_invalid_input(client):
    invalid_input = {
        "username": "",
        "pattern": "test",
        "page": 1,
        "limit": 10,
        "include_file_info": False,
    }
    response = client.post(
        "/api/v1/search",
        data=json.dumps(invalid_input),
        content_type="application/json",
    )
    assert response.status_code == 400
    assert response.json["status"] == "error"
