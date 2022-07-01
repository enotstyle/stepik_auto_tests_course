from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

def fill_form(link):
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
    return welcome_text

class Test_unittest(unittest.TestCase):

    def test_reg1(self):
        self.assertEqual(fill_form('http://suninjuly.github.io/registration1.html'),
                         'Congratulations! You have successfully registered!', 'registration is failed')


    def test_reg2(self):
        self.assertEqual(fill_form('http://suninjuly.github.io/registration2.html'),
                         'Congratulations! You have successfully registered!', 'registration is failed')


if __name__ == '__main__':
    unittest.main()