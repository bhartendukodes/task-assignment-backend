from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.event import EventCreate, EventResponse
from app.services.event_service import EventService

router = APIRouter(prefix="/events", tags=["events"])


@router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
async def create_event(event: EventCreate, db: Session = Depends(get_db)):
    """Create a new event"""
    try:
        db_event = EventService.create_event(db, event)
        
        # Add booking information for response
        db_event.booking_count = 0
        db_event.available_slots = db_event.total_slots
        
        return db_event
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create event"
        )


@router.get("/", response_model=List[EventResponse])
async def get_events(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    """Get all events with pagination"""
    try:
        events = EventService.get_events(db, skip=skip, limit=limit)
        return events
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch events"
        )


@router.get("/top-booked", response_model=List[EventResponse])
async def get_top_booked_events(
    limit: int = Query(3, ge=1, le=10),
    db: Session = Depends(get_db)
):
    """Get top N most booked events"""
    try:
        top_events = EventService.get_top_booked_events(db, limit=limit)
        return top_events
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch top booked events"
        )


@router.get("/{event_id}", response_model=EventResponse)
async def get_event(event_id: int, db: Session = Depends(get_db)):
    """Get event by ID"""
    try:
        event = EventService.get_event_by_id(db, event_id)
        return event
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch event"
        )