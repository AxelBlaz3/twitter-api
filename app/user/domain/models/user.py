from datetime import datetime
from beanie import Document
from pydantic import EmailStr, Field, BaseModel

from .location import Location
from typing import List

class BaseUser(BaseModel):
    """Represents a data model for the user.
    """
    username: str = Field(min_length=2)
    display_name: str = Field(alias='displayName', min_length=1)
    email: str = EmailStr()
    location: Location
    created_at: datetime = Field(default=datetime.utcnow(), alias='createdAt')
    followers: List[str] = Field(default=[])
    following: List[str] = Field(default=[])

class User(BaseUser, Document):
    pass

class UserRequest(BaseUser):
    """Represents a data model for user request."""
    password: str = Field(min_length=8)

class UserResponse(BaseUser):
    """Represents a data model for user response"""
    pass

class UserUpdate(BaseModel):
    """Represents a data model for updating user data"""
    pass
