from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from typing import Optional


class EventBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    location: str = Field(..., min_length=1, max_length=255)
    event_date: datetime
    total_slots: int = Field(..., ge=1)
    image_url: Optional[str] = Field(None, max_length=500)


class EventCreate(EventBase):
    pass


class EventResponse(EventBase):
    id: int
    created_at: datetime
    available_slots: Optional[int] = None
    booking_count: Optional[int] = None
    
    class Config:
        from_attributes = True