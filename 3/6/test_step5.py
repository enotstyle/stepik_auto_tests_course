from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

driver.get("https://stepik.org/lesson/25969/step/8")