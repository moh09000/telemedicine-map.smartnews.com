from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Path to your WebDriver executable (adjust the path based on your system)
service = Service('/usr/bin/chromedriver')  # Set the correct path for ChromeDriver
driver = webdriver.Chrome(service=service)  # Use 'service' argument instead of 'executable_path'

# List of emails and passwords
credentials = [
    {"email": "wejari9637@skrak.com", "password": "wejari9637@skrak.com"},
    # Add more credentials here
]

# Target URL
login_url = "https://smartmockups.com"

# Function to log in with a given email and password
def login(email, password):
    driver.get(login_url)
    time.sleep(2)  # Let the page load

    # Adjust the element locators based on the page's structure
    email_field = driver.find_element(By.NAME, 'email')  # Adjust to your site's form structure
    password_field = driver.find_element(By.NAME, 'password')  # Adjust accordingly

    # Clear fields and enter credentials
    email_field.clear()
    password_field.clear()

    email_field.send_keys(email)
    password_field.send_keys(password)

    # Submit the form (adjust the locator for the button)
    submit_button = driver.find_element(By.ID, 'login-button')  # Adjust accordingly
    submit_button.click()

    time.sleep(5)  # Wait to see the result

# Iterate over credentials and login
for credential in credentials:
    print(f"Logging in with {credential['email']}")
    login(credential['email'], credential['password'])
    time.sleep(3)  # Pause between attempts

# Close the browser
driver.quit()
