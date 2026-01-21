#!/bin/bash

# Complete Deployment Script
# This will push to GitHub and prepare for Render deployment

set -e

echo "🚀 Complete Deployment Setup"
echo "============================"
echo ""

# Get GitHub details
read -p "📝 GitHub Username: " GITHUB_USERNAME
read -p "📝 Repository Name (default: task-assignment-backend): " REPO_NAME
REPO_NAME=${REPO_NAME:-task-assignment-backend}

echo ""
echo "✅ Configuration:"
echo "   GitHub Username: $GITHUB_USERNAME"
echo "   Repository Name: $REPO_NAME"
echo "   Repository URL: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
echo ""

# Check if remote already exists
if git remote get-url origin &>/dev/null; then
    echo "⚠️  Remote 'origin' already exists. Removing..."
    git remote remove origin
fi

# Add remote
echo "📤 Adding GitHub remote..."
git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

# Set branch to main
git branch -M main 2>/dev/null || echo "Already on main branch"

echo ""
echo "📋 Ready to push! But first:"
echo ""
echo "1. GitHub pe repository create karein:"
echo "   👉 https://github.com/new"
echo ""
echo "   Repository name: $REPO_NAME"
echo "   Description: FastAPI Task Assignment Backend"
echo "   Public/Private: Choose as needed"
echo "   ⚠️  IMPORTANT: 'Initialize with README' UNCHECK karein"
echo ""
read -p "2. Repository create ho gaya? (y/n): " REPO_CREATED

if [ "$REPO_CREATED" != "y" ]; then
    echo ""
    echo "❌ Pehle repository create karein, phir script dobara run karein"
    exit 1
fi

echo ""
echo "📤 Pushing to GitHub..."
echo ""

# Push to GitHub
if git push -u origin main; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "🌐 GitHub Repository: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
    echo ""
    echo "🎯 Next Step: Render.com Deployment"
    echo "=================================="
    echo ""
    echo "1. Render.com pe jao: https://render.com"
    echo "2. Sign up/Login (GitHub account se)"
    echo "3. Dashboard se 'New +' → 'Web Service'"
    echo "4. 'Connect GitHub' click karein"
    echo "5. Repository select karein: $REPO_NAME"
    echo ""
    echo "6. Configure Settings:"
    echo "   - Name: task-assignment-api"
    echo "   - Region: Choose nearest"
    echo "   - Branch: main"
    echo "   - Runtime: Python 3"
    echo "   - Build Command: pip install -r requirements-lite.txt"
    echo "   - Start Command: uvicorn app.main:app --host 0.0.0.0 --port \$PORT"
    echo ""
    echo "7. Environment Variables (Advanced section):"
    echo "   - SECRET_KEY: (Random string - https://randomkeygen.com)"
    echo "   - DEBUG: False"
    echo ""
    echo "8. 'Create Web Service' click karein"
    echo "9. Wait 5-10 minutes for deployment"
    echo ""
    echo "✅ Deploy ho jayega!"
    echo ""
else
    echo ""
    echo "❌ Push failed. Possible reasons:"
    echo "   - Repository create nahi hua"
    echo "   - GitHub authentication issue"
    echo "   - Network problem"
    echo ""
    echo "💡 Solutions:"
    echo "   1. GitHub CLI install karein: brew install gh"
    echo "   2. Ya manually push karein: git push -u origin main"
    echo ""
fi