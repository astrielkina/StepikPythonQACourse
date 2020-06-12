from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects2.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)
    res = int(browser.find_element_by_id('num1').text) + int(browser.find_element_by_id('num2').text)
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(res))  # ищем элемент с текстом "res"

    button = browser.find_element_by_css_selector('button')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()


