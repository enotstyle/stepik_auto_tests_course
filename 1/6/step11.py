from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
    first.send_keys('Ivan')
    last = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    last.send_keys('Ivanov')
    email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
    email.send_keys('Ivan@ivanov')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(1)

    welcome_label = browser.find_element(By.TAG_NAME, 'h1')
    welcome_text = welcome_label.text

    assert welcome_text == 'Congratulations! You have successfully registered!', 'label не прошел проверку'

finally:
    time.sleep(10)
    browser.quit()