from pydantic import BaseModel, EmailStr
from typing import List, Optional
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@nvr.com",
                "password": "week!!!",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@nvr.com",
                "password": "week!!!",
                "events": [],
            }
        }
