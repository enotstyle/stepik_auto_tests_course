from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    pic_treasure = browser.find_element(By.ID, 'treasure')
    valuex = pic_treasure.get_attribute('valuex')
    answer = calc(valuex)
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(answer
    robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
    robotCheckbox.click()
    robotsRule = browser.find_element(By.ID, 'robotsRule')
    robotsRule.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
