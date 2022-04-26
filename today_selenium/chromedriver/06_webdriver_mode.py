
import time
from fake_useragent import UserAgent
from selenium import webdriver

options = webdriver.ChromeOptions()  # объект класса
useragent = UserAgent()
options.add_argument(f"user-agent={useragent.opera}")

# disable webdriver mode
options.add_argument("--disable-blink-features=AutomationControlled")

url = "?"
driver = webdriver.Chrome(
    executable_path=r"C:\Users\maxim\Robots\today\chromedriver\chromedriver.exe",
    options=options)

try:
    driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    time.sleep(10)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
