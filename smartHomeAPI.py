from fastapi import FastAPI,  HTTPException # API framework
from pydantic import BaseModel, Field, EmailStr # Validation library
import uuid
from typing import Optional, List

app = FastAPI()

## CLASSES ##
# Field() does input validation on creation
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

class House(BaseModel):
    id: Optional[str] = None  # Automatically generated if not provided
    name: str = Field(min_length=1, description="House name")
    address: str = Field(min_length=1, description="House address")
    owners: List[str] = Field(default=[], description="List of owner IDs")
    occupants: List[str] = Field(default=[], description="List of occupant IDs")

## DATA STORAGE ##
users = {}
devices = {}
rooms = {}
houses = {}

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



## HOUSE API ##
# Create house
@app.post("/houses", response_model=House)
def create_house(house: House):
    house_id = house.id if house.id else str(uuid.uuid4())

    if house_id in houses:
        raise HTTPException(status_code=400, detail="House ID already exists")

    house = House(id=house_id, name=house.name, address=house.address, owners=house.owners, occupants=house.occupants)
    houses[house_id] = house
    return house

# Get house
@app.get("/houses/{house_id}", response_model=House)
def get_house(house_id: str):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")
    
    return houses[house_id]

# Update house
@app.put("/houses/{house_id}", response_model=House)
def update_house(house_id: str, updated_house: House):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")

    houses[house_id] = updated_house
    return updated_house

# Delete house
@app.delete("/houses/{house_id}")
def delete_house(house_id: str):
    if house_id not in houses:
        raise HTTPException(status_code=404, detail="House not found")

    del houses[house_id]
    return {"message": "House deleted successfully"}