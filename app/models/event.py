from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    location = Column(String(255), nullable=False)
    event_date = Column(DateTime(timezone=True), nullable=False)
    total_slots = Column(Integer, nullable=False)
    image_url = Column(String(500), nullable=True)
    creator_ip = Column(String(45), nullable=True)  # IPv4 max 15 chars, IPv6 max 45 chars
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    # Relationships
    bookings = relationship("Booking", back_populates="event", cascade="all, delete-orphan")