from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_available_basket_button(browser):
    browser.get(link)
    button_basket = browser.find_elements(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    print(button_basket)
    assert button_basket, 'Нет кнопки "Добавить в корзину"'
    time.sleep(5)