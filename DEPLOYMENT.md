# Deployment Guide for Satayoo Agentic AI Tool

## Overview
This guide will help you deploy your Agentic AI tool to satayoo.com/agentic using Vercel.

## Prerequisites
- Node.js 16+ installed locally
- Git repository set up
- Vercel account (free tier works)
- AI API credentials (OpenAI, Anthropic, or your custom API)

## Local Development

1. **Install dependencies:**
   ```bash
   npm install --legacy-peer-deps
   ```

2. **Set up environment variables:**
   - Copy `.env.example` to `.env.local`
   - Add your AI API credentials:
     ```
     REACT_APP_AI_API_ENDPOINT=your_api_endpoint
     REACT_APP_AI_API_KEY=your_api_key
     ```

3. **Run locally:**
   ```bash
   npm start
   ```
   - Visit http://localhost:3000 for the home page
   - Visit http://localhost:3000/agentic for the AI tool

## Deployment to Vercel

### Method 1: Deploy via Vercel CLI

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel
   ```
   Follow the prompts to link your project.

### Method 2: Deploy via GitHub Integration

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add Agentic AI tool"
   git push origin main
   ```

2. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "Import Project"
   - Select your GitHub repository
   - Configure build settings (already set in vercel.json)

3. **Set Environment Variables in Vercel:**
   - Go to Project Settings → Environment Variables
   - Add:
     - `REACT_APP_AI_API_ENDPOINT`
     - `REACT_APP_AI_API_KEY`
   - These will be securely stored and used during build

### Custom Domain Setup

To deploy to satayoo.com/agentic:

1. **If satayoo.com is already on Vercel:**
   - The routing is already configured in our app
   - Just deploy and it will work at /agentic

2. **If using a custom domain:**
   - Go to Project Settings → Domains
   - Add satayoo.com
   - Follow DNS configuration instructions

## Project Structure

```
/workspace
├── src/
│   ├── App.tsx           # Main app with routing
│   ├── Home.tsx          # Home page
│   ├── Agentic.tsx       # AI tool interface
│   ├── Navigation.tsx    # Navigation component
│   ├── api/
│   │   └── aiService.ts  # AI API integration
│   └── *.css             # Styling files
├── public/               # Static assets
├── vercel.json          # Vercel configuration
└── package.json         # Dependencies
```

## Key Features

- **Client-side routing** with React Router
- **Beautiful UI** with gradient design
- **Responsive layout** for mobile and desktop
- **AI integration ready** - just add your API credentials
- **Navigation bar** for easy access between pages
- **Typing indicators** for better UX
- **Message history** with timestamps

## Customizing the AI Integration

Edit `src/api/aiService.ts` to integrate your specific AI API:

```typescript
// Example for OpenAI
const response = await fetch('https://api.openai.com/v1/chat/completions', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${this.apiKey}`
  },
  body: JSON.stringify({
    model: 'gpt-4',
    messages: [
      { role: 'user', content: request.message }
    ]
  })
});
```

## Build Configuration

The `vercel.json` file handles:
- Build command: `npm run build`
- Output directory: `build`
- Client-side routing rewrites

## Troubleshooting

1. **Build fails:**
   - Ensure all dependencies are installed with `--legacy-peer-deps`
   - Check environment variables are set

2. **Routing doesn't work:**
   - Verify `vercel.json` has the rewrite rules
   - Clear browser cache

3. **AI responses not working:**
   - Check API credentials in environment variables
   - Verify API endpoint is correct
   - Check browser console for errors

## Next Steps

1. **Enhance AI capabilities:**
   - Add conversation history persistence
   - Implement streaming responses
   - Add file upload support

2. **Add features:**
   - User authentication
   - Save/load conversations
   - Export chat history
   - Multiple AI models

3. **Optimize performance:**
   - Add response caching
   - Implement lazy loading
   - Optimize bundle size

## Support

For issues or questions:
- Check the browser console for errors
- Verify environment variables are set correctly
- Ensure API credentials are valid

## Security Notes

- Never commit `.env.local` or API keys to Git
- Use environment variables in Vercel for production
- Consider implementing rate limiting for API calls
- Add authentication if needed for production use