from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from typing import List
from app.models import Booking, Event, User
from app.schemas.booking import BookingCreate


class BookingService:
    @staticmethod
    def create_booking(db: Session, booking: BookingCreate, user_id: int) -> Booking:
        """Create a new booking"""
        # Check if event exists
        event = db.query(Event).filter(Event.id == booking.event_id).first()
        if not event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        
        # Check if event has available slots
        current_bookings = db.query(Booking).filter(Booking.event_id == booking.event_id).count()
        if current_bookings >= event.total_slots:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Event is fully booked"
            )
        
        # Create booking
        db_booking = Booking(
            user_id=user_id,
            event_id=booking.event_id
        )
        
        try:
            db.add(db_booking)
            db.commit()
            db.refresh(db_booking)
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="You have already booked this event"
            )
        
        return db_booking
    
    @staticmethod
    def get_user_bookings(db: Session, user_id: int) -> List[Booking]:
        """Get all bookings for a user"""
        bookings = (
            db.query(Booking)
            .filter(Booking.user_id == user_id)
            .all()
        )
        
        # Load related data
        for booking in bookings:
            booking.user
            booking.event
        
        return bookings
    
    @staticmethod
    def get_booking_by_id(db: Session, booking_id: int) -> Booking:
        """Get booking by ID"""
        booking = db.query(Booking).filter(Booking.id == booking_id).first()
        if not booking:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Booking not found"
            )
        
        # Load related data
        booking.user
        booking.event
        
        return booking