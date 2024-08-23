from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time
from bs4 import BeautifulSoup
import json 
import re
 
# Preparing json data 
def clean_text(text): 
    text = text.replace('\u00b7', ' - ') 
    text = re.sub(r'\s*\n\s*', ' ', text)
    return text 

for_json_data = []

try: 
    with open("scrapping/linkedin/user_experience.html") as f:
        html_doc = f.read() 
    soup = BeautifulSoup(html_doc, 'html.parser')
    elements = soup.select('.artdeco-list__item')  # Using CSS selector 

    # Iterate over the elements and extract data
    for item in elements:  
        logo_url = ''
        company_name = ''
        job_type = ''
        duration = ''
        location = ''
        skill = '' 
        skill_url = ''
        additional_data = ''
        
        logo_tag = item.find('a', attrs={'data-field': 'experience_company_logo'})
        if logo_tag:
            logo_url = logo_tag.find('img')['src']  
        
        # Extract company name and position
        company_tag = item.find('div', class_='t-bold') 
        company_name = company_tag.find('span') 
        if company_tag:
            company_name = company_name.get_text(strip=True) 
         
        print(company_name)
        break
         
        type_tag = item.find('span', class_='t-14 t-normal')
        if type_tag:
            job_type = type_tag.find('span') 
            job_type = job_type.get_text(strip=True) 
        
        # Extract employment duration
        duration_tag = item.find('span', class_='t-black--light')
        if duration_tag:
            duration = duration_tag.find('span') 
            duration = duration.get_text(strip=True)  
 
        # Find location
        parent_div = item.find('div', class_="justify-space-between") 
        span_elements = parent_div.find_all('span', class_="t-black--light")
         
        location = span_elements[-1].find('span').get_text(strip=True) if span_elements else None 
         
        # Additional
        additional_div = item.find('div', class_="pvs-entity__sub-components") 
        additinal_data = additional_div.find_all('div', attrs={'data-view-name': 'profile-component-entity'})
         
        additional_all_data = []
        for ad in additinal_data:
            all_data = {}
            addition_data = ad.find('span', attrs={'aria-hidden':'true'})
            all_data['title'] = clean_text(addition_data.get_text(strip=True))
            addition_data = ad.find('span', class_="pvs-entity__caption-wrapper")
            all_data['duration'] = clean_text(addition_data.get_text(strip=True))
            additional_all_data.append(all_data) 
        
        skill_tag = item.find('strong') 
        skill = skill_tag.get_text(strip=True) 
        skill_url = item.find('li', class_="pvs-list__item--with-top-padding")
        
        if skill_url:
            skill_url = skill_url.find('a')['href'] 
         
        for_json_data.append({
            'company_logo': clean_text(logo_url),
            'company_name': clean_text(company_name),
            'type': clean_text(job_type),
            'duration': clean_text(duration),  
            'location': clean_text(location),
            'skill': clean_text(skill),
            'skill_url': clean_text(skill_url),
            'additional_data': additional_all_data
        })
    
except Exception as e:
    print('Error: ',e)
    
print(json.dumps(for_json_data, indent=4))



