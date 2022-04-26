import pickle
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pass_vk import email_vk, password_vk

options = webdriver.ChromeOptions()  # объект класса
useragent = UserAgent()
options.add_argument(f"user-agent={useragent.opera}")

url = "https://www.vk.com/"
driver = webdriver.Chrome(executable_path=r"C:\Users\maxim\Robots_my\today_selenium\chromedriver\chromedriver.exe")

try:
    # driver.get(url=url)
    #
    # email = driver.find_element_by_id("index_email")
    # email.clear()
    # email.send_keys(email_vk)
    #
    # password = driver.find_element_by_id("index_pass")
    # password.clear()
    # password.send_keys(password_vk)
    # time.sleep(3)
    # password.send_keys(Keys.ENTER)
    # # come_button = driver.find_element_by_id("index_login_button").click()
    # time.sleep(5)
    #
    # # cookies
    # pickle.dump(driver.get_cookies(), open(f"{email_vk}_cookies", "wb"))
    #
    driver.get("https://vk.com/")
    time.sleep(3)
    driver.delete_all_cookies()
    for cookie in pickle.load(open(f"{email_vk}_cookies", "rb")):
        driver.add_cookie(cookie)
    time.sleep(5)
    driver.refresh()
    time.sleep(15)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
