from pydantic import BaseModel, EmailStr
from typing import Optional
#imports from pydantic and typing

#creates the first class, inherits from BaseModel and gathers name and (properly formatted) Email
class UserBase(BaseModel):
    name: str
    email: EmailStr

#second class, inherits from UserBase and defines password as a string
class UserCreate(UserBase):
    password: str

#update class, inherits from basemodel, but allows name or email to be null
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

#defines User class, takes everything from UserBase, adds an id, also defines input as objects instead of dictionaries
class User(UserBase):
    id: int
    class Config:
        from_attributes = True