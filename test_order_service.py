import pytest
from fastapi.testclient import TestClient
from order_service import app

client = TestClient(app)


def test_process_order():
    order_id = 1
    response = client.get(f"/process_order/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == f"Order {order_id} processed"
