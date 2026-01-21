# 🚀 Quick Deployment Guide

## Step 1: GitHub Repository Create Karein

1. https://github.com/new pe jao
2. Repository name: `task-assignment-backend`
3. Description: `FastAPI Task Assignment Backend`
4. Public/Private: Choose as needed
5. ⚠️ **IMPORTANT**: "Initialize with README" **UNCHECK** karein
6. "Create repository" click karein

## Step 2: Script Run Karein

```bash
cd /Users/surajsingh/Task-Assignment
./deploy_complete.sh
```

Script aapko GitHub username aur repo name puchhega, phir automatically push kar dega.

## Step 3: Render.com Deploy

Script ke instructions follow karein. Ya manually:

1. https://render.com → Sign up (GitHub se)
2. "New +" → "Web Service"
3. GitHub repo connect karein
4. Settings:
   - **Build Command**: `pip install -r requirements-lite.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variables**:
     - `SECRET_KEY`: Random string
     - `DEBUG`: `False`
5. Deploy!

---

**That's it! 🎉**