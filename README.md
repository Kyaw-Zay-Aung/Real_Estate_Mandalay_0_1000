<div align="center">

# 🏢 Mandalay Real Estate Scraper  
🚀 *A beginner-friendly Python web scraper for real estate data analysis*

</div>

---

## 📖 About the Project

**Mandalay Real Estate Scraper** is a **Python-based web scraping tool** that automatically collects **property listings for sale in the Mandalay Region** from **iMyanmarHouse** and exports the data into a structured **Excel file**.

> 🎓 This project was built for **learning and educational purposes**, especially for beginners interested in **web scraping**, **Python**, and **data analysis**.

---

## 📌 What This Scraper Does

The scraper automatically navigates through property listing pages and collects important information for properties priced between:

💰 **0 – 1,000,000,000 MMK (Kyats)**

---

## ✨ Key Features

### 🔄 Automatic Pagination
- Automatically detects and navigates through multiple pages using the **"Next" button** logic.

### 🎯 Targeted Data Extraction
The scraper collects the following details:
- 🏷️ **Property Title** – Main heading of the listing  
- 📍 **Location** – Township or area (extracted from map-marker icons)  
- 🏢 **Property Type** – Categories such as Apartment, Land, etc. (extracted from building icons)

### 📊 Excel Export
- Saves all collected data into a **timestamped `.xlsx` file**
- Easy to open and analyze using **Excel or Google Sheets**

---

## 🛠️ Tech Stack & Requirements

- **Language:** Python 3.x  
- **Libraries:**  
  - `requests`  
  - `beautifulsoup4`  
  - `pandas`  
  - `openpyxl`  
  - `html5lib`

> 💡 Using a **virtual environment** is recommended but optional.

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/mandalay-real-estate-scraper.git
cd mandalay-real-estate-scraper
2️⃣ Create & Activate a Virtual Environment (Recommended)
bash
Copy code
python -m venv myvenv

# Windows
.\myvenv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install requests beautifulsoup4 pandas openpyxl html5lib
▶️ How to Use
Run the scraper from your terminal:

bash
Copy code
python Mandalay_Real_Estate.py
📋 What to Expect
Real-time progress will be displayed in the terminal

After completion, an Excel file will be generated:

text
Copy code
Properties_extracted_YYYY-MM-DD_HH-MM-SS.xlsx
📁 The file will be saved in the project directory.

📁 Project Structure
text
Copy code
mandalay-real-estate-scraper/
├── Mandalay_Real_Estate.py   # Main scraping script
├── myvenv/                   # Virtual environment (do not upload)
└── README.md                 # Project documentation
⚠️ Disclaimer
This project is intended for educational purposes only.

Please respect iMyanmarHouse’s Terms of Service

Always check and follow the website’s robots.txt

Do not use this scraper for commercial or abusive purposes
