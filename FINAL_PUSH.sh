#!/bin/bash

# Final Push Script - Ready to execute
# Just create the GitHub repo and run this

GITHUB_USERNAME="bhartendukodes"
REPO_NAME="task-assignment-backend"
REPO_URL="https://github.com/$GITHUB_USERNAME/$REPO_NAME"

echo "🚀 Final Push Script"
echo "==================="
echo ""
echo "⚠️  IMPORTANT: Pehle GitHub pe repository create karein!"
echo ""
echo "1. https://github.com/new pe jao"
echo "2. Repository name: $REPO_NAME"
echo "3. 'Initialize with README' UNCHECK karein"
echo "4. 'Create repository' click karein"
echo ""
read -p "Repository create ho gaya? (y/n): " READY

if [ "$READY" != "y" ]; then
    echo "❌ Pehle repository create karein"
    exit 1
fi

echo ""
echo "📤 Pushing code to GitHub..."

# Setup remote
git remote remove origin 2>/dev/null || true
git remote add origin "$REPO_URL"

# Push
if git push -u origin main; then
    echo ""
    echo "✅ ✅ ✅ SUCCESS! Code pushed to GitHub! ✅ ✅ ✅"
    echo ""
    echo "🌐 Repository: $REPO_URL"
    echo ""
    echo "🎯 Ab Render.com pe deploy karein:"
    echo "   1. https://render.com"
    echo "   2. Sign up/Login (GitHub)"
    echo "   3. New Web Service"
    echo "   4. Connect: $REPO_NAME"
    echo "   5. Build: pip install -r requirements-lite.txt"
    echo "   6. Start: uvicorn app.main:app --host 0.0.0.0 --port \$PORT"
    echo "   7. Env Vars: SECRET_KEY (random), DEBUG=False"
    echo "   8. Deploy!"
    echo ""
else
    echo ""
    echo "❌ Push failed. Check:"
    echo "   - Repository URL sahi hai?"
    echo "   - GitHub authentication?"
    echo ""
    echo "Manual push: git push -u origin main"
fi