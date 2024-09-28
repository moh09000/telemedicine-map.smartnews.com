from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# تحميل WebDriver المناسب لمتصفحك
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')  # ضع المسار المناسب لـ ChromeDriver
# أو يمكن استخدام Firefox
# driver = webdriver.Firefox(executable_path='/path/to/geckodriver')

# فتح الموقع المطلوب
driver.get('https://smartmockups.com')

# إضافة وقت انتظار لتأكد من تحميل الصفحة
time.sleep(3)

# العثور على حقول البريد الإلكتروني وكلمة المرور
email_input = driver.find_element(By.NAME, 'email')  # استبدل 'email' بمعرف العنصر الصحيح إذا كان مختلفًا
password_input = driver.find_element(By.NAME, 'password')  # استبدل 'password' بمعرف العنصر الصحيح إذا كان مختلفًا

# إدخال البريد الإلكتروني وكلمة المرور
email_input.send_keys('wejari9637@skrak.com')  # استبدل بالبريد الإلكتروني الخاص بك
password_input.send_keys('your_password')  # استبدل بكلمة المرور الخاصة بك

# العثور على زر "تسجيل الدخول" والنقر عليه
login_button = driver.find_element(By.XPATH, '//*[@id="login_button_id"]')  # استبدل 'login_button_id' بالمسار المناسب
login_button.click()

# الانتظار قليلاً للتأكد من نجاح عملية تسجيل الدخول
time.sleep(5)

# إغلاق المتصفح بعد الانتهاء
driver.quit()
