from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .user import UserResponse
from .event import EventResponse


class BookingBase(BaseModel):
    event_id: int


class BookingCreate(BookingBase):
    pass


class BookingResponse(BookingBase):
    id: int
    user_id: int
    created_at: datetime
    user: Optional[UserResponse] = None
    event: Optional[EventResponse] = None
    
    class Config:
        from_attributes = True