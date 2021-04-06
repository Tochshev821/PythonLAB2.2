from bs4 import BeautifulSoup
from selenium import webdriver
from io import BytesIO
from urllib.request import urlretrieve
from selenium.webdriver.common.keys import Keys
import time
import subprocess



def print_hi(name):
    driver = webdriver.Chrome()
    driver.get("https://kpfu.ru/studentu/ucheba/raspisanie")

    write_elem=driver.find_element_by_id("p_group_name")
    print(type(write_elem))

    write_elem.send_keys("09-821")
    write_elem.send_keys(Keys.ENTER)
    # write_elem.send_keys(Keys.RETURN)

    # ('https://shelly.kpfu.ru/pdf/picture/mainpage_new/but_show.png')


if __name__ == '__main__':
    print_hi('PyCharm')

