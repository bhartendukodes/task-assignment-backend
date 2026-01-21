# 🧪 Testing Guide

This guide helps you test all the features of the Task Assignment Backend API.

## 🚀 Quick Start

1. **Start the server**: `python run_server.py`
2. **Visit Swagger UI**: http://127.0.0.1:8000/docs
3. **Automatic dummy data is loaded** - ready to test!

## 👥 Test Users (All have password: `password123`)

| Email | Name | Description |
|-------|------|-------------|
| `user1@test.com` | John Doe | Has bookings for Tech Conference |
| `user2@test.com` | Jane Smith | Has bookings for Tech Conference & Startup Pitch |
| `user3@test.com` | Bob Johnson | Has bookings for Tech Conference & Food Festival |
| `user4@test.com` | Alice Williams | Has bookings for Rock Concert & Marathon |
| `user5@test.com` | Charlie Brown | Has booking for Startup Pitch |

## 🎪 Sample Events (8 Events with Images)

1. **Tech Conference 2024** - 3 bookings (most popular)
2. **Rock Concert: Electric Nights** - 2 bookings
3. **Startup Pitch Competition** - 2 bookings  
4. **Food & Wine Festival** - 1 booking
5. **Art Gallery Opening** - 0 bookings
6. **Marathon Training Workshop** - 1 booking
7. **Jazz Evening with Live Orchestra** - 0 bookings
8. **Digital Marketing Masterclass** - 0 bookings

## 🧪 Test Scenarios

### **1. Authentication Flow**
```bash
# 1. Register new user
POST /auth/register
{
  "name": "Test User",
  "email": "test@example.com", 
  "password": "password123"
}

# 2. Login with existing user
POST /auth/login
{
  "email": "user1@test.com",
  "password": "password123"
}
# Save the access_token and refresh_token

# 3. Test refresh token
POST /auth/refresh
{
  "refresh_token": "your_refresh_token_here"
}
```

### **2. Events API**
```bash
# 1. Get all events (see images!)
GET /events

# 2. Get specific event  
GET /events/1

# 3. Get top booked events
GET /events/top-booked
# Should return: Tech Conference (3), Rock Concert (2), Startup Pitch (2)

# 4. Create new event
POST /events
{
  "title": "New Event",
  "description": "Test event",
  "location": "Test Location",
  "event_date": "2024-08-01T15:00:00",
  "total_slots": 50,
  "image_url": "https://source.unsplash.com/800x600/?event"
}
```

### **3. Bookings API (Requires Authentication)**
```bash
# Add Bearer token to Authorization header

# 1. Create booking
POST /bookings
Authorization: Bearer your_access_token
{
  "event_id": 1
}

# 2. Get my bookings  
GET /bookings/my
Authorization: Bearer your_access_token

# 3. Test rate limiting (try 6+ requests quickly)
# Should get HTTP 429 after 5 requests per minute
```

### **4. Rate Limiting Test**
1. Login as any user
2. Rapidly create 6 bookings for different events
3. The 6th request should return **HTTP 429**:
```json
{
  "error": true,
  "message": "Rate limit exceeded. Maximum 5 requests per 60 seconds.",
  "status_code": 429
}
```

### **5. Error Scenarios**
```bash
# Duplicate booking (should fail)
POST /bookings (same event_id twice)

# Event fully booked (create event with total_slots: 1, book twice)

# Invalid credentials  
POST /auth/login with wrong password

# Expired token (wait 15+ minutes or use invalid token)
GET /bookings/my with old/invalid token
```

## 🖼️ Image URLs

All events have public image URLs from Unsplash:
- Tech Conference: `https://source.unsplash.com/800x600/?conference,technology`
- Rock Concert: `https://source.unsplash.com/800x600/?concert,rock,music`
- And more...

These images are **directly viewable in browsers** and **display in Swagger responses**.

## 📊 Expected Results

### **Top Booked Events** (`GET /events/top-booked`)
```json
[
  {
    "id": 1,
    "title": "Tech Conference 2024",
    "booking_count": 3,
    "available_slots": 497,
    "image_url": "https://source.unsplash.com/800x600/?conference,technology"
  },
  {
    "id": 2, 
    "title": "Rock Concert: Electric Nights",
    "booking_count": 2,
    "available_slots": 14998,
    "image_url": "https://source.unsplash.com/800x600/?concert,rock,music"
  },
  {
    "id": 3,
    "title": "Startup Pitch Competition", 
    "booking_count": 2,
    "available_slots": 198,
    "image_url": "https://source.unsplash.com/800x600/?startup,business,presentation"
  }
]
```

## ✅ What to Verify

- [ ] All 8 events load with images
- [ ] Top booked events returns correct order
- [ ] Rate limiting blocks after 5 requests 
- [ ] JWT tokens work and expire properly
- [ ] Bookings prevent duplicates
- [ ] Images display correctly in Swagger UI
- [ ] Error responses are properly formatted
- [ ] All dummy users can login with `password123`

## 🎯 Pro Tips

1. **Use Swagger UI** - It's the easiest way to test all endpoints
2. **Check the logs** - Server logs show seeding process and errors
3. **Database resets** - Delete the database to see seeding happen again
4. **Image verification** - Click image URLs to verify they load
5. **Rate limiting** - Test with different users to see independent limits

Happy Testing! 🚀