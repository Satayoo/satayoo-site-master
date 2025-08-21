#!/bin/bash

echo "================================================"
echo "🚀 Satayoo Agentic AI Tool - Vercel Deployment"
echo "================================================"
echo ""

# Check if user is logged in to Vercel
echo "📋 Checking Vercel login status..."
if ! vercel whoami &> /dev/null; then
    echo "❌ You're not logged in to Vercel."
    echo ""
    echo "Please run: vercel login"
    echo "Then run this script again."
    exit 1
fi

echo "✅ Logged in to Vercel"
echo ""

# Build the project
echo "🔨 Building the project..."
npm run build

if [ $? -ne 0 ]; then
    echo "❌ Build failed. Please fix the errors and try again."
    exit 1
fi

echo "✅ Build successful!"
echo ""

# Deploy to Vercel
echo "🚀 Deploying to Vercel..."
echo ""
echo "This will deploy your app. You'll be asked a few questions:"
echo "1. Set up and deploy? → Yes"
echo "2. Which scope? → Select your account"
echo "3. Link to existing project? → No (for first deployment)"
echo "4. Project name? → satayoo-agentic (or your preferred name)"
echo "5. Directory with code? → ./ (current directory)"
echo ""

vercel

echo ""
echo "================================================"
echo "✅ Deployment initiated!"
echo "================================================"
echo ""
echo "Next steps:"
echo "1. Visit your Vercel dashboard to add environment variables:"
echo "   - REACT_APP_AI_API_ENDPOINT"
echo "   - REACT_APP_AI_API_KEY"
echo ""
echo "2. For production deployment, run: vercel --prod"
echo ""
echo "3. To set up custom domain (satayoo.com):"
echo "   - Go to your project settings in Vercel"
echo "   - Add domain in the Domains section"
echo ""
echo "================================================"