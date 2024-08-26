from selenium import webdriver 
from selenium.webdriver.common.by import By 
import time   
from PIL import Image
import pytesseract   
import requests

driver = webdriver.Chrome()

# Login to LinkedIn
def login_linkedin():
    ''' Login LinkedIn '''
    driver.get('https://www.linkedin.com/login')
    time.sleep(1)
    username = driver.find_element(By.ID, "username")
    username.send_keys("roshni.prajapati@bonamisoftware.com")
    password = driver.find_element(By.ID, "password") 
    password.send_keys("Y8$kP4@z!LwQ1tVb")
    return driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Function to check if CAPTCHA is present
def is_captcha_present(image_path):
    ''' Use OCR to check if CAPTCHA is detected in the image '''
    text = pytesseract.image_to_string(Image.open(image_path))
    return "quick security check" in text.lower() 

# Function to save a screenshot and check for CAPTCHA
def check_captcha():
    ''' Function to save a screenshot and check for CAPTCHA '''
    file_name_unique = time.time()
    screenshot_path = f'scrapping/linkedin/screenshot/screenshot{int(file_name_unique)}.png'
    driver.save_screenshot(screenshot_path)
    return is_captcha_present(screenshot_path)

# Saving User Experince in HTML file
def save_user_experience(username):
    ''' Saving User Experince in HTML file '''
    driver.get(f'https://www.linkedin.com/in/{username}/details/experience/') 
    time.sleep(5)
    
    data = driver.find_elements(By.CSS_SELECTOR, '.scaffold-finite-scroll__content')
    for elem in data: 
        d = elem.get_attribute("outerHTML")
        with open(f"scrapping/linkedin/experience/{username}_experience.html", "w", encoding="utf-8") as f:
            f.write(d) 
    return f"{username} Experience has been saved successfully"
    
# Wait and check until logged in and redirected to the correct URL
while True:
    current_url = driver.current_url 

    if 'feed' in current_url: 
        lst = ['vishal-rana-266309243', 'rohit-kumar-10b925324', 'utkarsh-singh-2a2845215', 'arya-shesham', 'irom-jenny-devi-688843178', 
               'nilabhsahu', 'sharma-tnahsin', 'simran-arora-she-her-933362194', 'akash-mittal-6997231a1', 'ayushdubey7799', 
               'gaurav-k-8a7920324', 'shreya-chauhan-ab253220a', 'lalitbarwal27', 'vivek-k-9aa022221', 'sudhanshu-gautam-b61305158', 
               'shailendra0710', 'bhvaikjain', 'krishna-singh-b375aa214', 'sanjay-rathor-82a269211', 'prince-kumar-07a69b2a0', 
               'namangrover', 'chandan-sahu-b87376191', 'satishpandey01', 'piyushsinghcse1', 'kartiknegi', 
               'vincentrkumar', 'tanishchaurasia', 'jkrishna31', 'abhishekkr3101', 'bhupesh-singh-nikhurpa']
        for user in lst: 
            print(save_user_experience(user)) 
        break  
    elif check_captcha():
        print("CAPTCHA detected! Please solve it manually.")
        time.sleep(10)  # Give time for the user to solve the CAPTCHA manually
    else:
        login_linkedin()
        print("Waiting for login...")
        time.sleep(5)  # Adjust the wait time if needed 

# Close the browser when done
driver.quit()
