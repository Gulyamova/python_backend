import pytest
from fastapi.testclient import TestClient
from main_service import app

client = TestClient(app)
AUTH_SERVICE_URL = "http://localhost:8002"


def test_create_order():
    item = {"name": "Krabby Patty burger", "description": "secret recipe"}
    response = client.post("/create_order/", json=item)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Order created"
    assert data["item"] == item
