from fastapi import FastAPI,  HTTPException # API framework
from pydantic import BaseModel, Field, EmailStr # Validation library
import uuid

app = FastAPI()

## CLASSES

class User(BaseModel):
    id: str
    name: str = Field(min_length=1, description="User's full name")
    phone_number: str = Field(min_length=12, max_length=12,description="Phone number in format XXX-XXX-XXXX")
    email: EmailStr # Validates email address

## DATA STORAGE
users = {}

## USER API
@app.post("/users", response_model=User)
def create_user(user: User):
    user_id = user.id if user.id else str(uuid.uuid4()) # Generate random ID if not provided by client

    # Raise error if ID is invalid
    if user.id in users:
        raise HTTPException(status_code=400, detail="User ID already exists")

    
    user = User(id=user_id, name=user.name, phone_number=user.phone_number, email=user.email)
    users[user_id] = user
    return user