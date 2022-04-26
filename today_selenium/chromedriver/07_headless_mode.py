import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pass_vk import email_vk, password_vk

options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# headless mode
# options.add_argument("--headless")
options.headless = True

url = "https://www.vk.com/"
driver = webdriver.Chrome(executable_path=r"C:\Users\maxim\Robots\today\chromedriver\chromedriver.exe",
                          options=options)

try:
    driver.get(url=url)

    email = driver.find_element_by_id("index_email")
    email.clear()
    email.send_keys(email_vk)

    password = driver.find_element_by_id("index_pass")
    password.clear()
    password.send_keys(password_vk)
    time.sleep(3)
    password.send_keys(Keys.ENTER)
    time.sleep(6)

    print("Going to the video page...")
    video_page = driver.find_element_by_link_text("")
    video_page.click()

    print("Start watching the video...")
    # открываю видео, не получается
    print("Finish watching the video...")

    time.sleep(15)



except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
