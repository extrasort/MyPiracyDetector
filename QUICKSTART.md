# Quick Start Guide

Get your piracy detector running in 5 minutes!

## 1️⃣ Set Up Telegram Bot (2 minutes)

### Create Bot
1. Open Telegram, search for `@BotFather`
2. Send `/newbot`
3. Name your bot: "My Piracy Detector"
4. Save the **Bot Token** (looks like: `123456789:ABC...`)

### Get Chat ID
1. Search for `@userinfobot` on Telegram
2. Send `/start`
3. Copy your **Chat ID** (a number)

## 2️⃣ Get SerpAPI Key (1 minute)

1. Go to [serpapi.com](https://serpapi.com/users/sign_up)
2. Sign up (free plan available)
3. Copy your API key from dashboard

## 3️⃣ Choose Deployment Method

### ☁️ Cloud (Railway) - Automated & Always Running

Perfect for: Set-it-and-forget-it automated scanning

1. **Quick Deploy:**
   
   [![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template)
   
   Or follow: [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md)

2. **Add Environment Variables** in Railway:
   ```
   SERPAPI_KEY=your_key
   TELEGRAM_BOT_TOKEN=your_token
   TELEGRAM_CHAT_ID=your_chat_id
   NOVEL_TITLE=Level Up Legacy
   AUTHOR_NAME=MellowGuy
   SCAN_SECRET_KEY=random_secret_123
   ```

3. **Set up cron job** (cron-job.org):
   - URL: `https://your-app.railway.app/scan?key=random_secret_123`
   - Schedule: Every 6 hours

✅ Done! You'll get Telegram alerts automatically.

### 💻 Local - Manual Scanning

Perfect for: Occasional manual checks

```bash
# 1. Clone and install
git clone <your-repo>
cd novel-piracy-detector
pip install -r requirements.txt

# 2. Edit piracy_detector.py with your keys
nano piracy_detector.py

# 3. Run manually
python piracy_detector.py
```

## 4️⃣ Test It!

### Test Telegram Bot
```bash
python test_telegram.py
```

### Test Full Scan
```bash
python piracy_detector.py
```

You should receive messages in Telegram!

## 📱 What You'll Receive

When piracy is detected:
1. 🚨 Alert message with summary
2. 📎 CSV file with all URLs
3. ⚖️ DMCA takedown notice (ready to send)

## 🔄 Scan Frequency Recommendations

- **High traffic novels**: Every 6 hours
- **Medium traffic**: Daily
- **Low traffic**: Weekly

Adjust based on your SerpAPI quota (free tier = 100 searches/month).

## 💡 Pro Tips

1. **Add custom search queries** in `piracy_detector.py`:
   ```python
   QUERIES = [
       f'"{NOVEL_TITLE}" "{AUTHOR_NAME}"',
       f'"{NOVEL_TITLE}" "read online free"',
       f'"{NOVEL_TITLE}" "chapter 1"',
   ]
   ```

2. **Add more official domains** to whitelist:
   ```python
   OFFICIAL_DOMAINS = {
       "webnovel.com",
       "yoursite.com",
       "patreon.com"
   }
   ```

3. **Monitor SerpAPI usage**: Check your dashboard regularly

## 🆘 Troubleshooting

### No Telegram messages?
- Verify bot token and chat ID
- Make sure you started chat with bot (`/start`)
- Run `python test_telegram.py`

### No results found?
- Check SerpAPI key and credits
- Verify novel title and author name
- Try broader search queries

### Railway deployment issues?
- Check environment variables are set
- View logs in Railway dashboard
- Ensure secret key is correct for triggering scans

## 📚 Next Steps

- Read full [README.md](README.md)
- Deploy to Railway: [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md)
- Customize search queries
- Set up automated scanning

Happy piracy hunting! 🎯

