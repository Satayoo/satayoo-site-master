#!/bin/bash

echo "================================================"
echo "🚀 Vercel Deployment with Token"
echo "================================================"
echo ""

# Check if VERCEL_TOKEN is provided
if [ -z "$1" ]; then
    echo "❌ No token provided."
    echo ""
    echo "Usage: ./deploy-with-token.sh YOUR_VERCEL_TOKEN"
    echo ""
    echo "To get a token:"
    echo "1. Go to https://vercel.com/account/tokens"
    echo "2. Create a new token"
    echo "3. Copy the token and run:"
    echo "   ./deploy-with-token.sh YOUR_TOKEN_HERE"
    echo ""
    echo "Or set it as environment variable:"
    echo "   export VERCEL_TOKEN=your_token_here"
    echo "   vercel --token \$VERCEL_TOKEN"
    exit 1
fi

VERCEL_TOKEN=$1

echo "🔨 Building the project..."
npm run build

if [ $? -ne 0 ]; then
    echo "❌ Build failed. Please fix the errors and try again."
    exit 1
fi

echo "✅ Build successful!"
echo ""

echo "🚀 Deploying to Vercel..."
vercel --token $VERCEL_TOKEN --yes

echo ""
echo "================================================"
echo "✅ Deployment complete!"
echo "================================================"
echo ""
echo "For production deployment, run:"
echo "vercel --token $VERCEL_TOKEN --prod --yes"
echo ""