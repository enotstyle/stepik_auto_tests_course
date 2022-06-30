from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    answer = calc(x)
    input_ans = browser.find_element(By.ID, 'answer')
    input_ans.send_keys(answer)
    robot_check = browser.find_element(By.ID, 'robotCheckbox')
    robot_check.click()
    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
