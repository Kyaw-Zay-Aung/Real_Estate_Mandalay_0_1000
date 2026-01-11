🏢 #Mandalay Real Estate Scraper
A powerful Python-based web scraper designed to collect property listings from iMyanmarHouse. It automates the data collection process for the Mandalay Region and exports the results into clean, analysis-ready Excel files.

Note: This project was created for educational purposes, perfect for beginners interested in web scraping and data analysis.

📌 Project Overview
The scraper systematically visits listing pages to gather information on properties priced between 0 and 1,000 Lakhs MMK.

✨ Key Features
🔄 Automatic Pagination: Automatically detects the "Next" button to crawl through all available search results.

🎯 Targeted Extraction: Precisely scrapes:

Property Title – The main heading of the listing.

Location – Township/Area details (via map-marker icons).

Property Type – Categories like Apartment or Land (via building icons).

📊 Excel Export: Generates timestamped .xlsx files automatically using Pandas.

🛠️ Tech Stack & Prerequisites
Language: Python 3.x

Libraries: requests, BeautifulSoup4, Pandas, openpyxl, html5lib

📥 Installation & Setup
1️⃣ Clone the Repository
Bash

git clone https://github.com/your-username/mandalay-real-estate-scraper.git
cd mandalay-real-estate-scraper
2️⃣ Environment Setup
It is highly recommended to use a Virtual Environment:

PowerShell

python -m venv myvenv
# Activate on Windows:
.\myvenv\Scripts\activate
3️⃣ Install Dependencies
PowerShell

pip install requests beautifulsoup4 pandas openpyxl html5lib
▶️ How to Use
Run the script directly from your terminal:

PowerShell

python Mandalay_Real_Estate.py
📋 What to Expect:
The terminal will display real-time progress for each page being scraped.

Once complete, a new file will appear in your folder:

Properties_extracted_YYYY-MM-DD_HH-MM-SS.xlsx

📁 Project Structure
Plaintext

mandalay-real-estate-scraper/
├── Mandalay_Real_Estate.py   # Core logic for scraping
├── myvenv/                   # Local environment (do not upload)
└── README.md                 # Project documentation


⚠️ Disclaimer
This tool is for educational purposes only.

Please respect iMyanmarHouse’s Terms of Service.

Always check the website’s robots.txt.

Avoid commercial or abusive use of this scraper.
