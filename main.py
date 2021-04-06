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

    write_elem= driver.find_element_by_id("p_group_name")
    print(type(write_elem))

    write_elem.send_keys("09-821")
    write_elem.send_keys(Keys.ENTER)
    # write_elem.send_keys(Keys.RETURN)
    time.sleep(2)
    html_page = driver.page_source
    soup = BeautifulSoup(html_page, 'html5lib')
    table = soup.findChildren('table')
    my_table = table[len(table)-1]
    # получение тегов и печать значений
    rows = my_table.findChildren(['th', 'tr'])
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.text
            print(value)
    # soup = BeautifulSoup(html_page, 'html5lib')
    # table = soup.findChildren('table')
    # my_table = table[0]
    # rows = my_table.findChildren(['th', 'tr'])
    # for row in rows:
    #     cells = row.findChildren('td')
    #     for cell in cells:
    #         value = cell.text
    #         print(value)

if __name__ == '__main__':
    print_hi('PyCharm')

