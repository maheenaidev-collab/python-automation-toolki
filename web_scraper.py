"""
Web Scraper - Extract data from any website
Author: Maheen | AI & ML Engineer
"""

import requests
from bs4 import BeautifulSoup
import csv
import json


def scrape_website(url, tag="p"):
    """Scrape text content from a website"""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    data = []
    for element in soup.find_all(tag):
        text = element.get_text(strip=True)
        if text:
            data.append(text)
    return data


def save_to_csv(data, filename="output.csv"):
    """Save scraped data to CSV"""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Content"])
        for item in data:
            writer.writerow([item])
    print(f"Data saved to {filename}")


def save_to_json(data, filename="output.json"):
    """Save scraped data to JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    url = input("Enter URL to scrape: ")
    results = scrape_website(url)
    print(f"\nFound {len(results)} items!")
    
    save_to_csv(results)
    save_to_json(results)
