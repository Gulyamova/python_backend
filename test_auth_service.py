import pytest
from fastapi.testclient import TestClient
from auth_service import app

client = TestClient(app)


def test_authenticate_user():
    response = client.post("/authenticate/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "User authenticated"
