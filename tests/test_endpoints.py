from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_process_receipt():
    receipt = {
        "retailer": "Target",
        "purchaseDate": "2022-01-02",
        "purchaseTime": "13:13",
        "total": "1.25",
        "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}],
    }
    response = client.post("/receipts/process", json=receipt)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_points():
    receipt = {
        "retailer": "Target",
        "purchaseDate": "2022-01-02",
        "purchaseTime": "13:13",
        "total": "1.25",
        "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}],
    }
    process_response = client.post("/receipts/process", json=receipt)
    receipt_id = process_response.json()["id"]

    response = client.get(f"/receipts/{receipt_id}/points")
    assert response.status_code == 200
    assert "points" in response.json()
