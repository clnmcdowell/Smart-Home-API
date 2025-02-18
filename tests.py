from fastapi.testclient import TestClient
from smartHomeAPI import app  # Import your FastAPI app
import uuid

client = TestClient(app)  # Test client to make API requests

## USER TESTS ##

# Test creating a user
def testCreateUser():
    userData = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email": "john@gmail.com"
    }

    response = client.post("/users", json=userData) # API request to create user
    assert response.status_code == 200 # 200 response code means OK
    data = response.json()
    assert "id" in data  # ID should be generated
    assert data["name"] == userData["name"]
    assert data["phone_number"] == userData["phone_number"]
    assert data["email"] == userData["email"]

def testGetUser():
    userData = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email": "john@gmail.com"
    }

    create_response = client.post("/users", json=userData)
    assert create_response.status_code == 200
    user_id = create_response.json()["id"]

    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == user_id
    assert data["name"] == userData["name"]