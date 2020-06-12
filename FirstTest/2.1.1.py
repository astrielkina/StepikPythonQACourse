import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector('body > div > form > div.form-check.form-check-custom > label')
    option1.click()
  #  option2 = browser.find_element_by_css_selector('[for=\'robotsRule\']')
  #  option2.click()

    people_radio = browser.find_element_by_id("robotsRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"


    button = browser.find_element_by_css_selector('button')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
