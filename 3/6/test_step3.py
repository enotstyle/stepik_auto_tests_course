import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time
import math

final_message = ''


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link_page', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_send_message(browser, link_page):
    link = f'https://stepik.org/lesson/{link_page}/step/1'

    browser.get(link)

    input_stepik = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, 'ember85')))
    input_stepik.send_keys(str(math.log(int(time.time()))))

    button = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
    button.click()

    message_correct = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))

    global final_message
    if message_correct.text != 'Correct!':
        final_message += message_correct.text

    print(final_message)
    assert message_correct.text == 'Correct!', 'MESSAGE IS NOT "Correct!"'


if __name__ == "__main__":
    pytest.main()
