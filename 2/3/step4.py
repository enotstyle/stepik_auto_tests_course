from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button1.click()
    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(1)

    x = browser.find_element(By.ID, 'input_value').text
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(calc(x))
    button2 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button2.click()

finally:
    time.sleep(5)
    browser.quit()