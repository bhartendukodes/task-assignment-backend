#!/bin/bash

# Auto Deployment Script - Complete Setup
# This script will handle everything

set -e

GITHUB_USERNAME="bhartendukodes"
REPO_NAME="task-assignment-backend"
REPO_URL="https://github.com/$GITHUB_USERNAME/$REPO_NAME"

echo "🚀 Auto Deployment Script"
echo "========================"
echo ""
echo "GitHub Username: $GITHUB_USERNAME"
echo "Repository: $REPO_NAME"
echo ""

# Check if GitHub CLI is available
if command -v gh &> /dev/null; then
    echo "✅ GitHub CLI found!"
    echo ""
    echo "📦 Creating GitHub repository..."
    
    # Check if logged in
    if ! gh auth status &>/dev/null; then
        echo "🔐 GitHub authentication required..."
        gh auth login
    fi
    
    # Create repository
    echo "Creating repository: $REPO_NAME"
    gh repo create "$REPO_NAME" --public --source=. --remote=origin --push 2>/dev/null || {
        echo "⚠️  Repository might already exist, trying to push..."
        git remote add origin "$REPO_URL" 2>/dev/null || true
        git push -u origin main
    }
    
    echo ""
    echo "✅ Repository created and code pushed!"
    
else
    echo "⚠️  GitHub CLI not found. Manual setup required."
    echo ""
    echo "📋 Please follow these steps:"
    echo ""
    echo "1. GitHub pe repository create karein:"
    echo "   👉 https://github.com/new"
    echo ""
    echo "   Repository name: $REPO_NAME"
    echo "   Description: FastAPI Task Assignment Backend"
    echo "   Public/Private: Choose"
    echo "   ⚠️  IMPORTANT: 'Initialize with README' UNCHECK karein"
    echo "   'Create repository' click karein"
    echo ""
    read -p "2. Repository create ho gaya? (y/n): " CONFIRM
    
    if [ "$CONFIRM" = "y" ]; then
        echo ""
        echo "📤 Pushing code to GitHub..."
        
        # Remove existing remote
        git remote remove origin 2>/dev/null || true
        
        # Add remote
        git remote add origin "$REPO_URL"
        
        # Push
        if git push -u origin main; then
            echo ""
            echo "✅ Successfully pushed to GitHub!"
        else
            echo ""
            echo "❌ Push failed. Check:"
            echo "   - Repository create hua hai?"
            echo "   - GitHub credentials setup hain?"
            echo ""
            echo "💡 Try manually:"
            echo "   git push -u origin main"
            exit 1
        fi
    else
        echo ""
        echo "❌ Pehle repository create karein"
        exit 1
    fi
fi

echo ""
echo "🌐 GitHub Repository: $REPO_URL"
echo ""
echo "🎯 Next: Render.com Deployment"
echo "================================"
echo ""
echo "1. https://render.com pe jao"
echo "2. Sign up/Login (GitHub account se)"
echo "3. 'New +' → 'Web Service'"
echo "4. 'Connect GitHub' → Repository select: $REPO_NAME"
echo ""
echo "5. Settings:"
echo "   - Name: task-assignment-api"
echo "   - Build Command: pip install -r requirements-lite.txt"
echo "   - Start Command: uvicorn app.main:app --host 0.0.0.0 --port \$PORT"
echo ""
echo "6. Environment Variables:"
echo "   - SECRET_KEY: (Random string)"
echo "   - DEBUG: False"
echo ""
echo "7. 'Create Web Service' → Wait 5-10 minutes"
echo ""
echo "✅ Deploy ho jayega!"