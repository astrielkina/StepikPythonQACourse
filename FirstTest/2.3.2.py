from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector('button')
    button.click()

    browser.switch_to.window(browser.window_handles[1])



    x = int(browser.find_element_by_id('input_value').text)
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_css_selector('body > form > div > div > button')
    button.click()
    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()
    #assert True

except Exception as error:
    print(f'There is an error: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
