from pydantic import BaseModel, ConfigDict, Field, EmailStr
from datetime import datetime, timezone, timedelta
IST = timezone(timedelta(hours=5, minutes=30))

class UserBase(BaseModel):
    username: str = Field(..., max_length=50)
    email: EmailStr = Field(..., max_length=120)

class UserCreate(UserBase):
    pass
class UserResponse(UserBase):
    id: int
    image_path: str
    model_config = ConfigDict(from_attributes=True)

class PostBase(BaseModel):
    title: str = Field(..., max_length=100)
    content: str = Field(..., max_length=500)

class PostCreate(PostBase):
    user_id: int

class PostResponse(PostBase):
    id: int
    date_posted: datetime
    author: UserResponse
    model_config = ConfigDict(from_attributes=True)