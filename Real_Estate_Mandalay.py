import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
from datetime import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

#Function Extraction for Title
def get_title(box):
    title_tag = box.find('h2', class_ = 'text-bold')
    return title_tag.get_text(strip = True) if title_tag else 'No Title'

def get_details(box):
    all_p_tags = box.find_all('p', class_= 'main-theme-font-color')

    for p in all_p_tags:
        if p.find('i', class_='fa-map-marker'):
            loc = p.get_text(strip=True)
        elif p.find('i', class_ = 'fa-building-o'):
            prop = p.get_text(strip=True)

    return loc, prop 

#This is the common url for all pages
base_url = "https://www.imyanmarhouse.com/search/for-sale/mandalay-region/all-township/price-0-1000-lakh"
current_page = 1
count = 0


titles_list = []
locations_list = []
property_types_list = []


while True:
    target_url = f"{base_url}?page={current_page}"
    print(f"\n[We are scraping {current_page}...")
    
    #Current Page
    data = requests.get(target_url, headers=headers)
    bsO4 = BeautifulSoup(data.text, 'html5lib')

    #Extracting the info of each peroperty that lies in each box for each page.
    containers = bsO4.find_all('div', class_ = "col-sm-7")

    #loop will stop if there is no list
    if not containers:
        print('We have scrpaed all data')
        break

    for container in containers:
        count += 1
        
        #Using Title Function
        property_title = get_title(container)
        
        #Using Location and property_type Functions
        location, property_type = get_details(container)
        
        
        #Putting Results into Lists
        titles_list.append(property_title)
        locations_list.append(location)
        property_types_list.append(property_type)

        #print(f"{count:<4} | {property_title}")
        #print(f"{' ': <4} | {location}")
        #print(f"{' ':<4} | {property_type}")
        #print("-" * 60)

    next_button = bsO4.find('a', string = 'Next »')

    if next_button:
        current_page += 1
        time.sleep(0.5)

    else:
        print("\n This is the last page")
        break
    
data_dic = {
    'Title' : titles_list,
    'Location' : locations_list,
    'Property_types': property_types_list
    }
df = pd.DataFrame(data_dic)
time_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f'Properties_extracted_{time_str}.xlsx'
df.to_excel(filename, index=False)

    
        

print(f"\n We found total {count} properties")
print(f"Data saved to {filename}")
              



