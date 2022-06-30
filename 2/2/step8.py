from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Potapov')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('xxx@mail.ru')

    file_button = browser.find_element(By.ID, 'file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    print(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_button.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()



finally:
    time.sleep(5)
    browser.quit()