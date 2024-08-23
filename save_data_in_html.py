from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time 

driver = webdriver.Chrome()
'''
Login to LinkedIn
'''
 
driver.get('https://www.linkedin.com/login')
time.sleep(3)

username = driver.find_element(By.ID, "username")
username.send_keys("roshni.prajapati@bonamisoftware.com")
password = driver.find_element(By.ID, "password") 
password.send_keys("Y8$kP4@z!LwQ1tVb")
driver.find_element("xpath", "//button[@type='submit']").click()

'''
Wait for login
'''
time.sleep(5) 
user_name = 'piyushsinghcse1'
html_doc = driver.get(f'https://www.linkedin.com/in/piyushsinghcse1/details/experience/')

time.sleep(5) 

data = driver.find_elements(By.CSS_SELECTOR, '.scaffold-finite-scroll__content')
for elem in data: 
    d = elem.get_attribute("outerHTML")
    with open(f"scrapping/linkedin/{user_name}_experience.html", "w", encoding="utf-8") as f:
        f.write(d) 

print(data)

driver.close()
 



