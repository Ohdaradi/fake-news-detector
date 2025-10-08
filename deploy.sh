#!/bin/bash
# Deploy RealFake AI to Cloud Platform

echo "🚀 RealFake AI - Cloud Deployment Helper"
echo "========================================"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Not a git repository. Please run this from your project root."
    exit 1
fi

echo "📋 Choose your deployment platform:"
echo "1) Render.com (Free tier available)"
echo "2) Railway.app (Fast deployment)"  
echo "3) Heroku (Classic platform)"
echo "4) Manual setup instructions"

read -p "Enter your choice (1-4): " choice

case $choice in
    1)
        echo "🚀 Deploying to Render.com..."
        echo "1. Push your code: git push origin main"
        echo "2. Visit: https://render.com"
        echo "3. Connect GitHub and select this repository"
        echo "4. Use these settings:"
        echo "   - Environment: Python 3"
        echo "   - Build Command: pip install -r requirements.txt"
        echo "   - Start Command: gunicorn --bind 0.0.0.0:\$PORT app:app"
        ;;
    2)
        echo "⚡ Deploying to Railway.app..."
        echo "1. Push your code: git push origin main"
        echo "2. Visit: https://railway.app"
        echo "3. Connect GitHub and deploy your repository"
        echo "4. Railway will auto-detect configuration from railway.json"
        ;;
    3)
        echo "🔥 Deploying to Heroku..."
        echo "1. Install Heroku CLI if not installed"
        echo "2. Run: heroku login"
        echo "3. Run: heroku create your-app-name"
        echo "4. Run: git push heroku main"
        echo "5. Run: heroku open"
        ;;
    4)
        echo "📖 Manual Setup:"
        echo "1. Requirements.txt ✅ Created"
        echo "2. Procfile ✅ Created" 
        echo "3. render.yaml ✅ Created"
        echo "4. railway.json ✅ Created"
        echo "5. App.py ✅ Updated for production"
        echo ""
        echo "Your app is ready for deployment to any platform!"
        ;;
    *)
        echo "❌ Invalid choice. Please run the script again."
        exit 1
        ;;
esac

echo ""
echo "🎉 Your RealFake AI app is ready for the cloud!"
echo "📍 Repository: https://github.com/Ohdaradi/fake-news-detector"