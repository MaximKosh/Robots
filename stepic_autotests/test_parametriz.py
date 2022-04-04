import math
import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    time.sleep(5)
    browser.quit()


@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
# вызываем фикстуру в тесте, передав ее как параметр
class TestMainPage1():

    def test1(self, browser, link):
        browser.get(link)
        answer = math.log(int(time.time()))
        # print(answer)
        time.sleep(5)
        link_1 = browser.find_element_by_xpath("//div/textarea")
        link_1.send_keys(str(answer))
        cont = browser.find_element_by_xpath("//div/section/div/div[1]/div[4]/button").click
        message = browser.find_element_by_id("ember95")
        assert "correct" in message.text
        time.sleep(35)



