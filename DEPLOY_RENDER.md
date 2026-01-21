# 🚀 Render.com Deployment Steps

## Step 1: GitHub Pe Push Karein

### Agar GitHub repo nahi hai:
1. https://github.com pe jao
2. "New repository" click karein
3. Repository name: `task-assignment-backend` (ya kuch bhi)
4. Public/Private choose karein
5. "Create repository" click karein
6. Copy the repository URL

### Ab terminal mein ye commands run karein:

```bash
cd /Users/surajsingh/Task-Assignment

# GitHub repo URL add karein (apna URL use karein)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Code push karein
git branch -M main
git push -u origin main
```

---

## Step 2: Render.com Pe Deploy

1. **Render.com pe jao**: https://render.com
2. **Sign up/Login**: GitHub account se login karein
3. **New Web Service**: Dashboard se "New +" → "Web Service"
4. **Connect GitHub**: Apna repository select karein
5. **Configure Settings**:
   - **Name**: `task-assignment-api` (ya kuch bhi)
   - **Region**: Choose nearest (Singapore ya US)
   - **Branch**: `main`
   - **Root Directory**: (leave empty)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements-lite.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. **Environment Variables** (Advanced section mein):
   - `SECRET_KEY`: Random string generate karein (https://randomkeygen.com se)
   - `DEBUG`: `False`
   - `DATABASE_URL`: (leave empty, SQLite use hoga)
7. **Create Web Service**: Click karein
8. **Wait**: 5-10 minutes deploy hone mein

---

## Step 3: Deploy Complete!

Deploy hone ke baad aapko milega:
- **Live URL**: `https://your-app-name.onrender.com`
- **Swagger UI**: `https://your-app-name.onrender.com/docs`

---

## Important Notes:

1. **First Deploy**: 5-10 minutes lag sakta hai
2. **Free Tier**: 15 minutes inactivity ke baad sleep ho jata hai
3. **Wake Up**: First request pe 30-60 seconds lag sakta hai
4. **Database**: SQLite file-based hai, restart pe data reset ho sakta hai

---

## Production Database (Optional):

Agar persistent database chahiye:
1. Render dashboard mein "New +" → "PostgreSQL"
2. Database create karein
3. Internal Database URL copy karein
4. Web Service settings mein `DATABASE_URL` add karein

---

## Troubleshooting:

- **Build fails**: Check logs in Render dashboard
- **App crashes**: Check environment variables
- **Slow response**: Free tier limitation (upgrade for better performance)

---

**Deploy ho gaya! 🎉**