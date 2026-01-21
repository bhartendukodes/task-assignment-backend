# 🚀 **Complete Setup Guide - Task Assignment Backend**

## 🔧 **Step-by-Step Installation**

### **1. Clone/Download Project**
```bash
# If using git
git clone <your-repo-url>
cd Task-Assignment

# If downloaded as ZIP, extract and navigate to folder
```

### **2. Create Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### **3. Install Dependencies**

**🚨 IMPORTANT: Choose the right option based on your Python version**

**Option A: Standard Installation (try this first)**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Option B: If you get Python 3.13 errors (like you did):**
```bash
pip install --upgrade pip
pip install -r requirements-lite.txt
```

**Option C: For Python 3.12 specifically:**
```bash
pip install --upgrade pip
pip install -r requirements-py312.txt
```

### **4. Setup PostgreSQL Database**

**Install PostgreSQL:**
```bash
# macOS (using Homebrew)
brew install postgresql
brew services start postgresql

# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib

# Windows
# Download from: https://www.postgresql.org/download/windows/
```

**Create Database:**
```bash
# Connect to PostgreSQL
psql postgres

# Create database and user
CREATE DATABASE task_assignment;
CREATE USER taskuser WITH PASSWORD 'taskpassword123';
GRANT ALL PRIVILEGES ON DATABASE task_assignment TO taskuser;
\q
```

### **5. Configure Environment**
```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your database settings
```

**Edit `.env` file:**
```env
DATABASE_URL=postgresql://taskuser:taskpassword123@localhost:5432/task_assignment
SECRET_KEY=your-super-secret-jwt-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=30
DEBUG=True
```

### **6. Run the Application**

**Method 1: Using run_server.py**
```bash
python run_server.py
```

**Method 2: Using uvicorn directly**
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

**Method 3: Using Python module**
```bash
python -m uvicorn app.main:app --reload
```

### **7. Access the Application**
- **API**: http://127.0.0.1:8000
- **Swagger UI**: http://127.0.0.1:8000/docs  
- **ReDoc**: http://127.0.0.1:8000/redoc

## 🧪 **Testing with Dummy Data**

The app automatically creates test data:

### **Login Credentials (all have password: `password123`)**
- `user1@test.com` - John Doe
- `user2@test.com` - Jane Smith
- `user3@test.com` - Bob Johnson
- `user4@test.com` - Alice Williams
- `user5@test.com` - Charlie Brown

### **Sample API Requests**

**1. Login to get token:**
```bash
curl -X POST "http://127.0.0.1:8000/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user1@test.com",
    "password": "password123"
  }'
```

**2. Get all events (with images):**
```bash
curl -X GET "http://127.0.0.1:8000/events"
```

**3. Create booking (use token from step 1):**
```bash
curl -X POST "http://127.0.0.1:8000/bookings" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "event_id": 1
  }'
```

**4. Get top booked events:**
```bash
curl -X GET "http://127.0.0.1:8000/events/top-booked"
```

## ❌ **Troubleshooting Common Issues**

### **Python 3.13 Compatibility Issues**
```bash
# Use the lite requirements
pip install -r requirements-lite.txt
```

### **PostgreSQL Connection Issues**
```bash
# Check if PostgreSQL is running
brew services list | grep postgresql  # macOS
sudo systemctl status postgresql      # Linux

# Test connection
psql -h localhost -U taskuser -d task_assignment
```

### **Port Already in Use**
```bash
# Kill process using port 8000
sudo lsof -ti:8000 | xargs kill -9

# Or use different port
uvicorn app.main:app --port 8001
```

### **Module Import Errors**
```bash
# Ensure you're in the project directory
pwd

# Ensure virtual environment is activated
which python  # Should show venv path

# Reinstall dependencies
pip install --force-reinstall -r requirements-lite.txt
```

## 🔥 **Quick Test Commands**

```bash
# Test if server is running
curl http://127.0.0.1:8000/health

# Test registration
curl -X POST "http://127.0.0.1:8000/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "password": "password123"
  }'

# Test events endpoint
curl http://127.0.0.1:8000/events
```

## 📱 **Swagger UI Features**

1. **Go to**: http://127.0.0.1:8000/docs
2. **Login**: Use `/auth/login` with dummy credentials
3. **Authorize**: Click "Authorize" button, paste token
4. **Test**: All endpoints are now accessible
5. **Images**: Event responses show image URLs
6. **Rate Limiting**: Try creating 6+ bookings quickly

## 🎯 **Production Deployment**

For production:
```bash
# Set production environment
DEBUG=False
SECRET_KEY=your-super-secure-random-key-here

# Use production server
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

That's it! Your FastAPI backend with dummy data is now running! 🚀