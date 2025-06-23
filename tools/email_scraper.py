import requests
import re
import sys
from bs4 import BeautifulSoup

def extract_emails(text):
    # Regex email pattern
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return set(re.findall(email_pattern, text))

def scrape_from_url(url):
    try:
        print(f"🔍 Scraping URL: {url}")
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")
        text = soup.get_text()
        emails = extract_emails(text)
        return emails

    except Exception as e:
        print(f"❌ Failed to scrape: {e}")
        return set()

def scrape_from_file(file_path):
    try:
        print(f"📂 Reading file: {file_path}")
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            return extract_emails(content)
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return set()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python email_scraper.py url https://example.com")
        print("  python email_scraper.py file path/to/file.html")
        sys.exit(1)

    mode = sys.argv[1]
    target = sys.argv[2]

    if mode == "url":
        emails = scrape_from_url(target)
    elif mode == "file":
        emails = scrape_from_file(target)
    else:
        print("❌ Invalid mode. Use 'url' or 'file'.")
        sys.exit(1)

    if emails:
        print(f"\n📧 Found {len(emails)} emails:")
        for email in sorted(emails):
            print(f"  - {email}")
    else:
        print("❌ No emails found.")
