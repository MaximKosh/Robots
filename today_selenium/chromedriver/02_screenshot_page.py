import time

from selenium import webdriver

url = "https://www.instagram.com/"
driver = webdriver.Chrome(executable_path=r"C:\Users\maxim\Robots\today\chromedriver\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(5)

    driver.get_screenshot_as_file("1.png")
    driver.get(url="https://nebesadance.ru/")
    time.sleep(5)
    driver.save_screenshot("2.png")
    time.sleep(2)
except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
