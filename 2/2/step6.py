from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text

    input = browser.find_element(By.ID, 'answer')
    browser.execute_script('return arguments[1].scrollIntoView(true);', input)
    input.send_keys(calc(x))

    check = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script('return arguments[0].scrollIntoView(true);', check)
    check.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radio)
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    button.click()

finally:
    time.sleep(5)
    browser.quit()