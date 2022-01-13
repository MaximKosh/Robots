from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import os
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")
browser.find_element_by_xpath("//button").click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x = browser.find_element_by_id("input_value").text
y = calc(x)
browser.find_element_by_id('answer').send_keys(y)
browser.find_element_by_class_name('btn-primary').click()


# успеваем скопировать код
time.sleep(5)
# закрываем браузер после всех манипуляций
browser.quit()

#       browser.execute_script("window.scrollBy(0, 100);")
#   current_dir = os.path.abspath(os.path.dirname(__file__))
#   file_path = os.path.join(current_dir, 'file.txt')
#   vi.send_keys(file_path)
# browser.switch_to.alert переключение на alert сообщение в браузере