# 🚀 **QUICK START GUIDE - Task Assignment Backend**

## ✅ **Installation Complete!**

All dependencies are installed. Now follow these simple steps:

---

## 📋 **Step 1: Start the Server**

Open terminal in the project folder and run:

```bash
# Make sure you're in the project directory
cd /Users/surajsingh/Task-Assignment

# Activate virtual environment (if not already activated)
source venv/bin/activate

# Start the server
python run_server.py
```

**OR use uvicorn directly:**
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

---

## 🌐 **Step 2: Access Swagger UI**

Once server is running, open in browser:

**👉 http://127.0.0.1:8000/docs**

---

## 🧪 **Step 3: Test with Dummy Data**

### **Login Credentials (Password: `password123`)**
- `user1@test.com`
- `user2@test.com`
- `user3@test.com`
- `user4@test.com`
- `user5@test.com`

### **Quick Test Flow:**

1. **Login** → `POST /auth/login`
   ```json
   {
     "email": "user1@test.com",
     "password": "password123"
   }
   ```
   Copy the `access_token` from response

2. **Authorize in Swagger** → Click "Authorize" button, paste token

3. **View Events** → `GET /events` (see 8 events with images!)

4. **Create Booking** → `POST /bookings` with `{"event_id": 1}`

5. **Top Booked Events** → `GET /events/top-booked`

---

## 📚 **Complete Documentation**

- **Setup Guide**: `SETUP_GUIDE.md`
- **Swagger Examples**: `SWAGGER_EXAMPLES.md`
- **Testing Guide**: `TESTING.md`

---

## ❌ **If Server Doesn't Start**

### **Check if port 8000 is free:**
```bash
lsof -ti:8000 | xargs kill -9
```

### **Check for errors:**
```bash
python -c "from app.main import app; print('✅ App OK')"
```

### **Reinstall dependencies:**
```bash
pip install -r requirements-lite.txt
```

---

## 🎯 **What You Get**

✅ **8 Realistic Events** with beautiful images  
✅ **5 Test Users** ready to use  
✅ **Pre-created Bookings** for testing  
✅ **JWT Authentication** (15min access + 30day refresh tokens)  
✅ **Rate Limiting** (5 bookings per minute)  
✅ **Top Booked Events** query  
✅ **Swagger UI** with full documentation  
✅ **SQLite Database** (no PostgreSQL setup needed!)  

---

## 🚀 **Ready to Go!**

Just run `python run_server.py` and visit **http://127.0.0.1:8000/docs**

**Happy Coding! 🎉**