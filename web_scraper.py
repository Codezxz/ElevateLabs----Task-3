"""
Welcome to my scraper! Extract the <h1> and all <h2> headings from a CNBC article.

Usage:
    python extract_headings.py "https://www.cnbc.com/2025/06/26/nvidia-shares-rally-overnight-lifts-asian-chip-stocks.html"  # writes Headings_H1_H2.txt
Dependencies:
    pip install requests beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup
from pathlib import Path

HEADERS  = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36" }
OUT_FILE = Path("Headings_H1_H2.txt")
print("Plese enter a news article link: ")
url = input()

def fetch_html(url: str) -> str:
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.text

def grab_headings(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")

    h1_tag = soup.find("h1")
    h2_tags = soup.find_all("h2")

    headings = []

    if h1_tag and h1_tag.get_text(strip=True):
        headings.append('Heading 1 = ' + h1_tag.get_text(" ", strip=True))

    for h2 in h2_tags:
        text = h2.get_text(" ", strip=True)
        if text:                  
            headings.append('Heading 2 = ' + text)

    return headings

def main(url: str) -> None:
    html      = fetch_html(url)
    headings  = grab_headings(html)

    OUT_FILE.write_text("\n".join(headings), encoding="utf-8")
    print(f"Saved {len(headings)} headings -> {OUT_FILE.resolve()}")


main(url)
