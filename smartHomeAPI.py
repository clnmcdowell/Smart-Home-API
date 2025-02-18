from fastapi import FastAPI,  HTTPException # API framework
from pydantic import BaseModel, Field, EmailStr # Validation library
import uuid
from typing import Optional

app = FastAPI()

## CLASSES

class User(BaseModel):
    id: Optional[str] = None
    name: str = Field(min_length=1, description="User's full name")
    phone_number: str = Field(min_length=10, max_length=10,description="Phone number in format XXXXXXXXXX")
    email: EmailStr # Validates email address

## DATA STORAGE
users = {}

## USER API

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
