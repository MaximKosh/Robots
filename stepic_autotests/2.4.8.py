from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as kk
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд,
button = WebDriverWait(browser, 12).until(
       kk.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
browser.find_element_by_id("book").click()

browser.execute_script("window.scrollBy(0, 100);")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x = browser.find_element_by_id("input_value").text
y = calc(x)
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()