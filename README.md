# Task Assignment Backend API

A production-ready FastAPI backend with JWT authentication, event management, and booking system.

## 🚀 Features

- **JWT Authentication** with access & refresh tokens
- **Event Management** (create, list, view details) with image URLs
- **Booking System** with rate limiting (5 bookings per minute)
- **PostgreSQL** database with SQLAlchemy ORM
- **Rate Limiting** (in-memory implementation)
- **Swagger UI** for API documentation
- **Automatic Dummy Data Seeding** for testing
- **Production-ready** error handling and logging

## 📋 Requirements

- Python 3.8+
- PostgreSQL 12+
- pip or poetry

## 🔧 Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd Task-Assignment
```

### 2. Create virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

**Option 1: Try standard installation first**
```bash
pip install -r requirements.txt
```

**Option 2: If you get Python 3.13 compatibility issues (like above), use:**
```bash
pip install -r requirements-lite.txt
```

**Option 3: For Python 3.12, use:**
```bash
pip install -r requirements-py312.txt
```

### 4. Setup PostgreSQL Database
```sql
-- Connect to PostgreSQL and create database
CREATE DATABASE task_assignment;
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE task_assignment TO your_username;
```

### 5. Configure Environment Variables
Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` with your configuration:
```env
DATABASE_URL=postgresql://your_username:your_password@localhost:5432/task_assignment
SECRET_KEY=your-super-secret-jwt-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=30
DEBUG=True
```

### 6. Run Database Migrations (Optional)
If you want to use Alembic for migrations:
```bash
# Initialize Alembic (only once)
alembic init migrations

# Create migration
alembic revision --autogenerate -m "Initial migration"

# Apply migration
alembic upgrade head
```

### 7. Start the Server
```bash
# Development mode
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Or using the main.py file
python app/main.py
```

The API will be available at:
- **API**: http://127.0.0.1:8000
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🎯 **Automatic Dummy Data**

When you first start the server, the application automatically creates dummy data for testing:

### **👥 Test Users** (Password: `password123`)
- `user1@test.com` - John Doe
- `user2@test.com` - Jane Smith  
- `user3@test.com` - Bob Johnson
- `user4@test.com` - Alice Williams
- `user5@test.com` - Charlie Brown

### **🎪 Sample Events** (8 realistic events with images)
- Tech Conference 2024
- Rock Concert: Electric Nights  
- Startup Pitch Competition
- Food & Wine Festival
- Art Gallery Opening
- Marathon Training Workshop
- Jazz Evening with Live Orchestra
- Digital Marketing Masterclass

### **📝 Test Bookings**
Pre-created bookings to test the "Top Booked Events" functionality:
- Tech Conference: 3 bookings (most popular)
- Rock Concert: 2 bookings  
- Startup Pitch: 2 bookings

**🔄 Seeding only happens if the database is empty** - no duplicates!

## 📚 API Documentation

### Authentication Endpoints

#### Register User
```bash
POST /auth/register
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword123"
}
```

#### Login
```bash
POST /auth/login
Content-Type: application/json

{
  "email": "john@example.com",
  "password": "securepassword123"
}

# Response
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### Refresh Token
```bash
POST /auth/refresh
Content-Type: application/json

{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Event Endpoints

#### Create Event
```bash
POST /events
Content-Type: application/json

{
  "title": "Tech Conference 2024",
  "description": "Annual technology conference",
  "location": "Convention Center",
  "event_date": "2024-07-15T10:00:00",
  "total_slots": 100,
  "image_url": "https://source.unsplash.com/800x600/?conference"
}
```

#### Get All Events
```bash
GET /events?skip=0&limit=10
```

#### Get Event by ID
```bash
GET /events/1
```

#### Get Top Booked Events
```bash
GET /events/top-booked?limit=3
```

### Booking Endpoints (Authentication Required)

#### Create Booking
```bash
POST /bookings
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "event_id": 1
}
```

#### Get My Bookings
```bash
GET /bookings/my
Authorization: Bearer <access_token>
```

## 🔒 Security Features

- **JWT Tokens**: Access tokens expire in 15 minutes, refresh tokens in 30 days
- **Password Hashing**: Using bcrypt for secure password storage
- **Rate Limiting**: Maximum 5 booking requests per minute per user
- **Input Validation**: Pydantic schemas for request/response validation
- **Error Handling**: Comprehensive error responses

## 🗃️ Database Schema

### Users Table
- `id` (Primary Key)
- `name` (String, max 100 chars)
- `email` (String, unique, indexed)
- `password_hash` (String)
- `created_at` (DateTime)

### Events Table
- `id` (Primary Key)
- `title` (String, max 200 chars)
- `description` (Text, optional)
- `location` (String, max 255 chars)
- `event_date` (DateTime)
- `total_slots` (Integer)
- `image_url` (String, optional) - Public image URLs
- `created_at` (DateTime)

### Bookings Table
- `id` (Primary Key)
- `user_id` (Foreign Key → Users)
- `event_id` (Foreign Key → Events)
- `created_at` (DateTime)
- **Unique constraint**: user_id + event_id

## 📊 Query Examples

### Top 3 Most Booked Events
The API includes a special endpoint that efficiently queries the top booked events:

```sql
SELECT 
    events.*,
    COUNT(bookings.id) as booking_count
FROM events
LEFT JOIN bookings ON events.id = bookings.event_id
GROUP BY events.id
ORDER BY COUNT(bookings.id) DESC
LIMIT 3;
```

Access via: `GET /events/top-booked`

## 🚨 Error Handling

The API returns consistent error responses:

```json
{
  "error": true,
  "message": "Error description",
  "status_code": 400
}
```

Common error scenarios:
- **401**: Invalid credentials, expired tokens
- **400**: Validation errors, duplicate bookings
- **404**: Resource not found
- **429**: Rate limit exceeded
- **500**: Internal server errors

## 🧪 Testing

The app comes with pre-loaded dummy data for immediate testing:

1. **Swagger UI**: http://127.0.0.1:8000/docs
2. **Test Login**: Use any dummy user (e.g., `user1@test.com` / `password123`)
3. **View Events**: Check out 8 realistic events with images
4. **Test Bookings**: Create bookings and see rate limiting in action
5. **Top Booked Events**: `/events/top-booked` shows events with most bookings

You can also test using:
- **curl** commands (see examples above)
- **Postman** collection (import the OpenAPI schema)

## 📁 Project Structure

```
Task-Assignment/
├── app/
│   ├── auth/                 # JWT authentication
│   │   ├── jwt_handler.py
│   │   └── password.py
│   ├── models/              # SQLAlchemy models
│   │   ├── user.py
│   │   ├── event.py
│   │   └── booking.py
│   ├── routers/             # FastAPI routers
│   │   ├── auth.py
│   │   ├── events.py
│   │   └── bookings.py
│   ├── schemas/             # Pydantic schemas
│   │   ├── user.py
│   │   ├── event.py
│   │   ├── booking.py
│   │   └── auth.py
│   ├── services/            # Business logic
│   │   ├── user_service.py
│   │   ├── event_service.py
│   │   └── booking_service.py
│   ├── utils/               # Utilities
│   │   └── rate_limiter.py
│   ├── config.py            # Configuration
│   ├── database.py          # Database setup
│   └── main.py             # FastAPI app
├── requirements.txt
├── .env.example
└── README.md
```

## 🚀 Production Deployment

For production deployment:

1. Set `DEBUG=False` in environment
2. Use a production WSGI server (Gunicorn)
3. Setup proper PostgreSQL instance
4. Use Redis for rate limiting (optional)
5. Configure proper CORS origins
6. Setup SSL/TLS certificates
7. Use environment-specific configurations

Example production command:
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```