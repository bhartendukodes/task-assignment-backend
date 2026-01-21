# 🚀 **Project Kaise Run Karein (How to Run)**

## ✅ **Sab Kuch Ready Hai!**

Aapka project completely setup ho gaya hai. Ab bas ye steps follow karein:

---

## 📋 **Step 1: Server Start Karein**

Terminal mein project folder mein jao aur ye command run karein:

```bash
cd /Users/surajsingh/Task-Assignment
python run_server.py
```

**Ya phir:**
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

---

## 🌐 **Step 2: Swagger UI Open Karein**

Browser mein ye URL open karein:

**👉 http://127.0.0.1:8000/docs**

Yahan aapko **complete API documentation** milega with **Try it out** feature!

---

## 🧪 **Step 3: Test Karein**

### **Login Credentials (Sabka password: `password123`)**
- `user1@test.com` - John Doe
- `user2@test.com` - Jane Smith
- `user3@test.com` - Bob Johnson
- `user4@test.com` - Alice Williams
- `user5@test.com` - Charlie Brown

### **Quick Test:**

1. **Login** → `POST /auth/login`
   - Email: `user1@test.com`
   - Password: `password123`
   - Response mein `access_token` copy karein

2. **Authorize** → Swagger UI mein "Authorize" button click karein
   - Token paste karein: `Bearer YOUR_TOKEN_HERE`

3. **Events Dekho** → `GET /events`
   - 8 events with beautiful images!

4. **Booking Create Karein** → `POST /bookings`
   - `{"event_id": 1}`

5. **Top Booked Events** → `GET /events/top-booked`

---

## 📚 **Complete Documentation Files**

- **START_HERE.md** - Quick start guide
- **SETUP_GUIDE.md** - Detailed setup instructions
- **SWAGGER_EXAMPLES.md** - Complete API examples
- **TESTING.md** - Testing scenarios

---

## 🎯 **Kya Kya Mil Raha Hai**

✅ **8 Realistic Events** with images  
✅ **5 Test Users** ready to use  
✅ **Pre-created Bookings** for testing  
✅ **JWT Authentication** (15min access + 30day refresh)  
✅ **Rate Limiting** (5 bookings per minute)  
✅ **Top Booked Events** query  
✅ **Swagger UI** with full documentation  
✅ **SQLite Database** (PostgreSQL ki zarurat nahi!)  

---

## ❌ **Agar Server Start Nahi Ho Raha**

### **Port check karein:**
```bash
lsof -ti:8000 | xargs kill -9
```

### **Test karein:**
```bash
python test_server.py
```

---

## 🚀 **Abhi Run Karein!**

```bash
python run_server.py
```

Phir browser mein: **http://127.0.0.1:8000/docs**

**Swagger UI mein sab kuch test kar sakte hain! 🎉**