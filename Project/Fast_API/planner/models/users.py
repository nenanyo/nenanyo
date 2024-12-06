from pydantic import BaseModel, EmailStr
from typing import Optional, List
from beanie import Document, Link
from models.events import Event



class User(Document):
    email: EmailStr
    password: str
    username: Optional[str] = None
    events: Optional[List[Event]] =[]


    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str
 
    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }