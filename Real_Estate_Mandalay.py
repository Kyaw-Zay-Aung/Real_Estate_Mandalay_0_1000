import requests
from bs4 import BeautifulSoup
import time


url = "https://www.imyanmarhouse.com/search/for-sale/mandalay-region/all-township/price-0-1000-lakh"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

data = requests.get(url, headers=headers)
web_data = data.text
bsObj = BeautifulSoup(web_data, 'html5lib')

if data.status_code == 200:    
    all_links = bsObj.find_all('a', href=True)    
    property_links = []
    for link in all_links:
        href = link.get('href', '')
        if '/sale/' in href and href not in property_links:
           
            if not href.startswith('http'):
                href = "https://www.imyanmarhouse.com" + href
            property_links.append(href)
        
            
    #print(property_links)
    count = 0
    for each_link in property_links:
        count += 1
        print(count)
        print(each_link)
        print('\n')
    print(f"The number of link found: {len(property_links)}")
    print('Accessed Successfully')
    
else:
    print('There is an error')
    
count = 0
for every_link in property_links:
    
    count += 1
    try:
        
        desc_request = requests.get(every_link, headers=headers)
        if desc_request.status_code == 200:
                desc_soup = BeautifulSoup(desc_request.text, 'html5lib')
                h1_text = desc_soup.find('h1')
                
                if h1_text:
                    print(count)
                    print(f"Link: {every_link}")
                    print(f"Title: {h1_text.get_text(strip=True)}")
                    print("-" * 30)
            
    # ၃။ Website က block မလုပ်အောင် ခဏနားပေးမယ် (အရေးကြီးပါတယ်)
        time.sleep(0.5) 
        
    except Exception as e:
        print(f"Error scraping {each_link}: {e}")
        



    
    

    
    

    
    





