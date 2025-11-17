import requests
import csv
import json
import os
from urllib.parse import urlparse
from datetime import datetime

# ===================== CONFIGURATION =====================

# Your SerpAPI key (get it from https://serpapi.com/)
SERPAPI_KEY = "YOUR_SERPAPI_KEY_HERE"

# Your work information
NOVEL_TITLE = "Level Up Legacy"
AUTHOR_NAME = "MellowGuy"

# The official domain(s) that are allowed to host your novel
OFFICIAL_DOMAINS = {
    "webnovel.com"
}

# Search queries used to find possible infringements
QUERIES = [
    f'"{NOVEL_TITLE}" "{AUTHOR_NAME}"',
    f'"{NOVEL_TITLE}" "MellowGuy"',
    f'"{NOVEL_TITLE}" "webnovel"',
    # You can add more lines with distinctive phrases from chapters if you like, e.g.:
    # '"Level Up Legacy" "unique phrase from chapter 1"',
]

# How many results to request per query (SerpAPI may cap this)
RESULTS_PER_QUERY = 20

# Output files
CANDIDATES_CSV = "piracy_candidates.csv"
SEEN_URLS_FILE = "seen_urls.json"
DMCA_REPORT_FILE = "dmca_report.txt"

# ===================== HELPER FUNCTIONS =====================

def get_domain(url: str) -> str:
    """Extract domain from URL (without www.)."""
    try:
        netloc = urlparse(url).netloc
        return netloc.replace("www.", "").lower()
    except Exception:
        return ""

def load_seen_urls():
    """Load previously seen URLs from JSON file."""
    if not os.path.exists(SEEN_URLS_FILE):
        return set()
    try:
        with open(SEEN_URLS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(data)
    except Exception:
        return set()

def save_seen_urls(seen_urls):
    """Save seen URLs back to JSON file."""
    try:
        with open(SEEN_URLS_FILE, "w", encoding="utf-8") as f:
            json.dump(sorted(list(seen_urls)), f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Error saving seen URLs:", e)

def search_google_serpapi(query: str):
    """Perform a Google search via SerpAPI and return organic results."""
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": RESULTS_PER_QUERY,
        "hl": "en",
    }
    resp = requests.get("https://serpapi.com/search", params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()
    return data.get("organic_results", [])

def append_rows_to_csv(rows, filename):
    """Append rows (list of dicts) to CSV file, writing header if needed."""
    if not rows:
        return
    fieldnames = ["found_at", "query", "url", "domain", "title", "snippet"]
    file_exists = os.path.exists(filename)
    try:
        with open(filename, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            writer.writerows(rows)
    except Exception as e:
        print("Error writing CSV:", e)

def generate_dmca_text(new_entries):
    """
    Generate a DMCA report text block listing newly found URLs.
    This text can be pasted into Google's copyright removal form.
    """
    if not new_entries:
        return ""
    lines = []
    lines.append("=== DMCA / COPYRIGHT INFRINGEMENT NOTICE DRAFT ===")
    lines.append("")
    lines.append("Work being infringed:")
    lines.append(
        f'I am the author and copyright holder of the web novel titled '
        f'"{NOVEL_TITLE}", written under the name "{AUTHOR_NAME}". '
        f'The official, authorized publication of this novel appears on Webnovel at:'
    )
    lines.append(" - https://www.webnovel.com/")
    lines.append("")
    lines.append("Infringing material:")
    lines.append("The following URLs host or make available my novel without my permission "
                 "and reproduce substantial portions (or complete chapters) of my work:")
    for entry in new_entries:
        lines.append(f" - {entry['url']}  (found via query: {entry['query']})")
    lines.append("")
    lines.append("Good-faith belief:")
    lines.append(
        "I have a good-faith belief that the use of the copyrighted material described "
        "above is not authorized by me, my agent, or the law."
    )
    lines.append("")
    lines.append("Accuracy and authority:")
    lines.append(
        "I swear, under penalty of perjury, that the information in this notification "
        "is accurate and that I am the copyright owner or am authorized to act on behalf "
        "of the owner of an exclusive right that is allegedly infringed."
    )
    lines.append("")
    lines.append("Signed,")
    lines.append("[YOUR FULL LEGAL NAME HERE]")
    lines.append("[YOUR CONTACT INFO HERE (email, country, etc.)]")
    return "\n".join(lines)

# ===================== MAIN LOGIC =====================

def main():
    if SERPAPI_KEY == "YOUR_SERPAPI_KEY_HERE":
        print("ERROR: Please edit the script and put your real SERPAPI_KEY.")
        return

    seen_urls = load_seen_urls()
    print(f"Loaded {len(seen_urls)} previously seen URLs.")

    all_new_entries = []
    now = datetime.utcnow().isoformat(timespec="seconds") + "Z"

    for query in QUERIES:
        print(f"\nSearching for: {query}")
        try:
            results = search_google_serpapi(query)
        except Exception as e:
            print(f"Error searching query '{query}': {e}")
            continue

        for r in results:
            url = r.get("link")
            title = r.get("title", "")
            snippet = r.get("snippet", "")

            if not url:
                continue

            domain = get_domain(url)
            if not domain:
                continue

            # Skip official domains
            if domain in OFFICIAL_DOMAINS:
                continue

            # Skip if we've already seen this URL in previous runs
            if url in seen_urls:
                continue

            # Mark as new
            seen_urls.add(url)
            entry = {
                "found_at": now,
                "query": query,
                "url": url,
                "domain": domain,
                "title": title,
                "snippet": snippet,
            }
            all_new_entries.append(entry)
            print(f"  [NEW] {url} ({domain})")

    if not all_new_entries:
        print("\nNo new suspicious URLs found this run.")
        return

    # Save seen URLs
    save_seen_urls(seen_urls)
    print(f"\nUpdated seen URLs ({len(seen_urls)} total).")

    # Append to CSV log
    append_rows_to_csv(all_new_entries, CANDIDATES_CSV)
    print(f"Appended {len(all_new_entries)} new entries to {CANDIDATES_CSV}.")

    # Generate DMCA draft text
    dmca_text = generate_dmca_text(all_new_entries)
    try:
        with open(DMCA_REPORT_FILE, "w", encoding="utf-8") as f:
            f.write(dmca_text)
        print(f"DMCA draft written to {DMCA_REPORT_FILE}.")
    except Exception as e:
        print("Error writing DMCA report file:", e)

    print("\nDone. Review the URLs in:")
    print(f" - {CANDIDATES_CSV}")
    print(f" - {DMCA_REPORT_FILE}")
    print("Then copy the DMCA text into Google's copyright removal form.")

if __name__ == "__main__":
    main()

