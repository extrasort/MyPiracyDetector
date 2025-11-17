# SerpAPI Usage Limits & Recommendations

## Your Current Plan
- **Monthly Limit**: 250 searches
- **Daily Limit**: ~8 searches/day (to stay within monthly limit)
- **Current Queries**: 4 queries configured

## Search Calculation

Each time the script runs:
```
1 run = 4 queries = 4 SerpAPI searches
```

### Recommended Schedules

#### ✅ SAFE: Once Daily (Recommended)
- **Frequency**: 1x per day
- **Searches/day**: 4
- **Searches/month**: ~120
- **Buffer**: 130 searches remaining for testing/manual runs
- **Cron**: `0 9 * * *` (9 AM daily)

#### ⚠️ MODERATE: Twice Daily
- **Frequency**: 2x per day
- **Searches/day**: 8
- **Searches/month**: ~240
- **Buffer**: 10 searches (tight!)
- **Cron**: `0 9,21 * * *` (9 AM and 9 PM)

#### ❌ AVOID: More than twice daily
- Will exceed your monthly limit
- Risk running out mid-month

## Current Query Configuration

```python
QUERIES = [
    '"Level Up Legacy" "MellowGuy"',          # Query 1
    '"Level Up Legacy" read online free',     # Query 2
    '"Level Up Legacy" chapter 1',            # Query 3
    '"Level Up Legacy" pdf download',         # Query 4
]
```

## Adjusting for More/Less Searches

### Want more queries? Reduce frequency
```
6 queries × 1 run/day = 6 searches/day = 180/month ✅
8 queries × 1 run/day = 8 searches/day = 240/month ⚠️
```

### Want more frequent scans? Reduce queries
```
3 queries × 2 runs/day = 6 searches/day = 180/month ✅
4 queries × 2 runs/day = 8 searches/day = 240/month ⚠️
```

## Monitoring Your Usage

### Check SerpAPI Dashboard
1. Go to: https://serpapi.com/account
2. View "API Usage" or "Statistics"
3. Monitor daily/monthly consumption

### Railway/Cron Job Logs
Check your Railway logs to see scan completion:
```
✅ Scan completed
Searches used: 4
```

## Optimizing Your Queries

### High-Value Queries (Recommended)
```python
'"Level Up Legacy" "MellowGuy"',              # Author+title combo
'"Level Up Legacy" read online free',         # Common piracy phrase
'"Level Up Legacy" chapter 1',                # Chapter searches
'"Level Up Legacy" pdf download',             # Download searches
'"Level Up Legacy" epub',                     # eBook format
'"Level Up Legacy" full text',                # Full text searches
```

### Queries to Avoid
- Too generic: `"Level Up Legacy"` alone (too many results)
- Too specific: Long chapter excerpts (miss variations)
- Official domains will be filtered anyway

## Emergency: Running Out of Searches

If you're approaching your limit mid-month:

### Reduce queries temporarily
Edit `piracy_detector.py`:
```python
QUERIES = [
    f'"{NOVEL_TITLE}" "{AUTHOR_NAME}"',  # Keep only the most important
]
```

### Pause automated scans
- Disable your cron job
- Wait until next month
- Resume with adjusted frequency

### Upgrade SerpAPI plan (if needed)
- Standard Plan: $50/month = 5,000 searches
- Visit: https://serpapi.com/pricing

## Best Practice Recommendations

### 🎯 Recommended Setup (Safe & Effective)
1. **Queries**: Keep 4 queries (current setup)
2. **Frequency**: Once daily at 9 AM
3. **Monthly usage**: ~120 searches
4. **Buffer**: 130 searches for manual testing

### 📊 Monitor Weekly
Check your SerpAPI dashboard every week:
- Week 1: Should be at ~28 searches
- Week 2: Should be at ~56 searches
- Week 3: Should be at ~84 searches
- Week 4: Should be at ~112 searches

If you're ahead of pace, reduce frequency.

### 🔧 Adjust as Needed
- More piracy activity? Increase to 2x daily for a week
- Quiet period? Run every other day
- Testing features? Count test runs toward your limit!

## Telegram Notifications

Every scan will show in the notification:
```
🔍 Found: X new URL(s)
⏰ Time: 2025-11-17 09:00 UTC
```

No results = Still used your search quota!

## Summary

**Your Current Setup:**
- ✅ 4 queries configured
- ✅ Recommended: Run once daily
- ✅ Uses ~120/250 searches per month
- ✅ Safe buffer for testing
- ✅ All results sent via Telegram

**Cron Job Setting:**
```
URL: https://your-app.railway.app/scan?key=your_secret
Schedule: Once daily (e.g., 9 AM)
```

This setup ensures you never exceed your limit while maintaining good coverage! 🎯

