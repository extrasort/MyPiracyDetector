# Novel Piracy Detector

A Python script to detect unauthorized hosting of your web novel by searching Google via SerpAPI and tracking potential copyright infringements.

## Features

- 🔍 Searches Google for your novel using SerpAPI
- 📊 Tracks discovered URLs and avoids duplicates
- 📝 Generates DMCA takedown notice drafts
- 💾 Exports results to CSV for easy review
- 🔄 Incremental scanning (remembers previously seen URLs)

## Prerequisites

- Python 3.7 or higher
- A SerpAPI account and API key (get one at https://serpapi.com/)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd novel-piracy-detector
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Edit `piracy_detector.py` and update the following constants:

```python
# Your SerpAPI key
SERPAPI_KEY = "your_actual_serpapi_key_here"

# Your work information
NOVEL_TITLE = "Your Novel Title"
AUTHOR_NAME = "Your Author Name"

# Official domains (won't be flagged as piracy)
OFFICIAL_DOMAINS = {
    "webnovel.com",
    "yourofficialdomain.com"
}

# Customize search queries
QUERIES = [
    f'"{NOVEL_TITLE}" "{AUTHOR_NAME}"',
    # Add more queries as needed
]
```

## Usage

Run the script:

```bash
python piracy_detector.py
```

The script will:
1. Search Google for your novel using the configured queries
2. Filter out official domains
3. Track new URLs not seen in previous runs
4. Generate three output files:
   - `piracy_candidates.csv` - All discovered URLs with metadata
   - `seen_urls.json` - Cache of previously seen URLs
   - `dmca_report.txt` - Draft DMCA takedown notice

## Output Files

### piracy_candidates.csv
A CSV file containing all discovered suspicious URLs with columns:
- `found_at` - Timestamp when the URL was discovered
- `query` - Search query that found this URL
- `url` - The full URL
- `domain` - The domain name
- `title` - Page title from search results
- `snippet` - Text snippet from search results

### seen_urls.json
A JSON file that caches all URLs seen across runs to avoid duplicate reporting.

### dmca_report.txt
A formatted DMCA notice draft that you can copy into Google's copyright removal form or send to hosting providers.

## Scheduling

You can schedule this script to run periodically using:

### Linux/Mac (cron)
```bash
# Run daily at 9 AM
0 9 * * * cd /path/to/novel-piracy-detector && /path/to/venv/bin/python piracy_detector.py
```

### Windows (Task Scheduler)
Create a task that runs `python piracy_detector.py` at your desired interval.

## Legal Disclaimer

This tool is designed to help copyright holders protect their work. Always verify that URLs are actually infringing before filing DMCA notices. False or abusive DMCA claims can have legal consequences.

## License

MIT License - See LICENSE file for details

## Support

For issues or questions, please open an issue on GitHub.

