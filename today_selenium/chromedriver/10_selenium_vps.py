import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pass_vk import email_vk, password_vk

options = webdriver.ChromeOptions()

# user-agent
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

# headless mode
options.add_argument("--headless")
options.headless = True

url = "https://www.vk.com/"
driver = webdriver.Chrome(executable_path=r"C:\Users\maxim\Robots\today\chromedriver\chromedriver.exe",
                          options=options)
driver.set_window_size(1440, 900)

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

    print("Going to the profile page...")
    my_page = driver.find_element_by_xpath("//li[1]/a/span[1]").click()

    print("Click on the comment icon...")
    driver.implicitly_wait(10)
    time.sleep(5)

    element = driver.find_element_by_css_selector(
        "div[class*='PostBottomAction PostBottomAction--withBg comment _comment _reply_wrap empty']")
    driver.execute_script('arguments[0].click()', element)

    print("Writing comment...")
    field_comment = driver.find_elements_by_class_name("submit_post_field")[1].send_keys("hi" + Keys.ENTER)
    time.sleep(5)
    print("work is done.")

    # cookies = driver.get_cookies()
    # for ck in cookies:
    #     print(ck)

    # comment = driver.find_element_by_class_name("comment").find_element_by_class_name("_like_button_icon").click()
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "_like_button_icon"))).click()
    time.sleep(5)

    # print("Going to the video page...")
    # video_page = driver.find_element_by_xpath("//li[9]/a/span[1]")
    # video_page.click()
    # time.sleep(5)
    #
    # print("Start watching the video...")
    # list_video = driver.find_elements_by_xpath('//*[@id="video_type_trends_list"]/div')[random.randint(0, 10)].click()
    # print(list_video)
    # time.sleep(15)
    # print("Finish watching the video...")



except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
