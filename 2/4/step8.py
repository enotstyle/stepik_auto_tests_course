from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, 'price'),'100'))
    button_book = browser.find_element(By.ID, 'book')
    button_book.click()

    answer = WebDriverWait(browser, 15).until(EC.visibility_of_element_located((By.ID, 'answer')))
    x = browser.find_element(By.ID, 'input_value').text
    answer.send_keys(calc(x))
    button_solve = browser.find_element(By.ID, 'solve')
    button_solve.click()

finally:
    time.sleep(5)
    browser.quit()