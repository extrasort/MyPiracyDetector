# Your Personal Deployment Guide

## ✅ Your Configuration

All your credentials are configured and ready to deploy!

### 🤖 Telegram Bot
- **Bot Token**: `8293675187:AAErsgcn1mzZUrrITeTA9fcOYybFL7X97QU`
- **Chat ID**: `139096195`
- **Status**: ✅ Ready

### 🔍 SerpAPI
- **API Key**: `10f5b9c093d015253b7b73bf56e2b15ddcec4d96a78a2e3add3b1afc1ec24cbd`
- **Monthly Limit**: 250 searches
- **Configured Usage**: 4 searches per run
- **Status**: ✅ Optimized

### 📚 Novel Information
- **Title**: Level Up Legacy
- **Author**: MellowGuy

## 🎯 Optimized Search Strategy

Your bot is configured with 4 targeted queries per scan:

1. `"Level Up Legacy" "MellowGuy"` - Most accurate (author+title)
2. `"Level Up Legacy" read online free` - Common piracy sites
3. `"Level Up Legacy" chapter 1` - Chapter-based piracy
4. `"Level Up Legacy" pdf download` - Document piracy

### Usage Calculation
```
4 queries per scan × 1 scan/day = 4 searches/day
4 searches/day × 30 days = 120 searches/month
Remaining buffer: 130 searches for testing
```

**✅ This is SAFE and leaves plenty of buffer!**

## 🚀 Deploy to Railway NOW (5 Minutes)

### Step 1: Go to Railway
Visit: **https://railway.app/new**

### Step 2: Connect GitHub
1. Click **"Deploy from GitHub repo"**
2. Authorize Railway to access GitHub
3. Select: **`extrasort/MyPiracyDetector`**
4. Click **"Deploy Now"**

### Step 3: Add Environment Variables

In Railway dashboard, go to your service → **Variables** tab.

Click **"Add Variables"** and paste this:

```env
SERPAPI_KEY=10f5b9c093d015253b7b73bf56e2b15ddcec4d96a78a2e3add3b1afc1ec24cbd
TELEGRAM_BOT_TOKEN=8293675187:AAErsgcn1mzZUrrITeTA9fcOYybFL7X97QU
TELEGRAM_CHAT_ID=139096195
TELEGRAM_ENABLED=true
NOVEL_TITLE=Level Up Legacy
AUTHOR_NAME=MellowGuy
SCAN_SECRET_KEY=mypiracy2024secret
```

**Important**: Change `SCAN_SECRET_KEY` to something unique if you want!

### Step 4: Wait for Deployment
- Railway will build and deploy (takes ~2 minutes)
- You'll get a URL like: `https://mypiracydetector.up.railway.app`
- Save this URL!

### Step 5: Test Your Deployment

Open this URL in your browser (replace with YOUR Railway URL):
```
https://mypiracydetector.up.railway.app/scan?key=mypiracy2024secret
```

You should see:
```json
{
  "status": "success",
  "message": "Piracy scan started. Results will be sent to Telegram."
}
```

**Check your Telegram!** You should receive:
- 🚨 Alert message
- 📎 CSV file (if URLs found)
- ⚖️ DMCA report (if URLs found)

## ⏰ Set Up Automated Daily Scans

### Option A: Cron-Job.org (Recommended - Free & Easy)

1. **Sign up**: Go to https://cron-job.org/en/signup/
2. **Create account** (free, no credit card needed)
3. **Create cron job**:
   - Click **"Create Cron Job"**
   - **Title**: `Novel Piracy Scanner`
   - **URL**: `https://YOUR-RAILWAY-URL.railway.app/scan?key=mypiracy2024secret`
   - **Schedule**: Select **"Once a day"**
   - **Time**: Choose 9:00 AM (or your preferred time)
   - **Enabled**: ✅ Yes
   - Click **"Create"**

✅ Done! Your bot will scan daily automatically.

### Option B: EasyCron (Alternative)

1. Go to: https://www.easycron.com/user/register
2. Free plan: 1 cron job
3. Add cron job:
   - **URL**: `https://YOUR-RAILWAY-URL.railway.app/scan?key=mypiracy2024secret`
   - **When**: Daily at 9 AM
   - **Method**: GET

### Option C: GitHub Actions (Advanced)

Already set up in your repo! Just enable workflows.

## 📱 What You'll Receive Daily

Every day at your scheduled time, if piracy is detected:

### 1. Alert Message
```
🚨 New Piracy URLs Detected!

📚 Novel: Level Up Legacy
✍️ Author: MellowGuy
🔍 Found: 3 new URL(s)
⏰ Time: 2025-11-17 09:00 UTC

📍 Infringing URLs:
1. pirate-novels.com
   https://pirate-novels.com/level-up-legacy/...
2. freenovel.site
   ...
```

### 2. CSV File
Complete data with all detected URLs

### 3. DMCA Report
Ready-to-send takedown notice

**If no new URLs**: You won't receive messages (bot stays quiet).

## 📊 Monitoring Your Usage

### Check SerpAPI Dashboard
Visit: https://serpapi.com/account

You should see:
- **Daily**: ~4 searches used
- **Weekly**: ~28 searches used
- **Monthly**: ~120 searches used

If you see more, reduce frequency!

### Check Railway Logs
1. Go to Railway dashboard
2. Click your service
3. Go to **"Deployments"** tab
4. Click **"View Logs"**

Look for:
```
✅ Telegram notification sent successfully
```

## ⚠️ IMPORTANT: Stay Within Limits

### ✅ SAFE (Your Current Setup)
- **Frequency**: Once per day
- **Daily searches**: 4
- **Monthly searches**: ~120
- **Status**: ✅ Safe with buffer

### ⚠️ MODERATE (If needed)
- **Frequency**: Twice per day
- **Daily searches**: 8
- **Monthly searches**: ~240
- **Status**: ⚠️ Tight, but works

### ❌ AVOID
- **Don't run more than 2x daily**
- **Don't add more than 4 extra queries**
- **Don't test too frequently**

## 🔧 Adjusting Your Setup

### Want More Coverage?
Add up to 4 more queries in Railway variables:
```
QUERY_5="Level Up Legacy" epub
QUERY_6="Level Up Legacy" full text
```

But remember: More queries = more searches per day!

### Want Less Usage?
Remove a query or run every 2 days instead.

### Want to Pause?
Disable your cron job temporarily on cron-job.org

## 🆘 Troubleshooting

### No Telegram Messages?
1. Test your bot: Visit your scan URL manually
2. Check Railway logs for errors
3. Verify environment variables are set
4. Make sure you've started chat with bot (send `/start` to your bot)

### "Unauthorized" Error?
- Check `SCAN_SECRET_KEY` matches in URL and Railway variables

### No Results Found?
- This is normal! It means no NEW piracy URLs were detected
- Existing URLs are tracked in `seen_urls.json`

### Railway App Sleeping?
- Railway free tier apps don't sleep on new plans
- Your cron will wake it up anyway

## 📈 Success Metrics

After 1 week, you should have:
- ✅ 7 scans completed
- ✅ ~28 searches used (out of 250)
- ✅ Any new piracy URLs detected and reported
- ✅ DMCA reports ready in Telegram

## 🎯 Next Steps

1. ✅ Deploy to Railway (5 minutes)
2. ✅ Test scan manually (2 minutes)
3. ✅ Set up daily cron job (3 minutes)
4. ✅ Check Telegram for first results
5. ✅ Monitor weekly usage

## 📞 Your URLs

- **GitHub Repo**: https://github.com/extrasort/MyPiracyDetector
- **Railway URL**: (You'll get this after deployment)
- **Scan URL**: `https://YOUR-APP.railway.app/scan?key=mypiracy2024secret`

## 🎉 You're All Set!

Everything is configured and ready. Just deploy to Railway and set up the cron job!

**Total time**: ~10 minutes
**Maintenance**: Zero (fully automated)
**Cost**: Free (Railway + SerpAPI free tiers)

Questions? Check:
- `RAILWAY_DEPLOY.md` - Detailed Railway guide
- `USAGE_LIMITS.md` - Search limit details
- `QUICKSTART.md` - Quick reference

Happy piracy hunting! 🎯

