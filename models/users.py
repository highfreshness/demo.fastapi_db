from pydantic import BaseModel, EmailStr
from typing import List, Optional
from beanie import Document, Link
from models.events import Event


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Event]]

    class Settings:
        name = "users"
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@nvr.com",
                "password": "week!!!",
                "events": [],
            }
        }


class TokenResponse(BaseModel):
    access_token:str
    token_type:str

