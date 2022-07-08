from selenium.webdriver.common.by import By
import time

link = 'https://stepik.org/'

def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(5)