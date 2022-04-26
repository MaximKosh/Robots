import time

from fake_useragent import UserAgent
from selenium import webdriver

# url = "https://www.whatismybrowser.com/"

useragent = UserAgent()  # объект класса

# user_agents_list = [
#     "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36",
#     "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
#     "Opera/9.80 (Android 4.1.2; Linux; Opera Mobi/ADR-1305251841) Presto/2.11.355 Version/12.10",
#     "Mozilla/5.0 (Android 7.0; Mobile; rv:54.0) Gecko/54.0 Firefox/54.0"
# ]

# options
options = webdriver.ChromeOptions()  # объект класса

# options.add_argument(f"user-agent={random.choice(user_agents_list)}")

# options.add_argument(f"user-agent={useragent.opera}")

# set_proxy
options.add_argument("--proxy-server = 46.229.187.169:53281")

driver = webdriver.Chrome(
    executable_path=r"C:\Users\maxim\Robots\today\chromedriver\chromedriver.exe",
    options=options)

try:
    driver.get("https://2ip.ru")
    time.sleep(15)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit()
