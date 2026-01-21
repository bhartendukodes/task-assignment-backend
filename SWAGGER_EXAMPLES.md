# 📚 **Swagger UI Complete Documentation & Examples**

## 🚀 **Access Swagger UI**
Visit: **http://127.0.0.1:8000/docs**

---

## 🔐 **Authentication Workflow**

### **Step 1: Register New User**
```json
POST /auth/register
{
  "name": "Test User",
  "email": "testuser@example.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "id": 6,
  "name": "Test User",  
  "email": "testuser@example.com",
  "created_at": "2024-01-21T10:30:45.123Z"
}
```

### **Step 2: Login to Get Tokens**
```json
POST /auth/login
{
  "email": "user1@test.com",
  "password": "password123"
}
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### **Step 3: Authorize in Swagger**
1. Click **"Authorize"** button in Swagger UI
2. Enter: `Bearer YOUR_ACCESS_TOKEN_HERE`
3. Click **"Authorize"**
4. Now all protected endpoints are accessible!

---

## 🎪 **Events API Examples**

### **Get All Events (with Images)**
```json
GET /events?skip=0&limit=10

Response:
[
  {
    "id": 1,
    "title": "Tech Conference 2024",
    "description": "Annual technology conference featuring the latest innovations...",
    "location": "San Francisco Convention Center",
    "event_date": "2024-02-04T10:00:00+00:00",
    "total_slots": 500,
    "image_url": "https://source.unsplash.com/800x600/?conference,technology",
    "created_at": "2024-01-21T10:00:00+00:00",
    "available_slots": 497,
    "booking_count": 3
  },
  {
    "id": 2,
    "title": "Rock Concert: Electric Nights",
    "description": "An electrifying rock concert featuring multiple bands...",
    "location": "Madison Square Garden, New York",
    "event_date": "2024-02-11T20:00:00+00:00",
    "total_slots": 15000,
    "image_url": "https://source.unsplash.com/800x600/?concert,rock,music",
    "created_at": "2024-01-21T10:00:00+00:00",
    "available_slots": 14998,
    "booking_count": 2
  }
]
```

### **Get Top Booked Events (Special Query)**
```json
GET /events/top-booked?limit=3

Response:
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

### **Create New Event**
```json
POST /events
{
  "title": "AI Workshop 2024",
  "description": "Learn cutting-edge AI and machine learning techniques",
  "location": "Tech Hub, Silicon Valley",
  "event_date": "2024-03-15T14:00:00",
  "total_slots": 100,
  "image_url": "https://source.unsplash.com/800x600/?ai,workshop,technology"
}
```

---

## 🎫 **Bookings API Examples (🔒 Auth Required)**

### **Create Booking**
```json
POST /bookings
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE
{
  "event_id": 1
}

Response:
{
  "id": 10,
  "user_id": 1,
  "event_id": 1,
  "created_at": "2024-01-21T11:00:00+00:00",
  "user": {
    "id": 1,
    "name": "John Doe",
    "email": "user1@test.com",
    "created_at": "2024-01-21T10:00:00+00:00"
  },
  "event": {
    "id": 1,
    "title": "Tech Conference 2024",
    "location": "San Francisco Convention Center",
    "event_date": "2024-02-04T10:00:00+00:00",
    "image_url": "https://source.unsplash.com/800x600/?conference,technology"
  }
}
```

### **Get My Bookings**
```json
GET /bookings/my
Authorization: Bearer YOUR_ACCESS_TOKEN_HERE

Response:
[
  {
    "id": 1,
    "user_id": 1,
    "event_id": 1,
    "created_at": "2024-01-21T10:00:00+00:00",
    "event": {
      "title": "Tech Conference 2024",
      "location": "San Francisco Convention Center",
      "event_date": "2024-02-04T10:00:00+00:00",
      "image_url": "https://source.unsplash.com/800x600/?conference,technology"
    }
  }
]
```

---

## ⚡ **Rate Limiting Test**

### **Test Rate Limiting (5 requests per minute)**
Try creating 6 bookings quickly:

**Request 1-5:** ✅ Success
```json
POST /bookings
{
  "event_id": 1  // Change event_id for each request
}
```

**Request 6:** ❌ Rate Limited
```json
Response (HTTP 429):
{
  "error": true,
  "message": "Rate limit exceeded. Maximum 5 requests per 60 seconds.",
  "status_code": 429
}
```

---

## 🔄 **Token Refresh Example**

### **Refresh Access Token**
```json
POST /auth/refresh
{
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

Response:
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

## ❌ **Error Response Examples**

### **Invalid Credentials**
```json
POST /auth/login
{
  "email": "user1@test.com",
  "password": "wrongpassword"
}

Response (HTTP 401):
{
  "error": true,
  "message": "Invalid credentials",
  "status_code": 401
}
```

### **Duplicate Booking**
```json
POST /bookings
{
  "event_id": 1  // Same event already booked
}

Response (HTTP 400):
{
  "error": true,
  "message": "You have already booked this event",
  "status_code": 400
}
```

### **Event Not Found**
```json
GET /events/999

Response (HTTP 404):
{
  "error": true,
  "message": "Event not found",
  "status_code": 404
}
```

### **Unauthorized Access**
```json
POST /bookings  // Without Authorization header
{
  "event_id": 1
}

Response (HTTP 401):
{
  "error": true,
  "message": "Could not validate credentials", 
  "status_code": 401
}
```

---

## 🖼️ **Image URLs in Responses**

All events include **clickable image URLs**:
- **Tech Conference**: `https://source.unsplash.com/800x600/?conference,technology`
- **Rock Concert**: `https://source.unsplash.com/800x600/?concert,rock,music` 
- **Startup Pitch**: `https://source.unsplash.com/800x600/?startup,business,presentation`
- **Food Festival**: `https://source.unsplash.com/800x600/?food,wine,festival`
- **Art Gallery**: `https://source.unsplash.com/800x600/?art,gallery,modern`
- **Marathon**: `https://source.unsplash.com/800x600/?marathon,running,fitness`
- **Jazz Evening**: `https://source.unsplash.com/800x600/?jazz,music,orchestra`
- **Marketing Class**: `https://source.unsplash.com/800x600/?marketing,digital,workshop`

**Click any image URL in Swagger responses to view the image!**

---

## 🧪 **Test Data Overview**

### **Users (Password: `password123`)**
| Email | Name | Has Bookings |
|-------|------|--------------|
| `user1@test.com` | John Doe | Tech Conference |
| `user2@test.com` | Jane Smith | Tech Conference, Startup Pitch |
| `user3@test.com` | Bob Johnson | Tech Conference, Food Festival |
| `user4@test.com` | Alice Williams | Rock Concert, Marathon |
| `user5@test.com` | Charlie Brown | Startup Pitch |

### **Events (8 Total)**
1. **Tech Conference** (3 bookings) - Most Popular
2. **Rock Concert** (2 bookings)
3. **Startup Pitch** (2 bookings) 
4. **Food Festival** (1 booking)
5. **Art Gallery** (0 bookings)
6. **Marathon Workshop** (1 booking)
7. **Jazz Evening** (0 bookings)
8. **Marketing Class** (0 bookings)

---

## 🎯 **Swagger UI Pro Tips**

1. **Use "Try it out"** - Test all endpoints directly
2. **Check Response Schema** - See expected response format
3. **Copy curl commands** - Get ready-to-use curl commands
4. **Download OpenAPI spec** - Export for Postman/Insomnia
5. **Explore Models** - View all data schemas at bottom

Happy Testing! 🚀