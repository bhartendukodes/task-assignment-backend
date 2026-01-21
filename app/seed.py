from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models import User, Event, Booking
from app.auth.password import get_password_hash
import logging

logger = logging.getLogger(__name__)


def create_dummy_users(db: Session):
    """Create dummy users for testing"""
    dummy_users = [
        {
            "name": "John Doe",
            "email": "user1@test.com",
            "password": "password123"
        },
        {
            "name": "Jane Smith",
            "email": "user2@test.com",
            "password": "password123"
        },
        {
            "name": "Bob Johnson",
            "email": "user3@test.com",
            "password": "password123"
        },
        {
            "name": "Alice Williams",
            "email": "user4@test.com",
            "password": "password123"
        },
        {
            "name": "Charlie Brown",
            "email": "user5@test.com",
            "password": "password123"
        }
    ]
    
    created_users = []
    for user_data in dummy_users:
        # Check if user already exists
        existing_user = db.query(User).filter(User.email == user_data["email"]).first()
        if not existing_user:
            hashed_password = get_password_hash(user_data["password"])
            user = User(
                name=user_data["name"],
                email=user_data["email"],
                password_hash=hashed_password
            )
            db.add(user)
            created_users.append(user)
    
    db.commit()
    
    # Refresh to get IDs
    for user in created_users:
        db.refresh(user)
    
    logger.info(f"Created {len(created_users)} dummy users")
    return created_users


def create_dummy_events(db: Session):
    """Create dummy events with realistic data and image URLs"""
    # Base date for future events
    base_date = datetime.now() + timedelta(days=7)
    
    dummy_events = [
        {
            "title": "Tech Conference 2024",
            "description": "Annual technology conference featuring the latest innovations in software development, AI, and cloud computing. Join industry leaders and experts for insightful talks and networking opportunities.",
            "location": "San Francisco Convention Center",
            "event_date": base_date + timedelta(days=14),
            "total_slots": 500,
            "image_url": "https://images.unsplash.com/photo-1540575467063-178a50c2df87?w=800&h=600&fit=crop"
        },
        {
            "title": "Rock Concert: Electric Nights",
            "description": "An electrifying rock concert featuring multiple bands and special guest performances. Get ready for an unforgettable night of music and energy.",
            "location": "Madison Square Garden, New York",
            "event_date": base_date + timedelta(days=21),
            "total_slots": 15000,
            "image_url": "https://images.unsplash.com/photo-1470229722913-7c0e2dbbafd3?w=800&h=600&fit=crop"
        },
        {
            "title": "Startup Pitch Competition",
            "description": "Watch the next generation of entrepreneurs pitch their innovative ideas to a panel of seasoned investors. Network with founders and learn about emerging trends.",
            "location": "Google Campus, Mountain View",
            "event_date": base_date + timedelta(days=35),
            "total_slots": 200,
            "image_url": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=800&h=600&fit=crop"
        },
        {
            "title": "Food & Wine Festival",
            "description": "Celebrate culinary excellence with renowned chefs, wine tastings, and gourmet food experiences. A paradise for food enthusiasts and wine connoisseurs.",
            "location": "Napa Valley, California",
            "event_date": base_date + timedelta(days=42),
            "total_slots": 800,
            "image_url": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=800&h=600&fit=crop"
        },
        {
            "title": "Art Gallery Opening: Modern Expressions",
            "description": "Experience contemporary art from emerging and established artists. An exclusive opening featuring paintings, sculptures, and digital art installations.",
            "location": "Museum of Modern Art, New York",
            "event_date": base_date + timedelta(days=28),
            "total_slots": 150,
            "image_url": "https://images.unsplash.com/photo-1541961017774-22349e4a1262?w=800&h=600&fit=crop"
        },
        {
            "title": "Marathon Training Workshop",
            "description": "Learn from professional trainers and nutritionists about marathon preparation, injury prevention, and performance optimization. Perfect for all fitness levels.",
            "location": "Central Park, New York",
            "event_date": base_date + timedelta(days=7),
            "total_slots": 100,
            "image_url": "https://images.unsplash.com/photo-1571008887538-b36bb32f4571?w=800&h=600&fit=crop"
        },
        {
            "title": "Jazz Evening with Live Orchestra",
            "description": "An intimate jazz performance featuring a 12-piece orchestra playing classic and contemporary jazz pieces. Enjoy drinks and great music in a sophisticated setting.",
            "location": "Blue Note Jazz Club, New York",
            "event_date": base_date + timedelta(days=49),
            "total_slots": 80,
            "image_url": "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=800&h=600&fit=crop"
        },
        {
            "title": "Digital Marketing Masterclass",
            "description": "Learn cutting-edge digital marketing strategies from industry experts. Covers social media marketing, SEO, content creation, and analytics.",
            "location": "WeWork, San Francisco",
            "event_date": base_date + timedelta(days=63),
            "total_slots": 50,
            "image_url": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=800&h=600&fit=crop"
        }
    ]
    
    created_events = []
    for event_data in dummy_events:
        event = Event(
            title=event_data["title"],
            description=event_data["description"],
            location=event_data["location"],
            event_date=event_data["event_date"],
            total_slots=event_data["total_slots"],
            image_url=event_data["image_url"]
        )
        db.add(event)
        created_events.append(event)
    
    db.commit()
    
    # Refresh to get IDs
    for event in created_events:
        db.refresh(event)
    
    logger.info(f"Created {len(created_events)} dummy events")
    return created_events


def create_dummy_bookings(db: Session, users: list, events: list):
    """Create dummy bookings to test 'top booked events' functionality"""
    if not users or not events:
        logger.warning("No users or events available for creating dummy bookings")
        return []
    
    # Create bookings to make some events more popular
    dummy_bookings = [
        # Tech Conference - Most popular (3 bookings)
        {"user": users[0], "event": events[0]},
        {"user": users[1], "event": events[0]},
        {"user": users[2], "event": events[0]},
        
        # Rock Concert - Second most popular (2 bookings)
        {"user": users[0], "event": events[1]},
        {"user": users[3], "event": events[1]},
        
        # Startup Pitch - Third most popular (2 bookings)
        {"user": users[1], "event": events[2]},
        {"user": users[4], "event": events[2]},
        
        # Food & Wine Festival (1 booking)
        {"user": users[2], "event": events[3]},
        
        # Marathon Workshop (1 booking)
        {"user": users[3], "event": events[5]},
    ]
    
    created_bookings = []
    for booking_data in dummy_bookings:
        # Check if booking already exists
        existing_booking = db.query(Booking).filter(
            Booking.user_id == booking_data["user"].id,
            Booking.event_id == booking_data["event"].id
        ).first()
        
        if not existing_booking:
            booking = Booking(
                user_id=booking_data["user"].id,
                event_id=booking_data["event"].id
            )
            db.add(booking)
            created_bookings.append(booking)
    
    db.commit()
    
    logger.info(f"Created {len(created_bookings)} dummy bookings")
    return created_bookings


def seed_database(db: Session):
    """Main seeding function - only runs if database is empty"""
    try:
        # Check if data already exists
        user_count = db.query(User).count()
        event_count = db.query(Event).count()
        
        if user_count > 0 or event_count > 0:
            logger.info("Database already contains data. Skipping seeding.")
            return
        
        logger.info("Database is empty. Starting data seeding...")
        
        # Create dummy data
        users = create_dummy_users(db)
        events = create_dummy_events(db)
        bookings = create_dummy_bookings(db, users, events)
        
        logger.info("Database seeding completed successfully!")
        logger.info(f"Created: {len(users)} users, {len(events)} events, {len(bookings)} bookings")
        
    except Exception as e:
        logger.error(f"Error during database seeding: {e}")
        db.rollback()
        # Don't raise - allow app to continue even if seeding fails
        logger.warning("Continuing without seeded data. Database may be empty.")