import unittest
import time
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def test_something(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first = browser.find_element_by_xpath("//div[1]/input")
        first.send_keys("Max")

        last = browser.find_element_by_xpath("//div[2]/input")
        last.send_keys("Volkov")

        email = browser.find_element_by_xpath("//div[3]/input")
        email.send_keys("maxumus.km@mail.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        time.sleep(1)
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_something1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first = browser.find_element_by_xpath("//div[1]/input")
        first.send_keys("Max")

        last = browser.find_element_by_xpath("//div[2]/input")
        last.send_keys("Volkov")

        email = browser.find_element_by_xpath("//div[3]/input")
        email.send_keys("maxumus.km@mail.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == '__main__':
    unittest.main()






