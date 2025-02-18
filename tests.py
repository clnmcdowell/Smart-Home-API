from fastapi.testclient import TestClient
from smartHomeAPI import app
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

# Test getting a user
def test_get_user():
    user_data = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email": "john@gmail.com"
    }

    # Get the user
    create_response = client.post("/users", json=user_data)
    assert create_response.status_code == 200 # Ensure successful creation
    user_id = create_response.json()["id"]

    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == user_id
    assert data["name"] == user_data["name"]

# Test updating a user
def test_update_user():
    user_data = {
        "name": "Bob",
        "phone_number": "5555555555",
        "email": "bob@gmail.com"
    }
    create_response = client.post("/users", json=user_data)
    assert create_response.status_code == 200
    user_id = create_response.json()["id"]

    updated_data = {
        "id": user_id,
        "name": "Bobby",
        "phone_number": "5555555555",
        "email": "bobby@aol.com"
    }

    # Update the user
    update_response = client.put(f"/users/{user_id}", json=updated_data)
    assert update_response.status_code == 200
    updated_user = update_response.json()

    # Check that user was updated correctly 
    assert updated_user["id"] == user_id
    assert updated_user["name"] == "Bobby"
    assert updated_user["phone_number"] == "5555555555"
    assert updated_user["email"] == "bobby@aol.com"

# Test deleting a user
def test_delete_user():
    user_data = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email": "john@gmail.com"
    }
    
    create_response = client.post("/users", json=user_data)
    assert create_response.status_code == 200 
    
    user_id = create_response.json()["id"]

    # Delete the user
    delete_response = client.delete(f"/users/{user_id}")
    assert delete_response.status_code == 200  # Ensure delete was successful
    assert delete_response.json() == {"message": "User deleted successfully"}

    #Try getting the deleted user
    get_response = client.get(f"/users/{user_id}")
    assert get_response.status_code == 404  # User should no longer exist



## DEVICE TESTS ##
# Test Creating a device
def test_create_device():
    device_data = {
        "name": "Living Room TV",
        "type": "TV",
        "room_id": "room123"
    }
    
    # Create device
    response = client.post("/devices", json=device_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "id" in data
    assert data["name"] == device_data["name"]
    assert data["type"] == device_data["type"]
    assert data["room_id"] == device_data["room_id"]

# Test getting a device
def test_get_device():
    device_data = {
        "name": "Living Room TV",
        "type": "TV",
        "room_id": "room123"
    }

    # Create device
    create_response = client.post("/devices", json=device_data)
    assert create_response.status_code == 200
    device_id = create_response.json()["id"]

    # Get device
    get_response = client.get(f"/devices/{device_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == device_id
    assert data["name"] == device_data["name"]

# Test updating a device
def test_update_device():
    device_data = {
        "name": "Living Room TV",
        "type": "Sony TV",
        "room_id": "room123"
    }

    # Create device
    create_response = client.post("/devices", json=device_data)
    assert create_response.status_code == 200
    device_id = create_response.json()["id"]

    updated_data = {
        "id": device_id,
        "name": "Living Room TV",
        "type": "Samsung TV",
        "room_id": "room4"
    }
    
    # Update device
    update_response = client.put(f"/devices/{device_id}", json=updated_data)
    assert update_response.status_code == 200
    updated_device = update_response.json()
    assert updated_device["id"] == device_id
    assert updated_device["name"] == "Living Room TV"
    assert updated_device["room_id"] == "room4"
    assert updated_device["type"] == "Samsung TV"

# Test deleting a device
def test_delete_device():
    device_data = {
        "name": "Living Room TV",
        "type": "TV",
        "room_id": "room123"
    }

    # Create device
    create_response = client.post("/devices", json=device_data)
    assert create_response.status_code == 200
    device_id = create_response.json()["id"]

    # Delete device 
    delete_response = client.delete(f"/devices/{device_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Device deleted successfully"}

    # Verify device is deleted
    get_response = client.get(f"/devices/{device_id}")
    assert get_response.status_code == 404



## ROOM TESTS ##
# Test creating a room
def test_create_room():
    room_data = {
        "name": "Master Bedroom",
        "type": "Bedroom",
        "size": 200,
        "house_id": "house123"
    }
    
    # Create room
    response = client.post("/rooms", json=room_data)
    assert response.status_code == 200 

    data = response.json()
    assert "id" in data
    assert data["name"] == room_data["name"]
    assert data["type"] == room_data["type"]
    assert data["size"] == room_data["size"]
    assert data["house_id"] == room_data["house_id"]

# Test getting a room
def test_get_room():
    room_data = {
        "name": "Master Bedroom",
        "type": "Bedroom",
        "size": 200,
        "house_id": "house123"
    }

    # Create room
    create_response = client.post("/rooms", json=room_data)
    assert create_response.status_code == 200
    room_id = create_response.json()["id"]

    # Get room
    get_response = client.get(f"/rooms/{room_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == room_id
    assert data["name"] == room_data["name"]

# Test updating a room
def test_update_room():
    room_data = {
        "name": "Guest Bedroom",
        "type": "Bedroom",
        "size": 200,
        "house_id": "house123"
    }

    # Create room
    create_response = client.post("/rooms", json=room_data)
    assert create_response.status_code == 200
    room_id = create_response.json()["id"]

    updated_data = {
        "id": room_id,
        "name": "Master Bedroom",
        "type": "Bedroom",
        "size": 312.5,
        "house_id": "house123"
    }
    
    # Update room
    update_response = client.put(f"/rooms/{room_id}", json=updated_data)
    assert update_response.status_code == 200
    updated_room = update_response.json()
    assert updated_room["id"] == room_id
    assert updated_room["name"] == "Master bedroom"
    assert updated_room["size"] == 312.5
    assert updated_room["house_id"] == "house123"

# Test deleting a room
def test_delete_room():
    room_data = {
        "name": "Master Bedroom",
        "type": "Bedroom",
        "size": 200,
        "house_id": "house123"
    }

    # Create room
    create_response = client.post("/rooms", json=room_data)
    assert create_response.status_code == 200
    room_id = create_response.json()["id"]

    # Delete room
    delete_response = client.delete(f"/rooms/{room_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Room deleted successfully"}

    # Verify room is deleted
    get_response = client.get(f"/rooms/{room_id}")
    assert get_response.status_code == 404 


## HOUSE TESTS ##
# Test creating a house
def test_create_house():
    house_data = {
        "name": "College Apartment ",
        "address": "1 Mass Ave, APT 1, Boston",
        "owners": ["Landlord Paul"],
        "occupants": ["Colin", "Brianna"]
    }
    
    # Create house
    response = client.post("/houses", json=house_data)
    assert response.status_code == 200
    
    data = response.json()
    assert "id" in data
    assert data["name"] == house_data["name"]
    assert data["address"] == house_data["address"]
    assert data["owners"] == house_data["owners"]
    assert data["occupants"] == house_data["occupants"]

# Test getting a house
def test_get_house():
    house_data = {
        "name": "College Apartment ",
        "address": "1 Mass Ave, APT 1, Boston",
        "owners": ["Landlord Paul"],
        "occupants": ["Colin", "Brianna"]
    }

    # Create house
    create_response = client.post("/houses", json=house_data)
    assert create_response.status_code == 200
    house_id = create_response.json()["id"]

    # Get house
    get_response = client.get(f"/houses/{house_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == house_id
    assert data["name"] == house_data["name"]

# Test updating a house
def test_update_house():
    house_data = {
        "name": "College Apartment ",
        "address": "1 Mass Ave, APT 1, Boston",
        "owners": ["Landlord Paul"],
        "occupants": ["Colin", "Brianna"]
    }

    # Create house
    create_response = client.post("/houses", json=house_data)
    assert create_response.status_code == 200
    house_id = create_response.json()["id"]

    updated_data = {
        "id": house_id,
        "name": "Postgrad Apartment",
        "address": "1 Mass Ave, APT 1, Boston",
        "owners": ["Landlord Paul"],
        "occupants": ["Colin"]
    }
    
    # Update house
    update_response = client.put(f"/houses/{house_id}", json=updated_data)
    assert update_response.status_code == 200
    updated_house = update_response.json()
    assert updated_house["id"] == house_id
    assert updated_house["name"] == "Postgrad Apartment"
    assert updated_house["address"] == "1 Mass Ave, APT 1, Boston"
    assert updated_house["owners"] == ["Landlord Paul"]
    assert updated_house["occupants"] == ["Colin"]

def test_delete_house():
    house_data = {
        "name": "College Apartment ",
        "address": "1 Mass Ave, APT 1, Boston",
        "owners": ["Landlord Paul"],
        "occupants": ["Colin", "Brianna"]
    }

    # Create house
    create_response = client.post("/houses", json=house_data)
    assert create_response.status_code == 200
    house_id = create_response.json()["id"]

    # Delete house
    delete_response = client.delete(f"/houses/{house_id}")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "House deleted successfully"}

    # Verify house is deleted
    get_response = client.get(f"/houses/{house_id}")
    assert get_response.status_code == 404
