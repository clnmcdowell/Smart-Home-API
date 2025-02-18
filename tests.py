from fastapi.testclient import TestClient
from user_api import app  # Import your FastAPI app
import uuid

client = TestClient(app)  # Test client to make API requests

# Test creating a user
def testCreateUser():
    user_data = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email": "john@gmail.com"
    }

    response = client.post("/users", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data  # ID should be generated
    assert data["name"] == user_data["name"]
    assert data["phone_number"] == user_data["phone_number"]
    assert data["email"] == user_data["email"]
