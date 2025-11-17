# Railway Deployment Guide

This guide will help you deploy the Novel Piracy Detector to Railway with full Telegram integration.

## 📋 Prerequisites

1. **Railway Account**: Sign up at [railway.app](https://railway.app)
2. **Telegram Bot**: Created via @BotFather (see main README)
3. **SerpAPI Key**: Get from [serpapi.com](https://serpapi.com)
4. **GitHub Account**: To connect your repository

## 🚀 Deployment Steps

### Step 1: Push to GitHub

```bash
cd /Users/sadiq/novel-piracy-detector

# Initialize git if not already done
git add .
git commit -m "Prepare for Railway deployment"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/novel-piracy-detector.git
git push -u origin master
```

### Step 2: Deploy to Railway

1. Go to [railway.app](https://railway.app)
2. Click **"New Project"**
3. Select **"Deploy from GitHub repo"**
4. Choose your `novel-piracy-detector` repository
5. Railway will automatically detect and deploy your app

### Step 3: Configure Environment Variables

In your Railway project dashboard:

1. Click on your service
2. Go to **"Variables"** tab
3. Add these environment variables:

```
SERPAPI_KEY=your_serpapi_key_here
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz
TELEGRAM_CHAT_ID=123456789
TELEGRAM_ENABLED=true
NOVEL_TITLE=Level Up Legacy
AUTHOR_NAME=MellowGuy
SCAN_SECRET_KEY=your_random_secret_key_here
```

**Important:** 
- Use your actual API keys and tokens
- `SCAN_SECRET_KEY` should be a random string (e.g., `a8f3h2k9p4m1n6v7`)

### Step 4: Get Your Railway URL

After deployment completes:

1. Railway will assign you a public URL (e.g., `https://your-app.up.railway.app`)
2. Save this URL - you'll need it for triggering scans

### Step 5: Test the Deployment

Visit these URLs to verify:

```
# Health check
https://your-app.up.railway.app/health

# Configuration check
https://your-app.up.railway.app/config
```

## 🔄 Triggering Scans

### Manual Trigger (Test)

You can manually trigger a scan by visiting (replace with your values):

```
https://your-app.up.railway.app/scan?key=your_random_secret_key_here
```

You should receive results in Telegram!

### Automated Scans (Recommended)

Set up automated scans using a cron service:

#### Option 1: Railway Cron (Built-in)

1. In Railway dashboard, go to your service
2. Click **"Settings"** → **"Cron Jobs"**
3. Add a new cron job:
   - **Schedule**: `0 */6 * * *` (every 6 hours)
   - **Command**: `python piracy_detector.py`

#### Option 2: Cron-job.org (Free External Service)

1. Go to [cron-job.org](https://cron-job.org)
2. Create a free account
3. Create a new cron job:
   - **Title**: Novel Piracy Scanner
   - **URL**: `https://your-app.up.railway.app/scan?key=YOUR_SECRET_KEY`
   - **Schedule**: Every 6 hours (or daily)
   - **Method**: GET or POST

#### Option 3: EasyCron (Alternative)

1. Go to [easycron.com](https://www.easycron.com)
2. Free plan allows 1 cron job
3. Set URL: `https://your-app.up.railway.app/scan?key=YOUR_SECRET_KEY`
4. Set schedule: Daily or every 6 hours

#### Option 4: GitHub Actions (Advanced)

Create `.github/workflows/piracy-scan.yml`:

```yaml
name: Piracy Scan

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
  workflow_dispatch:  # Manual trigger

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Scan
        run: |
          curl -X POST "https://your-app.up.railway.app/scan?key=${{ secrets.SCAN_SECRET_KEY }}"
```

Don't forget to add `SCAN_SECRET_KEY` to GitHub Secrets!

## 📱 What You'll Receive in Telegram

When piracy URLs are detected, you'll receive:

1. **📨 Summary Message**: Overview with detected URLs
2. **📎 CSV File**: Complete list with all details
3. **⚖️ DMCA Report**: Ready-to-use takedown notice

No need to check server files - everything comes to you!

## 🔧 Troubleshooting

### Check Logs

In Railway dashboard:
1. Click on your service
2. Go to **"Deployments"** tab
3. Click **"View Logs"** to see what's happening

### Common Issues

**"Unauthorized" error when triggering scan:**
- Make sure you're using the correct `SCAN_SECRET_KEY`
- Check that the key is set in Railway environment variables

**No Telegram messages:**
- Verify `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHAT_ID` are correct
- Make sure you've started a chat with your bot (send `/start`)
- Check Railway logs for errors

**No results found:**
- Verify `SERPAPI_KEY` is valid and has credits
- Check Railway logs for API errors

### Test Your Bot

Run the test script locally before deploying:

```bash
python test_telegram.py
```

## 💰 Cost Considerations

- **Railway**: Free tier includes 500 hours/month (sufficient for this app)
- **SerpAPI**: Free tier includes 100 searches/month
- **Telegram**: Completely free

With 3 queries per scan running every 6 hours:
- Daily: 4 scans × 3 queries = 12 searches
- Monthly: ~360 searches (may need paid SerpAPI plan)

Consider running daily instead of every 6 hours to stay in free tier.

## 🔒 Security Notes

1. **Never commit** `.env` file or hardcoded API keys
2. Keep your `SCAN_SECRET_KEY` private
3. Rotate keys periodically
4. Use Railway's environment variables for all secrets

## 📊 Monitoring

Railway provides built-in monitoring:
- CPU and memory usage
- Request logs
- Deployment history

Check these regularly to ensure smooth operation.

## 🆘 Need Help?

- Railway Docs: [docs.railway.app](https://docs.railway.app)
- Railway Discord: [discord.gg/railway](https://discord.gg/railway)
- This project: Open an issue on GitHub

