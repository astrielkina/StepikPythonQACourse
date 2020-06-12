from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()

    browser.get(link)
    x = int(browser.find_element_by_id('input_value').text)
    res = calc(x)
    browser.execute_script("window.scrollBy(0, 200);")
    button = browser.find_element_by_tag_name("button")
 #   browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(res)
    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()


    button.click()

    assert True

except Exception as error:
    print(f'There is an error: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
