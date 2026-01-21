#!/bin/bash

echo "🚀 GitHub Push Script"
echo "===================="
echo ""
echo "Pehle GitHub pe repository banao: https://github.com/new"
echo "Repository name: task-assignment-backend"
echo ""
read -p "GitHub username enter karein: " GITHUB_USERNAME
read -p "Repository name (default: task-assignment-backend): " REPO_NAME
REPO_NAME=${REPO_NAME:-task-assignment-backend}

echo ""
echo "GitHub repository URL: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
echo ""
read -p "Ye sahi hai? (y/n): " CONFIRM

if [ "$CONFIRM" != "y" ]; then
    echo "❌ Cancelled"
    exit 1
fi

echo ""
echo "📤 GitHub pe push kar rahe hain..."
echo ""

# Remove existing remote if any
git remote remove origin 2>/dev/null

# Add new remote
git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

# Push to GitHub
git branch -M main
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Successfully pushed to GitHub!"
    echo ""
    echo "🌐 Ab Render.com pe deploy karein:"
    echo "   1. https://render.com pe jao"
    echo "   2. Sign up/Login (GitHub se)"
    echo "   3. 'New +' → 'Web Service'"
    echo "   4. Apna repository select karein"
    echo "   5. Settings configure karein (DEPLOY_RENDER.md dekhain)"
    echo ""
else
    echo ""
    echo "❌ Push failed. Check karein:"
    echo "   - GitHub repository create hua hai?"
    echo "   - Username aur repo name sahi hai?"
    echo "   - GitHub credentials setup hain?"
fi