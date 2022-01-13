import time
import math
import pytest
import time
from selenium import webdriver


# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     time.sleep(3)
#     browser.quit()


# @pytest.mark.parametrize('linkk', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
#                                    "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
#                                    "https://stepik.org/lesson/236899/step/1",
#                                    "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1",
#                                    "https://stepik.org/lesson/236905/step/1"])
# def testitest(browser, linkk):
#     link = {linkk}
link = "https://stepik.org/lesson/236895/step/1"
browser = webdriver.Chrome()
browser.get(link)
answer = math.log(int(time.time()))
time.sleep(2)
 
a = browser.find_element_by_xpath("//div[@class='show-plugin']/div/textarea")
a.send_keys(str(answer))

otpravka = browser.find_element_by_xpath("//div[@class='attempt__actions']/button").click
# message = browser.find_element_by_id("verify_message")
# assert "correct" in message.text

# https://stepik.org/lesson/236895/step/1
# https://stepik.org/lesson/236896/step/1
# https://stepik.org/lesson/236897/step/1
# https://stepik.org/lesson/236898/step/1
# https://stepik.org/lesson/236899/step/1
# https://stepik.org/lesson/236903/step/1
# https://stepik.org/lesson/236904/step/1
# https://stepik.org/lesson/236905/step/1
