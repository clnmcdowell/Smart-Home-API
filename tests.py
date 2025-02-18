from fastapi.testclient import TestClient
from smartHomeAPI import app  # Import your FastAPI app
import uuid

client = TestClient(app)  # Test client to make API requests

## USER TESTS ##

# Test creating a user
def test_create_user():
    user_data = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email": "john@gmail.com"
    }

    response = client.post("/users", json=user_data) # API request to create user
    assert response.status_code == 200 # 200 response code means OK
    data = response.json()
    assert "id" in data  # ID should be generated
    assert data["name"] == user_data["name"]
    assert data["phone_number"] == user_data["phone_number"]
    assert data["email"] == user_data["email"]

def test_get_user():
    user_data = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email": "john@gmail.com"
    }

    create_response = client.post("/users", json=user_data)
    assert create_response.status_code == 200
    user_id = create_response.json()["id"]

    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == user_id
    assert data["name"] == user_data["name"]