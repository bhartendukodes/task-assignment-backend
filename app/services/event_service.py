from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException, status
from typing import List
from app.models import Event, Booking
from app.schemas.event import EventCreate, EventResponse


class EventService:
    @staticmethod
    def create_event(db: Session, event: EventCreate) -> Event:
        """Create a new event"""
        db_event = Event(
            title=event.title,
            description=event.description,
            location=event.location,
            event_date=event.event_date,
            total_slots=event.total_slots,
            image_url=event.image_url
        )
        
        db.add(db_event)
        db.commit()
        db.refresh(db_event)
        return db_event
    
    @staticmethod
    def get_events(db: Session, skip: int = 0, limit: int = 100) -> List[Event]:
        """Get all events with booking information"""
        events = db.query(Event).offset(skip).limit(limit).all()
        
        # Add available slots information
        for event in events:
            booking_count = db.query(Booking).filter(Booking.event_id == event.id).count()
            event.booking_count = booking_count
            event.available_slots = event.total_slots - booking_count
        
        return events
    
    @staticmethod
    def get_event_by_id(db: Session, event_id: int) -> Event:
        """Get event by ID with booking information"""
        event = db.query(Event).filter(Event.id == event_id).first()
        if not event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        
        # Add booking information
        booking_count = db.query(Booking).filter(Booking.event_id == event.id).count()
        event.booking_count = booking_count
        event.available_slots = event.total_slots - booking_count
        
        return event
    
    @staticmethod
    def get_top_booked_events(db: Session, limit: int = 3) -> List[dict]:
        """Get top N most booked events"""
        query = (
            db.query(
                Event,
                func.count(Booking.id).label("booking_count")
            )
            .outerjoin(Booking, Event.id == Booking.event_id)
            .group_by(Event.id)
            .order_by(func.count(Booking.id).desc())
            .limit(limit)
        )
        
        results = query.all()
        
        top_events = []
        for event, booking_count in results:
            event_dict = {
                "id": event.id,
                "title": event.title,
                "description": event.description,
                "location": event.location,
                "event_date": event.event_date,
                "total_slots": event.total_slots,
                "image_url": event.image_url,
                "created_at": event.created_at,
                "booking_count": booking_count,
                "available_slots": event.total_slots - booking_count
            }
            top_events.append(event_dict)
        
        return top_events