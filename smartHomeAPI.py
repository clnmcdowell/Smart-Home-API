from fastapi import FastAPI # API framework
from pydantic import BaseModel, Field, EmailStr # Input validation
import uuid

app = FastAPI()

class User(BaseModel):
    id: str # UUID generated automatically 
    name: str = Field(min_length=1, description="User's full name")
    phone_number: str = Field(min_length=12, max_length=12,description="Phone number in format XXX-XXX-XXXX")
    email: EmailStr # Validates email address