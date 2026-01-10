iMyanmarHouse Web Scraper (Mandalay Region)

A Python-based web scraper that extracts real estate listings from iMyanmarHouse.com, focusing on properties located in the Mandalay Region within a price range of 0–1000 Lakhs.

Features

Link Discovery
Automatically identifies and collects all unique property listing URLs containing /sale/ from the search results page.

Deep Scraping
Navigates into each individual property page to extract specific listing details.

Title Extraction
Captures the main listing title from the <h1> tag of each property page.

Data Cleaning
Uses .get_text(strip=True) to remove unnecessary whitespace and newlines.

Anti-Blocking Measures
Uses time.sleep() to regulate request frequency and reduce the risk of IP blocking.

Prerequisites

Python installed

Required libraries:

pip install requests
pip install beautifulsoup4
pip install html5lib

Usage
python Real_Estate_Mandalay.py

Logic Overview

Initial Request
Sends an HTTP GET request to the search results URL using a custom User-Agent header.

Parsing
Parses HTML content using BeautifulSoup with the html5lib parser.

URL Filtering
Extracts all <a> tags and filters valid property links (/sale/), avoiding duplicates.

Iterative Scraping
Visits each property page and retrieves the listing title.

Disclaimer

This project is for educational purposes only.
Always review the website’s robots.txt file and Terms of Service before performing large-scale scraping.
