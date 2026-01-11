🏢 Mandalay Real Estate Scraper

A Python-based web scraper that collects property listings for sale in the Mandalay Region from iMyanmarHouse and saves the data into an Excel file for easy analysis.

This project was created for learning and educational purposes, especially for beginners interested in web scraping and data analysis.

📌 What This Scraper Does

The scraper automatically visits real estate listing pages and collects useful information about properties priced between 0 and 1,000,000,000 MMK.

✨ Features

🔄 Automatic Pagination
Moves through multiple pages by detecting and clicking the “Next” page logic.

🎯 Targeted Data Extraction
Collects important property details:

Property Title – Main heading of the listing

Location – Township or area (from map-marker icons)

Property Type – Example: Apartment, Land (from building icons)

📊 Excel Export
Saves all scraped data into a timestamped .xlsx file, making it easy to open in Excel.

🛠️ Prerequisites

Before running the project, make sure you have:

Python 3.x installed

Virtual Environment (recommended, but optional)

📥 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/mandalay-real-estate-scraper.git
cd mandalay-real-estate-scraper

2️⃣ Create & Activate a Virtual Environment
python -m venv myvenv

# On Windows
.\myvenv\Scripts\activate

3️⃣ Install Required Libraries
pip install requests beautifulsoup4 pandas openpyxl html5lib

▶️ How to Use

Run the script from your terminal:

python Mandalay_Real_Estate.py

What Happens Next?

The script shows real-time progress (which page is being scraped)

When finished, it generates an Excel file like:

Properties_extracted_YYYY-MM-DD_HH-MM-SS.xlsx


📁 The file will appear in the project folder

📁 Project Structure
mandalay-real-estate-scraper/
│
├── Mandalay_Real_Estate.py   # Main scraping script
├── myvenv/                   # Virtual environment (local)
├── README.md                 # Project documentation

⚠️ Disclaimer

This project is created for educational purposes only.

Please respect iMyanmarHouse’s Terms of Service

Check and follow the website’s robots.txt

Do not use this scraper for commercial or abusive purposes
