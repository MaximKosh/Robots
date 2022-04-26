import random
import time
from multiprocessing import Pool

from selenium import webdriver

# options
options = webdriver.ChromeOptions()

# user-agent
options.add_argument("--disable-blink-features=AutomationControlled")


# headless mode
# options.add_argument("--headless")
# options.headless = True

# urls_list = ["https://www.google.com/","https://stackoverflow.com", "https://www.google.com/", "https://vk.com"]
#
#
# def get_data(url):
#     try:
#         driver = webdriver.Chrome(
#             executable_path=r"C:\Users\maxim\Robots\today\chromedriver\chromedriver.exe",
#             options=options
#         )
#
#         driver.get(url=url)
#         time.sleep(5)
#         driver.get_screenshot_as_file(f"media/{url.split('//')[1]}.png")
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#
#
# if __name__ == '__main__':
#     p = Pool(processes=3)
#     p.map(get_data, urls_list)      # код ф-ии применяется к каждому итерируемому объекту (к каждому url из urls_list)

def get_data(url):
    try:
        driver = webdriver.Chrome(
            executable_path=r"C:\Users\maxim\Robots\today\chromedriver\chromedriver.exe",
            options=options
        )
        driver.get(url=url)
        time.sleep(5)
        # ищем видео в блоке 2 find
        driver.find_elements_by_class_name("tiktok-kd7foj-DivVideoWrapper e1cpsqt16").find_elements_by_class_name(
            "tiktok-196h150-CanvasVideoCardPlaceholder e1cpsqt0").click()
        driver.implicitly_wait(10)
        time.sleep(random.randrange(3, 10))
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    process_count = int(input("Enter the number of processes: "))
    url = input("Enter the URL: ")
    urls_list = [url] * process_count
    print(urls_list)

    # мультипроцессинг
    p = Pool(processes=process_count)
    # применяем функцию к каждому процессу
    p.map(get_data, urls_list)
