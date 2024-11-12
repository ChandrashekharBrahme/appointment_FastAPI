# app/schemas.py
from pydantic import BaseModel
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str

class BookingCreate(BaseModel):
    slot: datetime

class BookingOut(BaseModel):
    id: int
    slot: datetime
    user_id: int

    class Config:
        orm_mode = True
