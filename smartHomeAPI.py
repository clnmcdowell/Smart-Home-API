from fastapi import FastAPI,  HTTPException # API framework
from pydantic import BaseModel, Field, EmailStr # Validation library
import uuid
from typing import Optional

app = FastAPI()

## CLASSES ##
class User(BaseModel):
    id: Optional[str] = None # Automatically generated if not provided
    name: str = Field(min_length=1, description="User's full name")
    phone_number: str = Field(min_length=10, max_length=10,description="Phone number in format XXXXXXXXXX")
    email: EmailStr # Validates email address

class Device(BaseModel):
    id: Optional[str] = None # Automatically generated if not provided
    name: str = Field(min_length=1, description="Device name")
    type: str = Field(min_length=1, description="Device type (TV, Thermometer, etc.)")
    room_id: str = Field(min_length=1, description="ID of the room the device belongs to")

class Room(BaseModel):
    id: Optional[str] = None # Automatically generated if not provided
    name: str = Field(min_length=1, description="Room name")
    type: str = Field(min_length=1, description="Room type (bedroom, kitchen, etc)")
    size: float = Field(gt=0, description="Room size in square feet")
    house_id: str = Field(min_length=1, description="ID of the house the room belongs to")

## DATA STORAGE ##
users = {}
devices = {}
rooms = {}

## USER API ##
# Creates new user with optional ID
@app.post("/users", response_model=User)
def create_user(user: User):
    user_id = user.id if user.id else str(uuid.uuid4()) # Generate random ID if not provided by client

    # Raise error if ID is invalid
    if user.id in users:
        raise HTTPException(status_code=400, detail="User ID already exists")

    
    user = User(id=user_id, name=user.name, phone_number=user.phone_number, email=user.email)
    users[user_id] = user
    return user

# Get user by ID
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    return users[user_id]

# Update user information
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, updated_user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    users[user_id] = updated_user # Copy user passed to function
    return updated_user

# Delete user by ID
@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    del users[user_id]
    return {"message": "User deleted successfully"}

## DEVICE API ##
# Create device
@app.post("/devices", response_model=Device)
def create_device(device: Device):
    device_id = device.id if device.id else str(uuid.uuid4())

    if device_id in devices:
        raise HTTPException(status_code=400, detail="Device ID already exists")

    device = Device(id=device_id, name=device.name, type=device.type, room_id=device.room_id)
    devices[device_id] = device
    return device

# Get device by ID
@app.get("/devices/{device_id}", response_model=Device)
def get_device(device_id: str):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")
    return devices[device_id]

# Update device
@app.put("/devices/{device_id}", response_model=Device)
def update_device(device_id: str, updated_device: Device):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")

    devices[device_id] = updated_device
    return updated_device

# Delete device by ID
@app.delete("/devices/{device_id}")
def delete_device(device_id: str):
    if device_id not in devices:
        raise HTTPException(status_code=404, detail="Device not found")

    del devices[device_id]
    return {"message": "Device deleted successfully"}

## ROOM API ##
# Create Room
@app.post("/rooms", response_model=Room)
def create_room(room: Room):
    room_id = room.id if room.id else str(uuid.uuid4())

    if room_id in rooms:
        raise HTTPException(status_code=400, detail="Room ID already exists")

    room = Room(id=room_id, name=room.name, type=room.type, size=room.size, house_id=room.house_id)
    rooms[room_id] = room
    return room

# Get room by ID
@app.get("/rooms/{room_id}", response_model=Room)
def get_room(room_id: str):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")
    
    return rooms[room_id]

# Update room
@app.put("/rooms/{room_id}", response_model=Room)
def update_room(room_id: str, updated_room: Room):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")

    rooms[room_id] = updated_room
    return updated_room

# Delete room
@app.delete("/rooms/{room_id}")
def delete_room(room_id: str):
    if room_id not in rooms:
        raise HTTPException(status_code=404, detail="Room not found")

    del rooms[room_id]
    return {"message": "Room deleted successfully"}
