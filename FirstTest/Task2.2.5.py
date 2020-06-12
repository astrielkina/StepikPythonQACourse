from selenium import webdriver
import time
import math
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('input[type="text"]:nth-child(2)')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('input[type="text"]:nth-child(4)')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector('input[type="text"]:nth-child(6)')
    input3.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname('__file__'))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '123.txt')  # добавляем к этому пути имя файла
    browser.find_element_by_css_selector('#file').send_keys(file_path)


    button = browser.find_element_by_css_selector('button')
    button.click()

    #assert True

except Exception as error:
    print(f'There is an error: {error}')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
