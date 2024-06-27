from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up the WebDriver (replace with the path to your WebDriver)
driver = webdriver.Chrome()

# Open the web application
driver.get("C:/Users/tanma/Downloads/new/pro/pro/templates/new.html")

# Locate elements and perform actions
age = driver.find_element(By.ID, 'age')
adate = driver.find_element(By.ID, 'adate')
ddate = driver.find_element(By.ID, 'ddate')
gender = driver.find_element(By.ID, 'gender')
ethnicity = driver.find_element(By.ID, 'ethnicity')
admission_type = driver.find_element(By.ID, 'admission_type')
insurance = driver.find_element(By.ID, 'insurance')
marital_status= driver.find_element(By.ID, 'marital_status')
submitBtn = driver.find_element(By.ID, 'submitBtn')


# Enter credentials and submit
age.send_keys('34')
adate.send_keys('12/04/2024')
ddate.send_keys('15/04/2024')
submitBtn.click()

# Wait for some element to be visible after login
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'results'))
    )
    print("Data Submitted successfully")
except:
    print("Submission failed or element not found")

# Close the WebDriver
driver.quit()