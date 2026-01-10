# iMyanmarHouse Web Scraper (Mandalay Region)

A Python-based web scraper that extracts real estate listings from iMyanmarHouse.com.

## Features
* **Link Discovery:** Automatically identifies and collects all unique property listing URLs.
* **Deep Scraping:** Navigates into each individual property page.
* **Title Extraction:** Captures the main listing title from the `<h1>` tag.
* **Data Cleaning:** Uses `.get_text(strip=True)` to remove whitespaces.
* **Anti-Blocking:** Uses `time.sleep()` to reduce IP blocking risk.

## Prerequisites
* Python installed
* Required libraries: `pip install requests beautifulsoup4 html5lib`

## Usage
`python Real_Estate_Mandalay.py`
